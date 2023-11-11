from stix_builder import StixBuilder
from stix2 import Grouping
import faker
import json

class GroupingBuilder(StixBuilder):
    def __init__(self, data):
        self.name = data.get(data['name'])
        self.description = data.get(data['description'])
        self.context = data.get(data['context'])
        self.object_refs = data.get(data['object_refs'])

    def create(self):
        pass