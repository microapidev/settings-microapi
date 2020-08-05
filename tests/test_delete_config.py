from tests import TestCase, main
from tests import BASE_URL, TEST_INSTANCE_NUMBER
from tests import requests, randint, json


class Test_For_Delete_Config_Endpoint(TestCase):
    def setUp(self):
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
        response = requests.post(BASE_URL + '/config/new',
                                 headers={'Content-Type': 'application/json'}, data=json.dumps(data))

    def test_delete_config_with_invalid_entry_response(self):
        # Ensures invalid id means 404 error
        user_id = '889'
        api_name = 'gad'
        response = requests.delete(BASE_URL + '/config/delete/'+user_id+'/'+api_name)
        res = response.json()
        self.assertEqual(response.status_code, 404)
        self.assertEqual(res['message'], "Config for {} not found".format(api_name))

    def test_delete_config_response(self):
        # Ensures valid input means 201
        user_id = '1'
        api_name = 'email-microapi'
        response = requests.delete(BASE_URL + '/config/delete/'+user_id+'/'+api_name)
        res = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['message'], "Config for '{}' successfully deleted".format(api_name))


if __name__ == '__main__':
    main()

