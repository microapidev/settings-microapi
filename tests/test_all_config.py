from tests import TestCase, main
from tests import BASE_URL, TEST_INSTANCE_NUMBER
from tests import requests


class Test_For_Get_All_Config_Endpoint(TestCase):

    def test_get_config_with_invalid_entry_response(self):
        # Ensures invalid id means 404 error
        user_id = '889'
        response = requests.get(BASE_URL + '/config/'+user_id+'/all')
        res = response.json()
        self.assertEqual(response.status_code, 404)
        self.assertEqual(res['message'], 'Invalid Id')

    def test_get_config_response(self):
        # Ensures valid input means 201
        user_id = '1'
        response = requests.get(BASE_URL + '/config/'+user_id+'/all')
        res = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['message'], f"All configuration associated with user {user_id}")


if __name__ == '__main__':
    main()

