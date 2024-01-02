from .stix_builder import StixBuilder
from stix2 import Indicator
import faker
import json

class IndicatorBuilder(StixBuilder):
    def __init__(self, data):
        self.name = data.get('name')
        self.description = data.get('description')
        self.indicator_types = data.get('indicator_types')
        self.pattern = data.get('pattern')
        self.pattern_type = data.get('pattern_types')
        self.pattern_version = data.get('pattern_version')
        self.valid_from = data.get('valid_from')
        self.valid_until = data.get('valid_until')
        self.kill_chain_phases = data.get('kill_chain_phases')

    def create(self):
        return Indicator(pattern=self.pattern, pattern_type=self.pattern_type, valid_from=self.valid_from)
            
