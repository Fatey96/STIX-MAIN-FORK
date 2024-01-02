from .stix_builder import StixBuilder
from stix2 import Opinion
import faker
import json

class OpinionBuilder(StixBuilder):
    def __init__(self, data):
        self.explanation = data.get('explanation')
        self.authors = data.get('authors')
        self.opinion = data.get('opinion')
        self.object_refs = data.get('object_refs')

    def create(self):
        return Opinion(opinion=self.opinion, object_refs=self.object_refs)
            