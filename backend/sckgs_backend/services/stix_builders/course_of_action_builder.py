from .stix_builder import StixBuilder
from stix2 import CourseOfAction
import faker
import json

class CourseOfActionBuilder(StixBuilder):
    def __int__(self, data):
        self.name = data.get('name')
        self.description = data.get('description')
        self.action = data.get('action')

    def create(self):
        if self.name is not None:
            return CourseOfAction(name=self.name)
