# -*- coding: utf-8 -*-

"""Default configuration. Use `env` var to override
"""
DEBUG = True
SECRET_KEY = "changeme"

SQLALCHEMY_DATABASE_URI = "sqlite:////tmp/smoke_backend.db"
SQLALCHEMY_TRACK_MODIFICATIONS = False
