# -*- coding: utf-8 -*-
""""This file creates an instance of Flask for the 'smoke_backend' package and configures flask extensions

"""
from flask import Flask

from smoke_backend import auth, api
from smoke_backend.extensions import cors, db, jwt, migrate


def create_app(config=None, testing=False, cli=False):
    """Application factory, used to create application
    Creates and returns new instance of Flask and configures its extensions

    Args:
        config: not used
        testing(bool): allows testing override for configure_app; default is false
        cli(bool): allows command line interface override for repository migration; default is false

    Returns:
        app(Flask): New Flask object with initialized extensions

    """
    app = Flask('smoke_backend')
    configure_app(app, testing)
    configure_extensions(app, cli)
    register_blueprints(app)

    return app


def configure_app(app, testing=False):
    """Set configuration for application

    Args:
        app(Flask): passes the newly created Flask instance for configuration
        testing(bool): if true, configuration is done through the configtest module

    """
    # default configuration
    app.config.from_object('smoke_backend.config')

    if testing is True:
        # override with testing config
        app.config.from_object('smoke_backend.configtest')
    else:   # pragma: no cover
        # override with env variable, fail silently if not set
        app.config.from_envvar("SMOKE_CONFIG", silent=True)


def configure_extensions(app, cli):
    """Configure flask extensions

    Args:
        app(Flask): used for configuring the extensions of the created Flask instance
        cli(bool): if command line interface is used, repository is migrated; default is false

    cors: enables cross origin resources on the Flask app
    db: initializes the SQLAlchemy Database
    jwt: initializes the JWTManager
    If command line is being used, a migrations repository is created
    """
    cors.init_app(app)
    db.init_app(app)
    jwt.init_app(app)

    if cli is True:  # pragma: no cover
        migrate.init_app(app, db)


def register_blueprints(app):
    """Register all blueprints for application

    Args:
        app(Flask): passes the newly created Flask instance for configuration

    """
    app.register_blueprint(auth.views.blueprint)
    app.register_blueprint(api.views.blueprint)
