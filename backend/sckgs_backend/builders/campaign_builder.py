from .stix_builder import StixBuilder
from stix2 import Campaign
import faker
import json

class CampaignBuilder(StixBuilder):

    counter = 0
    faker_instance = faker.Faker()

    def __init__(self, name=None):
        self.name = name

    @classmethod
    def _generate_identity_name(cls):
        """
        Generate a name in the format 'Identity X', 
        where X is a counter that increments with each call.

        Returns:
            str: Generated identity name.
        """
        cls.counter += 1
        return f"Identity {cls.counter}"

    @classmethod
    def generate_random_name(cls):
        """
        Generate a random name using the faker library.

        Returns:
            str: Randomly generated name.
        """
        return cls.faker_instance.name()

    def create(self, data=None):
        """
        Create a STIX identity object based on the provided data. 
        If no data is provided, use the instance's name attribute, 
        if that is also None, generate a name.

        Parameters:
            data (str or dict, optional): A JSON string or dictionary containing identity details.

        Returns:
            Identity: A STIX identity object.
        """
        if isinstance(data, str):
            data = json.loads(data)
        
        if data and 'name' in data:
            name = data['name']
        elif self.name:
            name = self.name
        else:
            name = self._generate_identity_name()

        campaign = Campaign(name=name)
        return campaign