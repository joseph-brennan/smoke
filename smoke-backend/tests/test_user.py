import factory
from pytest_factoryboy import register

from smoke_backend.models import User, Privilege


@register
class UserFactory(factory.Factory):

    username = factory.Sequence(lambda n: 'user%d' % n)
    email = factory.Sequence(lambda n: 'user%d@mail.com' % n)
    password = "mypwd"
    privilege_id = 2

    class Meta:
        model = User

def test_get_user_permission_student(client, db, user, admin_headers):

    data = {'username': 'labrat',
            'email': 'labrat@test.com',
            'password': 'labratsrule',
            }

    rep = client.post(
        '/api/v1/users',
        json=data,
        headers=admin_headers
    )

    assert rep.status_code == 201

    data = rep.get_json()
    user = db.session.query(User).filter_by(id=data['user']['id']).first()

    assert user.username == 'labrat'
    assert user.email == 'labrat@test.com'
    assert user.privilege_id == 1
    assert user.privilege.permission_level == 'STUDENT'

def test_get_user_permission_teacher(client, db, teacher_user, admin_headers):

    #data = {'username': 'labrat',
    #        'email': 'labrat@test.com',
    #        'password': 'labratsrule',
    #        'privilege_id': 2
    #        }

    #rep = client.post(
    #    '/api/v1/users',
    #    json=data,
    #    headers=admin_headers
    #)
    #assert rep.status_code == 201

    #data = rep.get_json()
    #user = db.session.query(User).filter_by(id=data['user']['id']).first()

    assert teacher_user.username == 'teacher'
    assert teacher_user.email == 'teacher@teacher.com'
    assert teacher_user.privilege_id == 2
    assert teacher_user.privilege.permission_level == 'TEACHER'

def test_get_user_permission_admin(client, db, admin_user, admin_headers):

    #permission_admin = Privilege.query.get(3)

    #data = {'username': 'labrat',
    #        'email': 'labrat@test.com',
    #        'password': 'labratsrule',
    #        'privilege_id': 3
    #        }

    #rep = client.post(
    #    '/api/v1/users',
    #    json=data,
    #    headers=admin_headers
    #)
    #assert rep.status_code == 201

    #data = rep.get_json()
    #user = db.session.query(User).filter_by(id=data['user']['id']).first()

    assert admin_user.username == 'admin'
    assert admin_user.email == 'admin@admin.com'
    assert admin_user.privilege_id == 3
    assert admin_user.privilege.permission_level == 'ADMIN'

def change_user_permission(client, db, user, admin_headers):
        data = {'username': 'labrat',
                'email': 'labrat@test.com',
                'password': 'labratsrule',
                'privilege_id': 1
                }

        rep = client.post(
            '/api/v1/users',
            json=data,
            headers=admin_headers
        )
        assert rep.status_code == 201

        data = {'permission': 2}

        rep = client.put(
            '/api/v1/users/%d' % user.id,
            json=data,
            headers=admin_headers
        )
        assert rep,status_code == 200

        data = rep.get_json()['user']
        assert data['privilege_id'] == 2
        assert data['privilege.permission_level'] == 'TEACHER'

        check = db.session.query(User).filter_by().first() is None

def test_get_user(client, db, user, admin_headers):
    # test 404
    rep = client.get("/api/v1/users/100000", headers=admin_headers)
    assert rep.status_code == 404

    db.session.add(user)
    db.session.commit()

    # test get_user
    rep = client.get('/api/v1/users/%d' % user.id, headers=admin_headers)
    assert rep.status_code == 200

    data = rep.get_json()['user']
    assert data['username'] == user.username
    assert data['email'] == user.email
    assert data['active'] == user.active


def test_put_user(client, db, user, admin_headers):
    # test 404
    rep = client.put("/api/v1/users/100000", headers=admin_headers)
    assert rep.status_code == 404

    db.session.add(user)
    db.session.commit()

    data = {'username': 'updated'}

    # test update user
    rep = client.put(
        '/api/v1/users/%d' % user.id,
        json=data,
        headers=admin_headers
    )
    assert rep.status_code == 200

    data = rep.get_json()['user']
    assert data['username'] == 'updated'
    assert data['email'] == user.email
    assert data['active'] == user.active

    # test 422
    data = {'username': 42}
    rep = client.put(
        '/api/v1/users/%d' % user.id,
        json=data,
        headers=admin_headers

    )
    assert rep.status_code == 422


def test_delete_user(client, db, user, admin_headers):
    # test 404
    rep = client.put("/api/v1/users/100000", headers=admin_headers)
    assert rep.status_code == 404

    db.session.add(user)
    db.session.commit()

    # test get_user
    user_id = user.id
    rep = client.delete(
        '/api/v1/users/%d' % user_id,
        headers=admin_headers
    )
    assert rep.status_code == 200
    assert db.session.query(User).filter_by(id=user_id).first() is None


def test_create_user(client, db, admin_headers):
    # test bad data
    data = {
        'username': 'created'
    }
    rep = client.post(
        '/api/v1/users',
        json=data,
        headers=admin_headers
    )
    assert rep.status_code == 422

    data['password'] = 'admin'
    data['email'] = 'create@mail.com'

    rep = client.post(
        '/api/v1/users',
        json=data,
        headers=admin_headers
    )
    assert rep.status_code == 201

    data = rep.get_json()
    user = db.session.query(User).filter_by(id=data['user']['id']).first()

    assert user.username == 'created'
    assert user.email == 'create@mail.com'


def test_get_all_user(client, db, user_factory, admin_headers):
    users = user_factory.create_batch(30)

    db.session.add_all(users)
    db.session.commit()

    rep = client.get('/api/v1/users', headers=admin_headers)
    assert rep.status_code == 200

    results = rep.get_json()
    for user in users:
        assert any(u['id'] == user.id for u in results['results'])


def test_permission_table(client, db, admin_headers):

    permissions = Privilege.query.all()

    assert permissions[0].permission_level == "STUDENT"
    assert permissions[0].id == 1
    assert permissions[1].permission_level == "TEACHER"
    assert permissions[2].permission_level == "ADMIN"


def test_get_current_user(client, db, admin_user, admin_headers):

    rep = client.get('/api/v1/me', headers=admin_headers)
    assert rep.status_code == 200

    data = rep.get_json()['user']
    assert data['username'] == admin_user.username
    assert data['email'] == admin_user.email
    assert data['active'] == admin_user.active
