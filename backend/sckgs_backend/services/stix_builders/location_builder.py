from stix_builder import StixBuilder
from stix2 import Location
import faker
import json

class LocationBuilder(StixBuilder):
    def __init__(self, data):
        self.name = data.get(data['name'])
        self.description = data.get(data['description'])
        self.latitude = data.get(data['latitude'])
        self.longitude = data.get(data['longitude'])
        self.percision = data.get(data['percision'])
        self.region = data.get(data['region'])
        self.country = data.get(data['country'])
        self.administrative = data.get(data['administrative'])
        self.city = data.get(data['city'])
        self.street_address = data.get(data['street_address'])
        self.postal_code = data.get(data['postal_code'])

    def create(self):
        pass