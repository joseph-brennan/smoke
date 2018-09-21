# -*- coding: utf-8 -*-
    """Top level management of the application

    This module controls/manages the functioning of the smoke backend application.
    It is responsible for

        * Creating the default user
        * Signing the user in
        * Managing the user database"""

import click 
from flask.cli import FlaskGroup
from smoke_backend.app import create_app


def create_smoke(info):
    """Get application from application factory method

    Args:
        info (str): An info string which is never used

    Returns:
        Flask: The Flask [#f1]_ controller object for the backend
    
    .. [#f1] http://flask.pocoo.org/

    """
    return create_app(cli=True)


@click.group(cls=FlaskGroup, create_app=create_smoke)
def cli():
    """Main entry point

    Forms the entry point for when this method is called as 
    a stand-alone application. 
    """


@cli.command("init")
def init():
    """Initialize application

    Creates the default user & creates the database users
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
    cli()
