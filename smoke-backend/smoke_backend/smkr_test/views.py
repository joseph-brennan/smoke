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

def fetch_json(self,url):
    response = requests.get(url)
    return response.json()

blueprint = Blueprint('JSON', __name__, url_prefix='/JSON')
@blueprint.route('/test', methods=['POST'])
def stringify_json():
    data = request.get_json()
    string = json.dumps(data)
    os.putenv(join(string))
    process = subprocess.Popen(run_smkr.sh, shell=True, stdout=subprocess.PIPE)
    process.wait()
    print (process.returncode)
    #value = subprocess.check_output(['run_smkr.sh', echo])
    return string

