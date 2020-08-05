from tests import TestCase, main
from tests import BASE_URL, TEST_INSTANCE_NUMBER
from tests import requests, randint, json


class Test_For__Update_Config_Endpoint(TestCase):

    def test_Update_config_with_no_entry_response(self):

        # Ensures no body input means 400 error
        response = requests.patch(BASE_URL + '/config/update')
        self.assertEqual(response.status_code, 400)

    def test_Update_config_response(self):
        # Ensures valid input means 200
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
        response = requests.patch(BASE_URL + '/config/update',
                                 headers={'Content-Type': 'application/json'}, data=json.dumps(data))
        res = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['message'], 'Update Success')

    def test_Update_config_non_existing_response(self):
        # Ensures an non existing valid input means 404 error
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
            "user_id": 333333
        }
        response = requests.patch(BASE_URL + '/config/update',
                                 headers={'Content-Type': 'application/json'}, data=json.dumps(data))
        res = response.json()
        self.assertEqual(response.status_code, 404)

        self.assertEqual(res['message'], "Config for {} not found".format(data["api_name"]))


if __name__ == '__main__':
    main()

