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


class TestList(TestCase):

    def setUp(self):
        self.access_token = os.getenv('AUTH0_ACCESS_TOKEN')
        if not self.access_token:
            raise ValueError("AUTH0_ACCESS_TOKEN is not set in environment variables")
        
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

    @pytest.mark.django_db
    def test_centers_list_empty(self):

        url = reverse('centers-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK, "Invalid status code")
        self.assertEqual(len(response.data), 0, "Invalid response size")

    @pytest.mark.django_db
    def test_centers_list_non_empty(self):
        center = baker.make(
            Center,
            lat=17.51299,
            long=78.46053
        )
        url = reverse('centers-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK, "Invalid status code")
        self.assertEqual(response.data[0]['lat'], center.lat, 'Invalid responsse message')

    @pytest.mark.django_db
    def test_centers_create_valid(self):
        payload = {
            "lat": 17.51299,
            "long": 78.46053
        }
        url = reverse('centers-list')
        response = self.client.post(url, payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, "Invalid status code")
        self.assertEqual(response.data['lat'], payload['lat'], 'Invalid response message')

    @pytest.mark.django_db
    def test_centers_create_duplicate(self):
        self.test_centers_create_valid()
        payload = {
            "lat": 17.51299,
            "long": 78.46053
        }
        url = reverse('centers-list')
        response = self.client.post(url, payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, "Invalid status Code")
    
    def test_centers_create_invalid(self):
        payload = {
            "driver": "test_driver"
        }
        url = reverse('centers-list')
        response = self.client.post(url, payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, "Invalid status code")