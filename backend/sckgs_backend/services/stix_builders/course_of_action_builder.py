from stix_builder import StixBuilder
from stix2 import CourseOfAction
import faker
import json

class CourseOfActionBuilder(StixBuilder):
    def __int__(self, data):
        self.name = data.get(data['name'])
        self.description = data.get(data['description'])
        self.action = data.get(data['action'])

    def create(self):
        if self.name is not None:
            return CourseOfAction(name=self.name)
