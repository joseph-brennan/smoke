# -*- coding: utf-8 -*-

"""Extensions registry

All extensions here are used as singletons and
initialized in application factory
"""
from flask_sqlalchemy import SQLAlchemy
from passlib.context import CryptContext
from flask_jwt_extended import JWTManager
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_cors import CORS


class Cors():
    """Creating a class for cross origin resource sharing """

    def init_app(self, app, *args, **kwargs):
        """takes an optional app object and, if supplied, will call init_app."""
        CORS(app, *args, **kwargs)


cors = Cors()
db = SQLAlchemy()
jwt = JWTManager()
ma = Marshmallow()
migrate = Migrate()
pwd_context = CryptContext(schemes=['pbkdf2_sha256'], deprecated='auto')
