# -*- coding: utf-8 -*-

from flask import Flask

from smoke_backend import auth, api
from smoke_backend.extensions import cors, db, jwt, migrate


def create_app(config=None, testing=False, cli=False):
    """Application factory, used to create application
    """
    app = Flask('smoke_backend')
    configure_app(app, testing)
    configure_extensions(app, cli)
    register_blueprints(app)

    return app


def configure_app(app, testing=False):
    """set configuration for application
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
    """configure flask extensions
    """
    cors.init_app(app)
    db.init_app(app)
    jwt.init_app(app)

    if cli is True:  # pragma: no cover
        migrate.init_app(app, db)


def register_blueprints(app):
    """register all blueprints for application
    """
    app.register_blueprint(auth.views.blueprint)
    app.register_blueprint(api.views.blueprint)
