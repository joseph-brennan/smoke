# -*- coding: utf-8 -*-
"""Communicates with database to create, update, or delete users.

Serialization provided by Marshmallow [#f1]_

.. [#f1] https://marshmallow.readthedocs.io/en/3.0/
.. [#f2] http://docs.sqlalchemy.org/en/latest/orm/session_api.html#sqlalchemy.orm.session.Session
.. [#f3] https://pythonhosted.org/Flask-JWT/
.. [#f4] http://docs.sqlalchemy.org/en/latest/core/schema.html
.. [#f5] https://flask-restful.readthedocs.io/en/0.3.5/quickstart.html
"""
from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required

from smoke_backend.models import User
from smoke_backend.extensions import ma, db
from smoke_backend.commons.pagination import paginate


class UserSchema(ma.ModelSchema):
    """Single object schema

    Class attempts to verify a password passed to it by a user

    Attributes:
        password (String): The user entered password

            Serialization, Persistence, & Verification by Marshmallow [#f1]_

    Args:
        ma.ModelSchema: The SQLAlchemy Schema used by Marshmallow to model the User [#f1]_

    """
    password = ma.String(load_only=True, required=True)

    class Meta:
        """Metadata of the login session

        Attributes:
            model (User): The specific SQLAlchemy Schema [#f4]_ which represents the current user

            sqla_session (Session): The SQLAlchemy session object [#f2]_

        """
        model = User
        sqla_session = db.session


class UserResource(Resource):
    """Single object resource.

    Attributes:
        method_decorators: Singleton array of decorator objects to require a valid JWT token to be present. [#f3]_

    Args:
        Resources: A Flask-RESTful Resource [#f4]_ object to direct the control of this class.
    """
    method_decorators = [jwt_required]

    def get(self, user_id):
        """Show and return a user.

        Args:
            user_id (int): The ID of the user to get.

        Returns:

        """
        schema = UserSchema()
        user = User.query.get_or_404(user_id)
        return {"user": schema.dump(user).data}

    def put(self, user_id):
        """update a user

        Args:
            user_id (int): The ID of the user to get
        """
        schema = UserSchema(partial=True)
        user = User.query.get_or_404(user_id)
        user, errors = schema.load(request.json, instance=user)
        if errors:
            return errors, 422

        return {"msg": "user updated", "user": schema.dump(user).data}

    def delete(self, user_id):
        """delete a user

        Args:
            user_id (int): The ID of the user to get
        """
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()

        return {"msg": "user deleted"}


class UserList(Resource):
    """Creation and get_all

    Attributes:
        method_decorators: Array of decorator objects to require a valid JWT token to be present. [#f3]_

    """
    method_decorators = [jwt_required]

    def get(self):
        """Get a list of all users

        Returns:
            A paginated list of all the users as defined by pagination.py
        """
        schema = UserSchema(many=True)
        query = User.query
        return paginate(query, schema)

    def post(self):
        """Create a new user & put it in the database if there are no errors

        Returns:
            String: Noting whether the user was created or the error which caused creation to fail
        """
        schema = UserSchema()
        user, errors = schema.load(request.json)
        if errors:
            return errors, 422

        db.session.add(user)
        db.session.commit()

        return {"msg": "user created", "user": schema.dump(user).data}, 201
