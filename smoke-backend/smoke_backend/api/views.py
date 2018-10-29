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
from flask import Blueprint, jsonify, request
from flask_restful import Api
from flask_jwt_extended import jwt_required, get_jwt_identity
import docker
import json

from smoke_backend.api.resources import UserResource, UserList, UserSchema
from smoke_backend.models import User

blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(blueprint)


api.add_resource(UserResource, '/users/<int:user_id>')
api.add_resource(UserList, '/users')


@blueprint.route('/me', methods=['GET'])
@jwt_required
def me():
    """Show current logged in user user.

    Returns:
        user: A JSON dictionary of the user data.
    """
    user_identity = get_jwt_identity()
    user = User.query.get(user_identity)

    schema = UserSchema()

    user_data = schema.dump(user).data

    return jsonify({'user': user_data}), 200


@blueprint.route('/test', methods=['POST'])
def stringify_json():
    variable = json.dumps(request.get_json())
    client = docker.from_env()
    result = client.containers.run("alpine:latest",
                                   ["printenv", "STRING"],
                                   auto_remove=True,
                                   environment=["STRING={}".format(variable)])

    return result.decode(), 200
