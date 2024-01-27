"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".
"""

from re import T
from turtle import title
import django
from django.test import TestCase
from restaurant.models import Menu
from restaurant.models import Booking
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from restaurant.serializers import MenuSerializer
from restaurant.serializers import BookingSerializer
from django.db.models.functions import Now



class ViewTest(TestCase):
    """Tests for the application views."""

    if django.VERSION[:2] >= (1, 7):
        # Django 1.7 requires an explicit setup() when running tests in PTVS
        @classmethod
        def setUpClass(cls):
            super(ViewTest, cls).setUpClass()
            django.setup()

    def test_home(self):
        """Tests the home page."""
        response = self.client.get('/restaurant/home/')
        print("running home test")
        self.assertContains(response, 'Home', 1, 200)

    def test_contact(self):
        """Tests the contact page."""
        response = self.client.get('/contact/')
        print("running contact test")
        self.assertContains(response, 'Contact', 3, 200)

    def test_about(self):
        """Tests the about page."""
        response = self.client.get('/about/')
        print("running about test")
        self.assertContains(response, 'About', 3, 200)
    
class MenuViewTest(TestCase):

    def setUp(self):
        # Add test instances of the Menu model
        menu1 = Menu.objects.create(title='Dog', price=10.99, inventory=100)
        menu1 = Menu.objects.create(title='Cat', price=11.99, inventory=110)
        menu1 = Menu.objects.create(title='horse', price=12.99, inventory=120)
 

    def test_getall(self):
        # Retrieve all Menu objects
     
        response = self.client.get("/restaurant/menu/")
        # Check if the response status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print("running menu view test")

        # Serialize the Menu objects
        serialized_data = MenuSerializer(Menu.objects.all(), many=True).data

        # Check if the serialized data equals the response data
        self.assertEqual(response.data, serialized_data)

class BookingViewTest(TestCase):


    def setUp(self):
        # Add test instances of the booking model
        booking1 = Booking.objects.create(name='Mike', number_of_guests=10, booking_datetime=Now())
        booking2 = Booking.objects.create(name='Matty', number_of_guests=18, booking_datetime=Now())
 

    def test_getall(self):
        # Create a user and obtain the token
        user = User.objects.create_user(username='super', password='user')
        token, created = Token.objects.get_or_create(user=user)
      

        # Include the token in the headers of the request
        headers = {'HTTP_AUTHORIZATION': f'Token {token.key}'}
        response = self.client.get("/restaurant/booking/booking/", **headers)

        # Check if the response status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print("running booking view test")

        # Serialize the booking objects
        serialized_data = BookingSerializer(Booking.objects.all(), many=True).data
       

        # Check if the serialized data equals the response data
        self.assertEqual(response.data, serialized_data)

