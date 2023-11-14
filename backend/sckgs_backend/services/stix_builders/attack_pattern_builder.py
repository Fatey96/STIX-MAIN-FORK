from .stix_builder import StixBuilder
from stix2 import AttackPattern
import faker
import json

class AttackPatternBuilder(StixBuilder):
    def __init__(self, data):
        self.external_references = data.get('external_references')
        self.name = data.get('name')
        self.description = data.get('description')
        self.aliases = data.get('aliases')
        self.kill_chain_phases = data.get('kill_chain_phases')

    def create(self):
        if self.name is not None:
            return AttackPattern(name=self.name)