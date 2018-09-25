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
from flask import Blueprint
from flask_restful import Api

from smoke_backend.api.resources import UserResource, UserList


blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(blueprint)


api.add_resource(UserResource, '/users/<int:user_id>')
api.add_resource(UserList, '/users')
