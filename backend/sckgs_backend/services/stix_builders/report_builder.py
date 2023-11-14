from .stix_builder import StixBuilder
from stix2 import Report
import faker
import json

class ReportBuilder(StixBuilder):
    def __init__(self, data):
        self.name = data.get('name')
        self.description = data.get('description')
        self.report_type = data.get('report_type')
        self.published = data.get('published')
        self.object_refs = data.get('object_refs')

    def create(self):
        pass
