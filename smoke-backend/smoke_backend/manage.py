# -*- coding: utf-8 -*-

import click
from flask.cli import FlaskGroup

from smoke_backend.app import create_app


def create_smoke(info):
    return create_app(cli=True)


@click.group(cls=FlaskGroup, create_app=create_smoke)
def cli():
    """Main entry point"""
    from smoke_backend.extensions import db
    from smoke_backend.models import User
    click.echo("create database")
    db.create_all()
    click.echo("done")
    click.echo("create user")
    user = User(
        username='admin',
        email='admin@mail.com',
        password='admin',
        active=True,
        privilege_id=3
    )
    db.session.add(user)
    db.session.commit()
    click.echo("created user admin")


@cli.command("init")
def init():
    """Init application, create database tables
    and create a new user named admin with password admin
    """

if __name__ == "__main__":
    cli()
