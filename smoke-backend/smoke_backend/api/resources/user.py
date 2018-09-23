# -*- coding: utf-8 -*-
"""Communicates with database to create, update, or delete users


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
    """
    password = ma.String(load_only=True, required=True)

    class Meta:
        """Metadata of the login session

        Attributes:
            model (User): The user schema

            sqla_session (Session): The SQLAlchemy session object [#f1]_

        .. [f#1] http://docs.sqlalchemy.org/en/latest/orm/session_api.html#sqlalchemy.orm.session.Session

        """
        model = User
        sqla_session = db.session


class UserResource(Resource):
    """Single object resource"""
    method_decorators = [jwt_required]

    def get(self, user_id):
        """show and return a user"""
        schema = UserSchema()
        user = User.query.get_or_404(user_id)
        return {"user": schema.dump(user).data}

    def put(self, user_id):
        """update a user"""
        schema = UserSchema(partial=True)
        user = User.query.get_or_404(user_id)
        user, errors = schema.load(request.json, instance=user)
        if errors:
            return errors, 422

        return {"msg": "user updated", "user": schema.dump(user).data}

    def delete(self, user_id):
        """delete a user"""
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()

        return {"msg": "user deleted"}


class UserList(Resource):
    """Creation and get_all"""
    method_decorators = [jwt_required]

    def get(self):
        """give a list of all users"""
        schema = UserSchema(many=True)
        query = User.query
        return paginate(query, schema)

    def post(self):
        """create a new user if no errors"""
        schema = UserSchema()
        user, errors = schema.load(request.json)
        if errors:
            return errors, 422

        db.session.add(user)
        db.session.commit()

        return {"msg": "user created", "user": schema.dump(user).data}, 201
