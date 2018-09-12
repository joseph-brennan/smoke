# -*- coding: utf-8 -*-

''' Command Line Tools '''
import click 
''' Flask Command Line Tools'''
from flask.cli import FlaskGroup
''' Import application factory method '''
from smoke_backend.app import create_app


def create_smoke(info):
    ''' Get application from application factory method '''
    return create_app(cli=True)


@click.group(cls=FlaskGroup, create_app=create_smoke)
def cli():
    """Main entry point"""


@cli.command("init")
def init():
    """Init application, create database tables
    and create a new user named admin with password admin
    """
    
    '''' Import the database of User objects through SQLAlchemy '''
    from smoke_backend.extensions import db
    ''' Import the User class '''
    from smoke_backend.models import User
    
    ''' Form the database tables '''
    click.echo("create database")
    db.create_all()
    click.echo("done")

    ''' Create the default user '''
    click.echo("create user")
    user = User(
        username='admin',
        email='admin@mail.com',
        password='admin',
        active=True
    )
    
    ''' Add the user to the database '''
    db.session.add(user)
    db.session.commit()
    click.echo("created user admin")

if __name__ == "__main__":
    ''' If this method is called as the main method, start client mode '''
    cli()
