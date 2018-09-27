import json
import pytest

from smoke_backend.models import User, Privilege
from smoke_backend.app import create_app
from smoke_backend.extensions import db as _db


@pytest.fixture
def app():
    app = create_app(testing=True)
    return app


@pytest.fixture
def db(app):
    _db.app = app

    with app.app_context():
        _db.create_all()

    privilege1 = Privilege(permission_level="STUDENT")
    privilege2 = Privilege(permission_level="TEACHER")
    privilege3 = Privilege(permission_level="ADMIN")

    _db.session.add(privilege1)
    _db.session.add(privilege2)
    _db.session.add(privilege3)

    _db.session.commit()

    yield _db

    _db.session.close()
    _db.drop_all()


@pytest.fixture
def admin_user(db):
    user = User(
        username='admin',
        email='admin@admin.com',
        password='admin',
        privilege_id = 3
    )

    db.session.add(user)
    db.session.commit()

    return user


@pytest.fixture
def teacher_user(db):
    user = User(
        username='teacher',
        email='teacher@teacher.com',
        password='teacher',
        privilege_id=2
    )

    db.session.add(user)
    db.session.commit()

    return user

@pytest.fixture
def admin_headers(admin_user, client):
    data = {
        'username': admin_user.username,
        'password': 'admin'
    }
    rep = client.post(
        '/auth/login',
        data=json.dumps(data),
        headers={'content-type': 'application/json'}
    )

    tokens = json.loads(rep.get_data(as_text=True))
    return {
        'content-type': 'application/json',
        'authorization': 'Bearer %s' % tokens['access_token']
    }


@pytest.fixture
def admin_refresh_headers(admin_user, client):
    data = {
        'username': admin_user.username,
        'password': 'admin'
    }
    rep = client.post(
        '/auth/login',
        data=json.dumps(data),
        headers={'content-type': 'application/json'}
    )

    tokens = json.loads(rep.get_data(as_text=True))
    return {
        'content-type': 'application/json',
        'authorization': 'Bearer %s' % tokens['refresh_token']
    }
