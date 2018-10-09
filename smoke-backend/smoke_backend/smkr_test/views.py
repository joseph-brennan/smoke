# -*- coding: utf-8 -*-
"""Creates view for JSON handling.

Attributes:
    blueprint (Flask Blueprint): The blueprint scheme for smoke. [fblueprint]_
"""

from flask import request, jsonify, Blueprint
import requests
import subprocess
import unittest
import json
from unittest import mock

def fetch_json(self,url):
    response = requests.get(url)
    return response.json()

blueprint = Blueprint('JSON', __name__, url_prefix='/JSON')
@blueprint.route('/test', methods=['POST'])
def stringify_json(data):
    data = request.get_json()
    string = json.dumps(data)
    os.putenv(join(string))
    #stringify here or in script?
    subprocess.call(['./run_smkr.sh']) 
    #value = subprocess.check_output(['run_smkr.sh', echo])
    return string

