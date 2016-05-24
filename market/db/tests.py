from django.test import TestCase
from .models import Venues, Organizers

class VenueTestCase(TestCase):

    def setUp(self):
        Venues.objects.create(name="Civic Center", location="San Francisco", capacity="23434")

    def test_valid_venue(self):
        venue = Venues.objects.get(name='Civic Center')
        self.assertEqual(venue.name, 'Civic Center')
        self.assertEqual(venue.location, 'San Francisco')
        self.assertEqual(venue.capacity, 23434)

