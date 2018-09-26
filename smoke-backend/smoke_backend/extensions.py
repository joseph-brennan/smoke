# -*- coding: utf-8 -*-

"""Extensions registry.

All extensions here are used as singletons and initialized in their application
factory.

Attributes:
    cors (flask_cors): The CORS strategy for allowing access to restricted
        objects. [cors]_  Safe for cross-origin AJAX. [ajax]_

        Provided by Flask-CORS [fcors]_

    db (flask_sqlalchemy): The SQL database handler.

        Provided by Flask-SQLAlchemy. [fsqla]_

    jwt (flask_jwt_extended): The JWT handler to process JSON web tokens.
        [jwt]_

        Provided by Flask-JWT-Extended. [fjwt]_

    ma (flask_marshmallow): Serialization handler. Integrates with SQLAlchemy
        for data persistence.

        Provided by Flask-Marshmallow. [fmar]_ [mar]_

    migrate (flask_migrate): Schema migration handler. Allows for incremental
        changes to the current SQLAlchemy schema without breaking current
        objects. [mig]_

        Provided by Flask-Migrate. [fmig]_

    pwd_context (PassLib context): Cryptographic password handler.

        Provided by PassLib. [pas]_
"""
from flask_sqlalchemy import SQLAlchemy
from passlib.context import CryptContext
from flask_jwt_extended import JWTManager
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_cors import CORS


class Cors():
    """Creates a class for COS in the backend. [cors]_ [fcors]_

    Per the CORS documentation, the settings for CORS are determined in the
    following order:

        1. Resource level settings (e.g when passed as a dictionary)
        2. Keyword argument settings
        3. App level configuration settings (e.g. CORS_*)
        4. Default settings
    """

    def init_app(self, app, *args, **kwargs):
        """ Defines arguments to leverage flasks CORS method

        Parameters:
            app (Flask app): the Flask app from which to configure CORS model.
        """

        CORS(app, *args, **kwargs)


cors = Cors()
db = SQLAlchemy()
jwt = JWTManager()
ma = Marshmallow()
migrate = Migrate()
pwd_context = CryptContext(schemes=['pbkdf2_sha256'], deprecated='auto')
