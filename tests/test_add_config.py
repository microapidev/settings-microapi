import random
from unittest import TestCase
import requests
import json
from flask import jsonify

test_instance_number = random.randint(0, 200000)
class Test_For_Add_Config_Endpoint(TestCase):

    def test_config_with_no_entry_response(self):

        # Ensures no body input means 400 error
        response = requests.post('https://settings.microapi.dev/v1/config/new')
        self.assertEqual(response.status_code, 400)

    def test_config_response(self):
        # Ensures valid input means 201
        data = {
            "api_name": "email-microapi",
            "current_config": {
            "key_1": "value_1",
            "key_2": "value_2"
            },
            "default_config": {
            "key_1": "value_1",
            "key_2": "value_2"
            },
            "user_id": test_instance_number
        }
        response = requests.post('https://settings.microapi.dev/v1/config/new',
                                 headers={'Content-Type': 'application/json'}, data=json.dumps(data))
        res = response.json()
        self.assertEqual(response.status_code, 201)
        self.assertEqual(res['message'], 'Create Success')

    def test_config_existing_response(self):
        # Ensures an already existing valid input means 403 error
        data = {
            "api_name": "email-microapi",
            "current_config": {
            "key_1": "value_1",
            "key_2": "value_2"
            },
            "default_config": {
            "key_1": "value_1",
            "key_2": "value_2"
            },
            "user_id": 1
        }
        response = requests.post('https://settings.microapi.dev/v1/config/new',
                                 headers={'Content-Type': 'application/json'}, data=json.dumps(data))
        res = response.json()
        self.assertEqual(response.status_code, 403)

        self.assertEqual(res['message'], 'Config already exists! Please update instead')

if __name__ == '__main__':
    unittest.main()

