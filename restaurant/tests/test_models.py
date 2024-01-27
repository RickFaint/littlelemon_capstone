
import django
from django.db.models.functions import Now
from django.test import TestCase
from restaurant.models import Menu
from restaurant.models import Booking


class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80,inventory=100)
        itemstr = item.__str__()
        print("running menu model test")
        self.assertEqual(itemstr, "IceCream80")

class BookingTest(TestCase):
    def test_get_item(self):
        item = Booking.objects.create(name="bob", number_of_guests=80,booking_datetime=Now())
        itemstr = item.__str__()
        print("running booking model test")
        self.assertEqual(itemstr, "bob - 80")
