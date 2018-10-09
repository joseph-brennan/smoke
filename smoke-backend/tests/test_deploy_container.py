#import factory
#from pytest_factoryboy import register
from smoke_backend.smkr_test import veiws
import requests
import unittest
import json

def mocked_requests_get(*args,**kwargs):
        class MockResponse:
            def __init__(self, json_data, status_code):
                self.json_data = json_data
                self.status_code = status_code
                self.json_string = json.dumps(json_data)

            #def json_string:
                

            def json(self):
                return self.json_data
       # mock the responses to each argument to be used in the test
        if args[0] == 'http://someurl.com/test.json':
            return MockResponse({"key1": "value1"}, 200)
        elif args[0] == 'http://someotherurl.com/anothertest.json':
            return MockResponse({"key2": "value2"},200)

        return MockResponse(None, 404)
    #TODO: mock the stringifyJSON method (get stringify info from Ron)

class JSONTesterTest(unittest.TestCase):

    # We patch 'requests.get' with our own method. The mock object is passed in to our test case method.
     @mock.patch('requests.get', side_effect=mocked_requests_get)
     def test_fetch(self, mock_get):
         #assert requests.get calls
         jt = JSONTester()
         #json_string = jt.stringify_json(jt.
         json_data = jt.fetch_json('http://someurl.com/test.json')        
         self.assertEqual(json_data, {"key1": "value1"})
         json_data = jt.fetch_json('http://someotherurl.com/anothertest.json')
         self.assertEqual(json_data, {"key2": "value2"})
         json_data = jt.fetch_json('http://nonexistenturl.com/cantfindme.json')
         self.assertIsNone(json_data)

         # assert that our mocked method was called with the right parameters
         self.assertIn(mock.call('http://someurl.com/test.json'), mock_get.call_args_list)
         self.assertIn(mock.call('http://someotherurl.com/anothertest.json'), mock_get.call_args_list)

         self.assertEqual(len(mock_get.call_args_list), 3)

if __name__ == '__main__':
    unittest.main()
