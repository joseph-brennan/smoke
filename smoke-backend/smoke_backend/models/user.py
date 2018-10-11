# -*- coding: utf-8 -*-
"""Defines the user model for the database
"""
from smoke_backend.extensions import db, pwd_context


class User(db.Model):
    """Basic user model.

    Extends SQLAlchemy Model to define the ORM for a User of smoke.
    [fsqlamodels]_

    Attributes:
        id (int): The unique identification number of the user. (Primary key)

        username (str): The username of the user. (Unique & non-null)

        email (str): The user's email. (Unique & non-null)

        password (str): The user's password. (Non-null)

        active (bool): Whether the user is currently active.
            (`True` by default)
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    active = db.Column(db.Boolean, default=True)
    privilege_id = db.Column(
        db.Integer, db.ForeignKey('privilege.id'), default=1)

    # Relationship
    privilege = db.relationship('Privilege')

    def __init__(self, **kwargs):
        """Constructor for User class.

        Creates a user with a cryptographically hashed password through
        PassLib. [pas]_

        Parameters:
            **kwargs: The keyword arguments passed to the SQLAlchemy Model
                constructor (which this class inherits from) [fsqlamodels]_
        """
        super(User, self).__init__(**kwargs)
        self.password = pwd_context.hash(self.password)
