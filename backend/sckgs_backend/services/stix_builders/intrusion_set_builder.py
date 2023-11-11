from stix_builder import StixBuilder
from stix2 import IntrusionSet
import faker
import json

class IntrusionSetBuilder(StixBuilder):
    def __init__(self, data):
        self.name = data.get(data['name'])
        self.description = data.get(data['description'])
        self.aliases = data.get(data['aliases'])
        self.first_seen = data.get(data['first_seen'])
        self.last_seen = data.get(data['last_seen'])
        self.goals = data.get(data['goals'])
        self.resource_level = data.get(data['resource_level'])
        self.primary_motivation = data.get(data['primary_motivation'])
        self.secondary_motivations = data.get(data['secondary_motivations'])

    def create(self):
        pass