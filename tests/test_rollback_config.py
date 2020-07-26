import random
from unittest import TestCase
import requests
import json
from flask import jsonify

test_instance_number = random.randint(0, 200000)
class Test_For_Rollback_Config_Endpoint(TestCase):

    def setUp(self):
        data = {
            "api_name": "email-microapi",
            "current_config": {
            "key_1": "value_1",
            "key_2": "value_2"
            },
            "user_id": test_instance_number
        }
        response = requests.post('https://settings.microapi.dev/v1/config/new',
                                 headers={'Content-Type': 'application/json'}, data=json.dumps(data))

    def test_rollback_config_with_invalid_entry_response(self):
        # Ensures invalid id means 404 error
        user_id = '889'
        api_name = 'gad'
        response = requests.get('https://settings.microapi.dev/v1/config/rollback/'+user_id+'/'+api_name)
        res = response.json()
        self.assertEqual(response.status_code, 404)
        self.assertEqual(res['message'], "No configuration found for {} API".format(api_name))

    def test_rolback_config_response(self):
        # Ensures valid input means 200
        user_id = '1'
        api_name = 'email-microapi'
        response = requests.get('https://settings.microapi.dev/v1/config/rollback/'+user_id+'/'+api_name)
        res = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['message'],  "Config rollback Success")


    def test_rolback_no_default_config_response(self):
        # Ensures no default config input means 400
        user_id = str(test_instance_number)
        api_name = 'email-microapi'
        response = requests.get('https://settings.microapi.dev/v1/config/rollback/'+user_id+'/'+api_name)
        res = response.json()
        self.assertEqual(response.status_code, 400)
        self.assertEqual(res['message'], "No previous or default config to rollback")

if __name__ == '__main__':
    unittest.main()

