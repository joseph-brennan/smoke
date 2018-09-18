# -*- coding: utf-8 -*-
"""Comunicates with database to create,
update, or delete users
"""
from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required

from smoke_backend.models import User
from smoke_backend.extensions import ma, db
from smoke_backend.commons.pagination import paginate


class UserSchema(ma.ModelSchema):
     """Single object schema

     the value you pass in needs a password so you verify access to the user
     """
    password = ma.String(load_only=True, required=True)

    class Meta:
     """Then it stores the user and database session in the Meta class"""
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
