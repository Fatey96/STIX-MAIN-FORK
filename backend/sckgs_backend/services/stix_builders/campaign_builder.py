from stix_builder import StixBuilder
from stix2 import Campaign
import faker
import json

class CampaignBuilder(StixBuilder):
    def __init__(self, data):
        self.name = data.get(data['name'])
        self.description = data.get(data['description'])
        self.aliases = data.get(data['aliases'])
        self.first_seen = data.get(data['first_seen'])
        self.last_seen = data.get(data['last_seen'])
        self.objective = data.get(data['objective'])

    def create(self):
        if self.name is not None:
            return Campaign(name=self.name)