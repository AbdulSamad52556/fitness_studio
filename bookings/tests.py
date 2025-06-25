from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from classes.models import FitnessClass

class BookingTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.class1 = FitnessClass.objects.create(
            name='YOGA',
            datetime='2023-12-25T09:00:00Z',
            instructor='Instructor',
            max_slots=10,
            available_slots=10
        )
    
    def test_create_booking(self):
        url = reverse('create-booking')
        data = {
            'fitness_class': self.class1.id,
            'client_name': 'Test User',
            'client_email': 'test@example.com'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.class1.refresh_from_db()
        self.assertEqual(self.class1.available_slots, 9)