from stix_builder import StixBuilder
from stix2 import Report
import faker
import json

class ReportBuilder(StixBuilder):
    def __init__(self, data):
        self.name = data.get(data['name'])
        self.description = data.get(data['description'])
        self.report_type = data.get(data['report_type'])
        self.published = data.get(data['published'])
        self.object_refs = data.get(data['object_refs'])

    def create(self):
        pass
