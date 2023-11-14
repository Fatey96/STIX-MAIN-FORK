from .stix_builder import StixBuilder
from stix2 import Campaign
import faker
import json

class CampaignBuilder(StixBuilder):
    def __init__(self, data):
        self.name = data.get('name')
        self.description = data.get('description')
        self.aliases = data.get('aliases')
        self.first_seen = data.get('first_seen')
        self.last_seen = data.get('last_seen')
        self.objective = data.get('objective')

    def create(self):
        if self.name is not None:
            return Campaign(name=self.name)