from django.test import TestCase
from django.urls import reverse
import json

class TestRequest(TestCase):
    def test_json_data(self):
        json_data = {
            "dataset": 1,
            "objects": [
                {
                    "type": "identity",
                    "name": "John Doe",
                    "identity_class": "individual",
                    "options": []
                },
                {
                    "type": "threat-actor",
                    "name": "Evil Incorporated"
                },
                {
                    "type": "malware",
                    "name": "stuxnet"
                }
            ],
            "relationships": [
                {
                    "source": 1,
                    "target": 0,
                    "relationship": "attributed-to"
                },
                {
                    "source": 1,
                    "target": 2,
                    "relationship": "uses"
                }
            ]
        }

        response = self.client.post(reverse('add_stix_data'), json.dumps(json_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
