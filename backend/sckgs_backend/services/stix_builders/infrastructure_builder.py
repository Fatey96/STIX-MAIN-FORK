from stix_builder import StixBuilder
from stix2 import Infrastructure
import faker
import json

class InfrastructureBuilder(StixBuilder):
    def __init__(self, data):
        self.name = data.get(data['name'])
        self.description = data.get(data['description'])
        self.infrastructure_types = data.get(data['infrastructure_type'])
        self.aliases = data.get(data['aliases'])
        self.kill_chain_phases = data.get(data['kill_chain_phases'])
        self.first_seen = data.get(data['first_seen'])
        self.last_seen = data.get(data['last_seen'])

    def create(self):
        pass