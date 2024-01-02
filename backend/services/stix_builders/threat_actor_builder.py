from .stix_builder import StixBuilder
from stix2 import ThreatActor
import faker
import json

class ThreatActorBuilder(StixBuilder):
    def __init__(self, data):
        self.name = data.get('name')

    def create(self):
        return ThreatActor(name=self.name)
