import random
from unittest import TestCase
import requests
import json
from flask import jsonify

class Test_For_Get_Single_Config_Endpoint(TestCase):
    #FIX THE GET SINGLE CONFIG RESPONSE CODE FOR 500 ERROR
    def test_get_single_config_with_invalid_entry_response(self):
        # Ensures invalid id means 404 error
        user_id = '889'
        api_name = 'gad'
        response = requests.get('https://settings.microapi.dev/v1/config/'+user_id+'/'+api_name)
        print(response)
        res = response.json()
        self.assertEqual(response.status_code, 404)
        self.assertEqual(res['message'], f'Config for {api_name} not found')

    def test_get_single_config_response(self):
        # Ensures valid input means 200
        user_id = '1'
        api_name = 'email-microapi'
        response = requests.get('https://settings.microapi.dev/v1/config/'+user_id+'/'+api_name)
        res = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['message'],  f"Config for {api_name}")

if __name__ == '__main__':
    unittest.main()

