# -*- coding: utf-8 -*-
"""Top level management of the application through flask. [f]_

This module controls/manages the functioning of the smoke backend application.
It is responsible for:

    * Creating the default user
    * Signing the user in
    * Managing the user database

"""

import click
from flask.cli import FlaskGroup

from smoke_backend.app import create_app


def create_smoke(info):
    """Get application from application factory method.

    Parameters:
        info (str): Currently not used.

    Returns:
        Flask: The Flask [f]_ controller object for the backend

    """
    return create_app(cli=True)


@click.group(cls=FlaskGroup, create_app=create_smoke)
def cli():
    """Main entry point

    Forms the entry point for when this method is called as a stand-alone
    application.
    """


@cli.command("init")
def init():
    """Initialize application

    Initializes the SQLAlchemy [flasksqla]_ database and adds a default user.
    """

    from smoke_backend.extensions import db

    click.echo("drop old database")
    db.reflect()
    db.drop_all()
    click.echo("create database")
    db.create_all()
    click.echo("done")


@cli.command("seed")
def seed():
    """Seeds the database with the standard privilege values.

    Relative values noted here are in *descending order*, in that a relative
    privilege value of 3 is the highest value.

    Function also initializes the default user, with a privilege value of
    Admin (3).

    Values:
        Student: User which defines the code to test. (Relative value: 1)
        Teacher: User which defines the test cases. (Relative value: 2)
        Admin: User which has complete access. (Relative value 3)

    """
    from smoke_backend.extensions import db
    from smoke_backend.models import Privilege, User

    privilege1 = Privilege(permission_level="STUDENT")
    privilege2 = Privilege(permission_level="TEACHER")
    privilege3 = Privilege(permission_level="ADMIN")

    click.echo("create priveledges")
    db.session.add(privilege1)
    db.session.add(privilege2)
    db.session.add(privilege3)
    db.session.commit()
    click.echo("create user admin")
    user = User(
        username='admin',
        email='admin@mail.com',
        password='admin',
        active=True,
        privilege=Privilege.query.get(3)
        )
    db.session.add(user)
    db.session.commit()
    click.echo("done")


if __name__ == "__main__":
    cli()
