from stix_builder import StixBuilder
from stix2 import Indicator
import faker
import json

class IndicatorBuilder(StixBuilder):
    def __init__(self, data):
        self.name = data.get(data['name'])
        self.description = data.get(data['description'])
        self.indicator_types = data.get(data['indicator_types'])
        self.pattern = data.get(data['pattern'])
        self.pattern_type = data.get(data['pattern_types'])
        self.pattern_version = data.get(data['pattern_version'])
        self.valid_from = data.get(data['valid_from'])
        self.valid_until = data.get(data['valid_until'])
        self.kill_chain_phases = data.get(data['kill_chain_phases'])

    def create(self):
        pass
