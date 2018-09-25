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
    """Creating a class for cross origin resource sharing for the application

    at the simplest use of the CORS extension is to allow CORS for all domains on all routes.
    The settings for CORS are determined in the following order

    1. Resource level settings (e.g when passed as a dictionary)
    2. Keyword argument settings
    3. App level configuration settings (e.g. CORS_*)
    4. Default settings
    """

    def init_app(self, app, *args, **kwargs):
        """ defines arguments to leverage flasks CORS method 

        Args: 
        	app: app obeject, the resources and options may be specified in the App Config
        	*args: Variable length argument list.
        	**kwargs: Arbitrary keyword arguments.
        """

        CORS(app, *args, **kwargs)


cors = Cors()
db = SQLAlchemy()
jwt = JWTManager()
ma = Marshmallow()
migrate = Migrate()
pwd_context = CryptContext(schemes=['pbkdf2_sha256'], deprecated='auto')
