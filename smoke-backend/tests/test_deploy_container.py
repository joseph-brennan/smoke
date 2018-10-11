from smoke_backend.api.v1.test.views import stringify_json
import requests
import subprocess
import unittest
import json


def test_stringify(client):

    data = {'Bryan': 'Blageolle'}

    rep = client.post(
        '/api/v1/test',
        data=json.dumps(data),
        headers={'content-type': 'application/json'}
      )

    assert json.loads(stringify_json()) == data
