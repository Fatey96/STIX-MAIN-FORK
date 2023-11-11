from stix_builder import StixBuilder
from stix2 import Tool
import faker
import json

class ToolBuilder(StixBuilder):
    def __init__(self, data):
        self.name = data.get(data['name'])
        self.description = data.get(data['description'])
        self.tool_types = data.get(data['tool_types'])
        self.aliases = data.get(data['aliases'])
        self.kill_chain_phases = data.get(data['kill_chain_phases'])
        self.tool_version = data.get(data['tool_version'])

    def create(self):
        pass