from .stix_builder import StixBuilder
from stix2 import ObservedData
import faker
import json

class ObservedDataBuilder(StixBuilder):
    def __init__(self, data):
        self.first_observed = data.get('first_observed')
        self.last_observed = data.get('last_observed')
        self.number_observed = data.get('number_observed')
        self.objects = data.get('objects')
        self.object_refs = data.get('object_refs')

    def create(self):
        pass