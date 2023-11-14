from .stix_builder import StixBuilder
from stix2 import Note
import faker
import json

class NoteBuilder(StixBuilder):
    def __init__(self, data):
        self.abstract = data.get('abstract')
        self.content = data.get('content')
        self.authors = data.get('authors')
        self.object_refs = data.get('object_refs')

    def create(self):
        pass