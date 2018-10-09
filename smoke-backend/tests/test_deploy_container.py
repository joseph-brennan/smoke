from smoke_backend.smkr_test.views import stringify_json
import requests
import subprocess
import unittest
import json
def mocked_requests_get(*args,**kwargs):
        class MockResponse:
            def __init__(self, json_data, status_code):
                self.json_data = json_data
                self.status_code = status_code
                self.json_string = json.dumps(json_data)

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
     def test_stringify(self, mock_get):
        rep = client.post(
              '/JSON/test',
              data=json.dumps({'Bryan': 'Blageolle'}),
              headers={'content-type': 'application/json'}
              )
        
        assert rep.status_code == 400
        assert rep.stringify_json()['msg'] == {'Bryan': 'Blageolle'}
        

if __name__ == '__main__':
    unittest.main()
