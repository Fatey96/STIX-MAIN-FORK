from .stix_builder import StixBuilder
from stix2 import Incident
import faker
import json

class IncidentBuilder(StixBuilder):
    def __init__(self, data):
        self.name = data.get('name')
        self.description = data.get('description')

    def create(self):
        print(self.name)
        if self.name is not None:
            return Incident(name=self.name)