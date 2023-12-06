from .stix_builder import StixBuilder
from stix2 import Incident
import faker
import json

class IncidentBuilder(StixBuilder):
    def __init__(self, data):
        self.name = data.get('name')
        self.description = data.get('description')

    def create(self):
        return Incident(name=self.name)
            