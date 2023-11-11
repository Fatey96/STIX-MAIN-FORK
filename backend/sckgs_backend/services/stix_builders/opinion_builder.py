from stix_builder import StixBuilder
from stix2 import Opinion
import faker
import json

class OpinionBuilder(StixBuilder):
    def __init__(self, data):
        self.explanation = data.get(data['explanation'])
        self.authors = data.get(data['authors'])
        self.opinion = data.get(data['opinion'])
        self.object_refs = data.get(data['object_refs'])

    def create(self):
        pass