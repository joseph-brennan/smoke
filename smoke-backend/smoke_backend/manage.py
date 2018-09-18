# -*- coding: utf-8 -*-
""" This file manages the database of users, the creation of users,
and the initialization of both for the backend of smokr. """


import click 
from flask.cli import FlaskGroup
from smoke_backend.app import create_app


def create_smoke(info):
    """ Get application from application factory method """
    return create_app(cli=True)


@click.group(cls=FlaskGroup, create_app=create_smoke)
def cli():
    """Main entry point"""


@cli.command("init")
def init():
    """Init application, create database tables
    and create a new user named admin with password admin
    """

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
        active=True
    )
    
    
    db.session.add(user)
    db.session.commit()
    click.echo("created user admin")

if __name__ == "__main__":
    """ If this method is called as the main method, start client mode """
    cli()
