# -*- coding: utf-8 -*-
"""Creates view for user login authentication.

Attributes:
    blueprint (Flask Blueprint): The blueprint scheme for smoke. [fblueprint]_
"""

from flask import request, jsonify, Blueprint
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_refresh_token_required,
    jwt_required,
    get_jwt_identity,
    get_raw_jwt
)

from smoke_backend.models import User
from smoke_backend.extensions import pwd_context, jwt


blacklist = set()
blueprint = Blueprint('auth', __name__, url_prefix='/auth')


@blueprint.route('/login', methods=['POST'])
def login():
    """Authenticate user and return token.

    Uses flask's jsonify function to convert requests to valid JSON objects.
    [fjsonify]_

    Return:
        flask.Response: If valid request & credentials present, returns the
            valid access tokens for the backend in JSON format.

            If the user password or username is missing or invalid, then method
            returns a JSON formatted message noting how the method failed.

    .. _Flask Local Proxy Request through werkzeug local:
        http://werkzeug.pocoo.org/docs/0.14/wrappers/
    """
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if not username or not password:
        return jsonify({"msg": "Missing username or password"}), 400

    user = User.query.filter_by(username=username).first()
    if user is None or not pwd_context.verify(password, user.password):
        return jsonify({"msg": "Bad credentials"}), 400

    access_token = create_access_token(identity=user.id)
    refresh_token = create_refresh_token(identity=user.id)

    ret = {
        'access_token': access_token,
        'refresh_token': refresh_token
    }
    return jsonify(ret), 200


@blueprint.route('/refresh', methods=['POST'])
@jwt_refresh_token_required
def refresh():
    """Receives access token and refreshes the page.

    Requires a valid jwt token for access to method. [fjwtfresh]_

    Returns:
        flask.response: A JSONified object containing the updated contents of
            the login page. [fjsonify]_
    """
    current_user = get_jwt_identity()
    ret = {
        'access_token': create_access_token(identity=current_user)
    }
    return jsonify(ret), 200


@blueprint.route('/logout', methods=['DELETE'])
@jwt_required
def logout():
    jti = get_raw_jwt()['jti']
    blacklist.add(jti)
    return jsonify({"msg": "Successfully logged out"}), 200


@jwt.user_loader_callback_loader
def user_loader_callback(identity):
    """Returns user information.

    Parameters:
        identity: The unique identifier for the user.

    Returns:
        flask.response: The user data as a JSON dictionary.
    """
    return User.query.get(identity)
