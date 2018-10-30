import requests
import subprocess
import unittest
import json


def test_stringify(client):

    data = {'Bryan': 'Blageolle',
            'Joe': 'Shmo',
            'John': 'Doe',
            }

    resp = client.post(
        '/api/v1/test',
        data=json.dumps(data),
        headers={'content-type': 'application/json'}
      )

    assert resp.status_code == 200
