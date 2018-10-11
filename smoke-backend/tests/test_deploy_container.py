<<<<<<< HEAD
from smoke_backend.api.v1.test.views import stringify_json
=======
from smoke_backend.api.v1.test import stringify_json
>>>>>>> 1df1446f12328a1b33c5c097d8337d9bbbfe8bad
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
