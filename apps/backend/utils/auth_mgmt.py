from functools import wraps
import logging
from django.http import JsonResponse
import jwt
import requests
from urllib.request import urlopen
import os
import json
from django.conf import settings
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth import authenticate

logger = logging.getLogger(__name__)

class Auth0JSONWebTokenAuthentication(BaseAuthentication):
    def get_jwks(self):
        AUTH0_DOMAIN=os.getenv('AUTH0_DOMAIN')
        jsonurl = urlopen(f"https://{AUTH0_DOMAIN}/.well-known/jwks.json")
        jwks = json.loads(jsonurl.read())
        
        return jwks

    def authenticate(self, request):
        AUTH0_DOMAIN=os.getenv('AUTH0_DOMAIN')
        AUDIENCE=os.getenv('AUDIENCE')
        auth_header = request.META.get('HTTP_AUTHORIZATION', None)
        if not auth_header:
            logger.debug("No authorization header provided")
            return None
        
        parts = auth_header.split()
        if parts[0].lower() != 'bearer':
            raise AuthenticationFailed('Authorization header must start with Bearer')
        elif len(parts) == 1:
            raise AuthenticationFailed('Token not found')
        elif len(parts) > 2:
            raise AuthenticationFailed('Authorization header must be Bearer token')

        token = parts[1]
        jwks = self.get_jwks()
        unverified_header = jwt.get_unverified_header(token)
        rsa_key = {}
        for key in jwks['keys']:
            if key['kid'] == unverified_header['kid']:
                rsa_key = {
                    'kty': key['kty'],
                    'kid': key['kid'],
                    'use': key['use'],
                    'n': key['n'],
                    'e': key['e']
                }

        if rsa_key:
            try:
                payload = jwt.decode(
                    token,
                    rsa_key,
                    algorithms=settings.AUTH0_ALGORITHMS,
                    audience=f"http://{AUDIENCE}/",
                    issuer=f"https://{AUTH0_DOMAIN}/"
                )
                logger.debug(f"Token payload: {payload}")
            except jwt.ExpiredSignatureError:
                raise AuthenticationFailed('Token is expired')
            except jwt.JWTClaimsError:
                raise AuthenticationFailed('Incorrect claims, please check the audience and issuer')
            except Exception:
                logger.exception("Unable to parse authentication token")
                raise AuthenticationFailed('Unable to parse authentication token.')

            return (AnonymousUser(), token)

        raise AuthenticationFailed('Unable to find appropriate key.')

    def authenticate_header(self, request):
        return 'Bearer'

def get_token_auth_header(request):
    """Obtains the Access Token from the Authorization Header
    """
    auth = request.META.get("HTTP_AUTHORIZATION", None)
    parts = auth.split()
    token = parts[1]

    return token

def requires_scope(required_scope):
    """Determines if the required scope is present in the Access Token
    Args:
        required_scope (str): The scope required to access the resource
    """
    def require_scope(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            token = get_token_auth_header(args[0])
            decoded = jwt.decode(token, verify=False)
            if decoded.get("scope"):
                token_scopes = decoded["scope"].split()
                for token_scope in token_scopes:
                    if token_scope == required_scope:
                        return f(*args, **kwargs)
            response = JsonResponse({'message': 'You don\'t have access to this resource'})
            response.status_code = 403
            return response
        return decorated
    return require_scope

def jwt_get_username_from_payload_handler(payload):
    username = payload.get('sub').replace('|', '.')
    authenticate(remote_user=username)
    return username

def jwt_decode_token(token):
    header = jwt.get_unverified_header(token)
    AUTH0_DOMAIN=os.getenv('AUTH0_DOMAIN')
    jwks = requests.get(f'https://{AUTH0_DOMAIN}/.well-known/jwks.json').json()
    public_key = None
    for jwk in jwks['keys']:
        if jwk['kid'] == header['kid']:
            public_key = jwt.algorithms.RSAAlgorithm.from_jwk(json.dumps(jwk))

    if public_key is None:
        raise ValueError('Public key not found.')

    issuer = f'https://{AUTH0_DOMAIN}/'
    return jwt.decode(token, public_key, audience='http://localhost:8000/', issuer=issuer, algorithms=['RS256'])
