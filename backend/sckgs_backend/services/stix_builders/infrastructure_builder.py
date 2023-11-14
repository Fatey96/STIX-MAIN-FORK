from .stix_builder import StixBuilder
from stix2 import Infrastructure
import faker
import json

class InfrastructureBuilder(StixBuilder):
    def __init__(self, data):
        self.name = data.get('name')
        self.description = data.get('description')
        self.infrastructure_types = data.get('infrastructure_type')
        self.aliases = data.get('aliases')
        self.kill_chain_phases = data.get('kill_chain_phases')
        self.first_seen = data.get('first_seen')
        self.last_seen = data.get('last_seen')

    def create(self):
        pass