from .stix_builder import StixBuilder
from stix2 import Identity
import faker
import json

class IdentityBuilder(StixBuilder):
    def __init__(self, data):
        self.name = data.get('name')

    def create(self):
        return Identity(name=self.name)
