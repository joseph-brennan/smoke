# -*- coding: utf-8 -*-

import click
from flask.cli import FlaskGroup

from smoke_backend.app import create_app


def create_smoke(info):
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
    click.echo("create database")
    db.create_all()
    click.echo("done")

@cli.command("seed")
def seed():
    from smoke_backend.extensions import db
    from smoke_backend.models import Privilege, User

    privilege1 = Privilege(permission_level="STUDENT")
    privilege2 = Privilege(permission_level="TEACHER")
    privilege3 = Privilege(permission_level="ADMIN")
    db.session.add(privilege1)
    db.session.add(privilege2)
    db.session.add(privilege3)

    db.session.commit()

    click.echo("create user")
    user = User(
        username='admin',
        email='admin@mail.com',
        password='admin',
        active=True,
        privilege=Privilege.query.get(3)
        )
    db.session.add(user)
    db.session.commit()
    click.echo("created user admin")



if __name__ == "__main__":
    cli()
