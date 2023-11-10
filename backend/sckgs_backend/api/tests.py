from django.test import TestCase
from django.urls import reverse
import json

class TestRequest(TestCase):
    def test_json_data(self):
        json_data = {
            "dataset": 100,
            "objects": [
                {
                    "type": "identity",
                    "name": "Bad Guys R Us",
                    "identity_class": "individual",
                    "options": []
                },
                {
                    "type": "identity",
                    "name": "AmbuCare Inc",
                    "options": []
                },
                {
                    "type": "threat-actor",
                    "name": "Buddy Noob"
                },
                {
                    "type": "malware",
                    "name": "stuxnet"
                },
                {
                    "type": "campaign",
                    "name": "Operation AttackEmergVehicles"
                },
                {
                    "type": "location",
                    "name": "Marilliv"
                },
                {
                    "type": "location",
                    "name": "Timeville"
                }
            ],
            "relationships": [
                {
                    "source": 2,
                    "target": 0,
                    "relationship": "attributed-to"
                },
                {
                    "source": 4,
                    "target": 0,
                    "relationship": "attributed-to"
                },
                {
                    "source": 4,
                    "target": 3,
                    "relationship": "uses"
                },
                 {
                    "source": 2,
                    "target": 3,
                    "relationship": "uses"
                },
                {
                    "source": 1,
                    "target": 5,
                    "relationship": "located-at"
                },
                {
                    "source": 2,
                    "target": 6,
                    "relationship": "located-at"
                },
                {
                    "source": 2,
                    "target": 1,
                    "relationship": "targets"
                },
                {
                    "source": 4,
                    "target": 1,
                    "relationship": "targets"
                }
            ]
        }

        response = self.client.post(reverse('add_stix_data'), json.dumps(json_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
