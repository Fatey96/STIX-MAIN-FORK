from django.test import TestCase
from django.urls import reverse
import json

class TestRequest(TestCase):
    def test_json_data(self):
        json_data = {
            "dataset": 30,
            "objects": [
                {
                    "type": "identity",
                    "name": "Bad Guys R Us"
                },
                {
                    "type": "identity",
                    "name": "AmbuCare Inc"
                },
                {
                    "type": "threat-actor",
                    "name": "Buddy Noob"
                },
                {
                    "type": "malware",
                    "is_family": "false"
                }
            ],
            "relationships": [
                {
                    "source": 2,
                    "target": 0,
                    "relationship": "attributed-to"
                },
                {
                    "source": 2,
                    "target": 1,
                    "relationship": "targets"
                },
                {
                    "source": 2,
                    "target": 3,
                    "relationship": "uses"
                }
            ]
        }

        response = self.client.post(reverse('add_stix_data'), json.dumps(json_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
