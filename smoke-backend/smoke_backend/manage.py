# -*- coding: utf-8 -*-

import click
from flask.cli import FlaskGroup

from smoke_backend.app import create_app


def create_smoke(info):
    return create_app(cli=True)


@click.group(cls=FlaskGroup, create_app=create_smoke)
def cli():
    """Main entry point"""
    init()


@cli.command("init")
def init():
    """Init application, create database tables
    and create a new user named admin with password admin
    """

if __name__ == "__main__":
    cli()
