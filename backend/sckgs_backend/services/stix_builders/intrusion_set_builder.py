from .stix_builder import StixBuilder
from stix2 import IntrusionSet
import faker
import json

class IntrusionSetBuilder(StixBuilder):
    def __init__(self, data):
        self.name = data.get('name')
        self.description = data.get('description')
        self.aliases = data.get('aliases')
        self.first_seen = data.get('first_seen')
        self.last_seen = data.get('last_seen')
        self.goals = data.get('goals')
        self.resource_level = data.get('resource_level')
        self.primary_motivation = data.get('primary_motivation')
        self.secondary_motivations = data.get('secondary_motivations')

    def create(self):
        return IntrusionSet(name=self.name)
            