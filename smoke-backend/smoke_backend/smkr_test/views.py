# -*- coding: utf-8 -*-
"""Creates view for JSON handling.

Attributes:
    blueprint (Flask Blueprint): The blueprint scheme for smoke. [fblueprint]_
"""
from flask import request, jsonify, Blueprint
import requests
import docker
import json


blueprint = Blueprint('api', __name__, url_prefix='api/v1')
@blueprint.route('/test', methods=['GET'])
def stringify_json():
    data = request.get_json()  ##__name__ = JSON object, data = __name__
    variable = json.dumps(data)  ##string = stringified JSON object
    client = docker.from_env()
    print (client.containers.run("alpine", ["echo", "hello world"]))

    # We will need to be able to wait for docker container to finish being run
    # and complete then pass back respnce as a JSON object 
    return jsonify(variable)

