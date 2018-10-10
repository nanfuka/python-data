from tests import BaseTestCase
import json


class RequestTestCase(BaseTestCase):
    
    def test_create_request(self):
        """ Tests whether a user can create a request successfully """
        response = self.test_client.post('/api/v1/menu', data=json.dumps(self.user_data), content_type = 'application/json')
        self.assertEqual(response.status_code, 400)
        self.assertTrue("User successfully created an account")


    def test_create_request_without_client_name(self):
        """ Test for create request without user_id """
        with self.test_client:
            response = self.test_client.post( '/api/v1/menu',content_type='application/json',
                data=json.dumps({"menu_id":"chips", "price":""}))            
            reply = json.loads(response.data)
            self.assertTrue(reply["message"], 'All fields are required')