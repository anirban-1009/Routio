import base64
import os

from Crypto.Cipher import AES
from django.urls.resolvers import ImproperlyConfigured
from dotenv.main import load_dotenv
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import status
from rest_framework.viewsets import GenericViewSet

from Crypto.Util.Padding import unpad

from backend.settings import AUDIENCE, BASE_DIR, CLIENT_ID, CLIENT_SECRET

env_path = os.path.join(str(BASE_DIR), ".env")
load_dotenv(dotenv_path=env_path)

class TokenViewset(GenericViewSet):
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
            # Allow public access only to the create method
            if self.action == 'create':
                return [AllowAny()]
            return super().get_permissions()

    def create(self, request):

        try:
            received_token = self.decrypt_secret(request.data['key'])
            if (received_token == CLIENT_ID):
                import requests

                # Define the URL and the necessary data
                url = 'https://dev-v8l73w5o4qropczv.us.auth0.com/oauth/token'

                # Prepare the request payload (data)
                data = {
                    'grant_type': 'client_credentials',
                    'client_id': CLIENT_ID,
                    'client_secret': CLIENT_SECRET,
                    'audience': AUDIENCE,
                }

                # Send the POST request
                response = requests.post(url, data=data, headers={'Content-Type': 'application/x-www-form-urlencoded'})

                # Check the response
                if response.status_code == 200:
                    return Response(response.json(), status=status.HTTP_200_OK)
                else:
                    return Response({"error message": response.json(), "displaymessage": "Please contact the administrator"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        except Exception as e:
            print(e)
            return Response({"message": e.__str__(), "displaymessage": "Invalid Access"}, status=status.HTTP_403_FORBIDDEN)

    def decrypt_secret(self, encrypted_text):
        SECRET_KEY =os.getenv('DECRYPT_SECRET_KEY')
        try:
            enc=base64.b64decode(encrypted_text)
            if SECRET_KEY:
                cipher = AES.new(SECRET_KEY.encode('utf-8'), AES.MODE_ECB)
                return unpad(cipher.decrypt(enc),16).decode("utf-8", "ignore")
            else:
                raise ImproperlyConfigured("The environment variable SECRET_KEY is not set.")
        except Exception as e:
            raise ValueError(f"Decryption failed: {str(e)}")
