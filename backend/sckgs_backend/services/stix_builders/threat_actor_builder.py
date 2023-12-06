from .stix_builder import StixBuilder
from stix2 import ThreatActor
import faker
import json

class ThreatActorBuilder(StixBuilder):
    # For testing will delete later
    def __init__(self, data):
        self.name = data.get('name')

    def create(self):
        return ThreatActor(name=self.name)
             
    # counter = 0
    # faker_instance = faker.Faker()

    # def __init__(self, name=None):
    #     self.name = name

    # @classmethod
    # def _generate_threat_actor_name(cls):
    #     cls.counter += 1
    #     return f"Threat Actor {cls.counter}"

    # def create(self, data=None):
    #     if isinstance(data, str):
    #         data = json.loads(data)
        
    #     if data and 'name' in data:
    #         name = data['name']
    #     elif self.name:
    #         name = self.name
    #     else:
    #         name = self._generate_threat_actor_name()

    #     threat_actor = ThreatActor(name=name)
    #     return threat_actor

# actor_builder1 = ThreatActorBuilder("Custom Threat Actor")
# threat_actor_obj1 = actor_builder1.create()
# print(threat_actor_obj1)

# actor_builder2 = ThreatActorBuilder()
# threat_actor_obj2 = actor_builder2.create()
# print(threat_actor_obj2)