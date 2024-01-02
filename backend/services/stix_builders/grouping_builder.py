from .stix_builder import StixBuilder
from stix2 import Grouping
import faker
import json

class GroupingBuilder(StixBuilder):
    def __init__(self, data):
        self.name = data.get('name')
        self.description = data.get('description')
        self.context = data.get('context')
        self.object_refs = data.get('object_refs')

    def create(self):
        return Grouping(object_refs=self.object_refs)
            