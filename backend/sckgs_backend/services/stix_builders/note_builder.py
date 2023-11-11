from stix_builder import StixBuilder
from stix2 import Note
import faker
import json

class NoteBuilder(StixBuilder):
    def __init__(self, data):
        self.abstract = data.get(data['abstract'])
        self.content = data.get(data['content'])
        self.authors = data.get(data['authors'])
        self.object_refs = data.get(data['object_refs'])

    def create(self):
        pass