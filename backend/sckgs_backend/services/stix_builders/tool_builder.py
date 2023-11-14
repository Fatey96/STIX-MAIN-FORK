from .stix_builder import StixBuilder
from stix2 import Tool
import faker
import json

class ToolBuilder(StixBuilder):
    def __init__(self, data):
        self.name = data.get('name')
        self.description = data.get('description')
        self.tool_types = data.get('tool_types')
        self.aliases = data.get('aliases')
        self.kill_chain_phases = data.get('kill_chain_phases')
        self.tool_version = data.get('tool_version')

    def create(self):
        pass