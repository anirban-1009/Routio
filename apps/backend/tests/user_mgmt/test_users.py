from model_bakery import baker
from rest_framework.test import APIClient
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
import os
from user_mgmt.models import UserModel
from driver_mgmt.models import Driver
from center_mgmt.models import Center
import pytest



class UsersList(TestCase):

    """
    Tests for the Users List API endpoint.

    This class tests the following functionalities:
    - Retrieving the list of users.
    - Ensuring the list is non-empty after creating a user.
    - Creating a new user.
    - Handling duplicate user creation.

    Setup:
        - Authenticates API requests using an Auth0 bearer token from environment variables.
        - Creates a test user in the database.

    Methods:
        test_users_list_get(): Verify the users list endpoint returns a 200 OK status.
        test_users_list_get_non_empty(): Check that the users list contains at least one user.
        test_users_create(): Test the creation of a new user.
        test_users_create_duplicate(): Ensure duplicate user creation results in a 400 Bad Request.
    """

    def setUp(self):
        self.access_token = os.getenv('AUTH0_ACCESS_TOKEN')
        if not self.access_token:
            raise ValueError("AUTH0_ACCESS_TOKEN is not set in environment variables")
        
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        self.user = baker.make(
            UserModel,
            email='test_user@mail.com'
        )
        self.user.save()

    @pytest.mark.django_db
    def test_users_list_get(self):
        url = reverse('users-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    @pytest.mark.django_db
    def test_users_list_get_non_empty(self):
        url = reverse('users-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)
    
    @pytest.mark.djano_db
    def test_users_create(self):
        url = reverse('users-list')
        payload = {
            "name": "test_user",
            "email": "test+user1@email.com"
        }
        response = self.client.post(url, payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    @pytest.mark.django_db
    def test_users_create_duplicate(self):
        self.test_users_create()
        url = reverse('users-list')
        payload = {
            "name": "test_user",
            "email": "test+user1@email.com"
        }
        response = self.client.post(url, payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class UsersDetail(TestCase):

    """
        Unit tests for the Users Detail API endpoint.

        This class tests the following functionalities:
        - Retrieving a valid user by ID.
        - Handling retrieval of an invalid user ID.
        - Updating a user's details with valid data.
        - Handling errors when required fields are missing during update.
        - Partially updating a user's details using PATCH.
        - Ensuring invalid data during partial update returns the appropriate error.

        The tests use an Auth0 access token for authentication, and the API client is authenticated using this token.
    """

    def setUp(self):
        self.access_token = os.getenv('AUTH0_ACCESS_TOKEN')
        if not self.access_token:
            raise ValueError("AUTH0_ACCESS_TOKEN is not set in environment variables")
        
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        self.user = baker.make(
            UserModel,
            email='test_user@mail.com'
        )

    @pytest.mark.django_db
    def test_user_retrieve_valid(self):
        url = reverse('users-detail', kwargs={'pk': self.user.user_id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK, 'Invalid Status Code')
        self.assertEqual(response.data['email'], self.user.email, 'Invalid Response Message')
    
    @pytest.mark.django_db
    def test_user_retrieve_invalid(self):
        url = reverse('users-detail', kwargs={'pk': 2983})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND, 'Invalid Status Code')
        self.assertEqual(
            response.data['detail'],
            'No UserModel matches the given query.',
            'Invalid response message'
        )

    @pytest.mark.django_db
    def test_user_update_valid(self):
        url = reverse('users-detail', kwargs={'pk': self.user.user_id})
        payload = {
            "email": self.user.email,
            "address": "Hyderabad"
        }
        response = self.client.put(url, payload)

        self.assertEqual(response.status_code, status.HTTP_200_OK, 'Invalid Status Code')
        self.assertEqual(response.data['address'], "Hyderabad", 'Invalid Response message')

    @pytest.mark.django_db
    def test_user_update_invalid(self):
        url = reverse('users-detail', kwargs={'pk': self.user.user_id})
        payload = {
            "address": "Hyderabad"
        }
        response = self.client.put(url, payload)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, 'Invalid Response Message')
        self.assertEqual(response.data['email'][0], 'This field is required.', 'Invalid Response message')

    @pytest.mark.django_db
    def test_user_update_patch_valid(self):
        url = reverse('users-detail', kwargs={'pk': self.user.user_id})
        payload = {
            "name": "test_user"
        }
        response = self.client.patch(url, payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK, 'Invalid Status Code')
        self.assertEqual(response.data['name'], "test_user", 'Invalid Response Message')

    @pytest.mark.django_db
    def test_user_update_patch_invalid(self):
        url = reverse('users-detail', kwargs={'pk': self.user.user_id})
        payload = {
            "center": "test_user"
        }
        response = self.client.patch(url, payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, 'Invalid Status Code')
        self.assertEqual(
            response.data['center'][0],
            'Invalid pk "test_user" - object does not exist.',
            'Invalid Response Message'
        )

    @pytest.mark.django_db
    def test_user_delete_valid(self):
        url = reverse('users-detail', kwargs={'pk': self.user.user_id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT, 'Invalid Status Code')
        self.assertEqual(response.data, None, 'Invalid Response Message')
    
    @pytest.mark.django_db
    def test_user_delete_invalid(self):
        url = reverse('users-detail', kwargs={'pk': '98337A'})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND, 'Invalid  Status Code')
        self.assertEqual(
            response.data['detail'],
            'No UserModel matches the given query.',
            'Invalid Response Message'
        )

class UserDriver(TestCase):

    """
    Unit tests to test the `users/<pk>/driver/` endpoint with GET method for valid and invalid requests.
    """

    def setUp(self):
        self.access_token = os.getenv('AUTH0_ACCESS_TOKEN')
        if not self.access_token:
            raise ValueError("AUTH0_ACCESS_TOKEN is not set in environment variables")
        
        self.setupUser()
        
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

    def setupUser(self):

        self.user = baker.make(
            UserModel,
            email='test_user@mail.com'
        )

        self.driver = baker.make(
            Driver,
            name='JohnDoe',
            email='test_driver@mail.com',
            registration_id='AIUEOIU',
            lat=17.51299,
            long=78.46053,
        )

        self.center = baker.make(
            Center,
            lat=17.51299,
            long=78.46053,
            driver=self.driver
        )

        self.user.center = self.center
        self.user.save()

    @pytest.mark.django_db
    def test_user_driver_valid(self):

        url = reverse('users-driver', kwargs={'pk': self.user.user_id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK, 'Invalid status code')
        self.assertEqual(
            response.data['driver']['driver_id'],
            self.driver.driver_id,
            'Invalid response message'
        )

    @pytest.mark.django_db
    def test_user_driver_valid_empty(self):
        self.driver.delete()
        self.driver.save()

        url = reverse('users-driver', kwargs={'pk': self.user.user_id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND, 'Invalid status code')
        self.assertEqual(response.data['detail'], "No UserModel matches the given query.", 'Invalid Response Data')

class UserGreenImpact(TestCase):

    """
    Unittests for the `users/<pk>/green-impact/` endpoint for GET requests for valid and invalid requests
    """

    def setupUser(self):
        self.user = baker.make(
            UserModel,
            email='test_user@mail.com'
        )

        self.driver = baker.make(
            Driver,
            name='JohnDoe',
            email='test_driver@mail.com',
            registration_id='AIUEOIU',
            lat=17.51299,
            long=78.46053,
        )

        self.center = baker.make(
            Center,
            lat=17.51299,
            long=78.46053,
            driver=self.driver
        )

        self.user.center = self.center
        self.user.save()

    def setUp(self):
        self.access_token = os.getenv('AUTH0_ACCESS_TOKEN')
        if not self.access_token:
            raise ValueError("AUTH0_ACCESS_TOKEN is not set in environment variables")

        self.setupUser()

        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

    @pytest.mark.django_db
    def test_user_green_impact_valid(self):

        url = reverse('users-green-impact', kwargs={'pk': self.user.user_id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK, 'Invalid status code')
        self.assertEqual(
            response.data['driver']['driver_id'],
            self.driver.driver_id,
            'Invalid response message'
        )

    @pytest.mark.django_db
    def test_user_green_impact_invalid(self):
        self.driver.delete()
        self.driver.save()

        url = reverse('users-green-impact', kwargs={'pk': self.user.user_id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND, 'Invalid status code')
        self.assertEqual(response.data['detail'], "No UserModel matches the given query.", 'Invalid Response Data')

