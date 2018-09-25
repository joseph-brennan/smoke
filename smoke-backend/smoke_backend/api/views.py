# -*- coding: utf-8 -*-
"""Setting up API routes

Uses a Flask blueprint [#f1]_ to control the function of the various libraries used by smoke.

Attributes:
    blueprint (Flask Blueprint): The blueprint [#f1]_ for the smoke api.

    api (Flask-RESTful): An extension for Flask to build RESTful APIs through ORM libraries. [#f2]_

.. [#f1] http://flask.pocoo.org/docs/1.0/blueprints/
.. [#f2] https://flask-restful.readthedocs.io/en/latest/
"""
from flask import Blueprint
from flask_restful import Api

from smoke_backend.api.resources import UserResource, UserList


blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(blueprint)


api.add_resource(UserResource, '/users/<int:user_id>')
api.add_resource(UserList, '/users')
