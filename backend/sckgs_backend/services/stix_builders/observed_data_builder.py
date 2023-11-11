from stix_builder import StixBuilder
from stix2 import ObservedData
import faker
import json

class ObservedDataBuilder(StixBuilder):
    def __init__(self, data):
        self.first_observed = data.get(data['first_observed'])
        self.last_observed = data.get(data['last_observed'])
        self.number_observed = data.get(data['number_observed'])
        self.objects = data.get(data['objects'])
        self.object_refs = data.get(data['object_refs'])

    def create(self):
        pass