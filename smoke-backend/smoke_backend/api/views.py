# -*- coding: utf-8 -*-
"""Setting up API routes

Uses a Flask blueprint to control the function of the various libraries used
by smoke. [f]_ [fblueprint]_

Attributes:
    blueprint (Flask Blueprint): The blueprint for the smoke api.
        [fblueprint]_ [frestful]_

    api (Flask-RESTful): An extension for Flask to build RESTful APIs through
        ORM libraries. [frestful]_
"""

from flask import request, jsonify,  Blueprint
from flask_restful import Api
import requests
import docker
import json
from smoke_backend.api.resources import UserResource, UserList


blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(blueprint)

@blueprint.route('/test', methods=['GET'])
def stringify_json():
    data = request.get_json()  # __name__ = JSON object, data = __name__

    variable = json.dumps(data)  # string = stringified JSON object

    client = docker.from_env()
    # print (client.containers.run("alpine", ["echo", "hello world"]))

    # client.images.build(path='.', tag="alpine:test")

    result = client.containers.run("alpine:latest", ["printenv", "STRING"], auto_remove=True, environment=["STRING={}".format(variable)])

    return result

api.add_resource(UserResource, '/users/<int:user_id>')
api.add_resource(UserList, '/users')
