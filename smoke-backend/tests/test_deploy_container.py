from smoke_backend.smkr_test.views import stringify_json
import requests
import subprocess
import unittest
import json


def test_stringify(client):
    rep = client.post(
        '/JSON/test',
        data=json.dumps({'Bryan': 'Blageolle'}),
        headers={'content-type': 'application/json'}
      )

    assert stringify_json() == '{"Bryan": "Blageolle"}'
