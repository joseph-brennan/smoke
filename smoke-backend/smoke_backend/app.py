# -*- coding: utf-8 -*-
"""Creates an instance of Flask and configures its' extensions. [fextensions]_
"""
from flask import Flask

from smoke_backend import auth, api
from smoke_backend.extensions import cors, db, jwt, migrate


def create_app(config=None, testing=False, cli=False):
    """Flask application factory. [fappfactory]_

    Creates and returns new instance of Flask and configures its extensions.
    [fextensions]_

    Parameters:
        config: not currently used.

        testing (bool): allows testing override for configure_app; default is
            `False`.

        cli (bool): allows command line interface override for repository
            migration; default is `False`.

    Returns:
        Flask: New Flask application with initialized extensions.
    """
    app = Flask('smoke_backend')
    configure_app(app, testing)
    configure_extensions(app, cli)
    register_blueprints(app)

    return app


def configure_app(app, testing=False):
    """Set configuration for application.

    Configures Flask application through the built in Flask methods. [fconfig]_

    Parameters:
        app (Flask): the newly created Flask instance for configuration.

        testing (bool): if true, configuration is done through the configtest
            module. Else, configuration is done through the SMOKE_CONFIG
            environment variable.

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
    """Configure flask extensions located in extensions.py.

    Parameters:
        app (Flask): Flask application to configure [fconfig]_

        cli (bool): if command line interface is used, migration repository
            is created; default is false
    """
    cors.init_app(app)
    db.init_app(app)
    jwt.init_app(app)

    if cli is True:  # pragma: no cover
        migrate.init_app(app, db)


def register_blueprints(app):
    """Register all blueprints for application. [fblueprint]_

    Parameters:
        app(Flask): Flask application to register the blueprints with.
            [fblueprint]_

    """
    app.register_blueprint(auth.views.blueprint)
    app.register_blueprint(api.views.blueprint)
