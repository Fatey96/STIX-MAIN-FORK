from .stix_builder import StixBuilder
from stix2 import Location
import faker
import json

class LocationBuilder(StixBuilder):
    def __init__(self, data):
        self.name = data.get('name')
        self.description = data.get('description')
        self.latitude = data.get('latitude')
        self.longitude = data.get('longitude')
        self.percision = data.get('percision')
        self.region = data.get('region')
        self.country = data.get('country')
        self.administrative = data.get('administrative')
        self.city = data.get('city')
        self.street_address = data.get('street_address')
        self.postal_code = data.get('postal_code')

    def create(self):
        # At least one of the following properties must be provided:
        # country, region or both latitude and longitude.
        if self.region is not None:
            return Location(region=self.region)
        elif self.country is not None:
            return Location(country=self.country)
        elif self.latitude and self.longitude is not None:
            return Location(latitude=self.latitude, longitude=self.longitude)