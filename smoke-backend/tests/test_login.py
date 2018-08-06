import json
import factory
from pytest_factoryboy import register

from smoke.models import User


@register
class UserFactory(factory.Factory):

    username = factory.Sequence(lambda n: 'user%d' % n)
    email = factory.Sequence(lambda n: 'user%d@mail.com' % n)
    password = "mypwd"

    class Meta:
        model = User


def test_login(client, db, user):
    # test 400 missing JSON
    rep = client.post('/auth/login')
    assert rep.status_code == 400
    assert rep.get_json()['msg'] == 'Missing JSON in request'

    #test 400 missing username
    rep = client.post(
      '/auth/login',
      data=json.dumps({'password': 'bogus'}),
      headers={'content-type': 'application/json'}
    )
    assert rep.status_code == 400
    assert rep.get_json()['msg'] == 'Missing username or password'

    #test 400 missing password
    rep = client.post(
      '/auth/login',
      data=json.dumps({'username': 'bogus'}),
      headers={'content-type': 'application/json'}
    )
    assert rep.status_code == 400
    assert rep.get_json()['msg'] == 'Missing username or password'

    #test 400 missing username
    rep = client.post(
      '/auth/login',
      data=json.dumps({'username': 'bogus', 'password': 'bogus'}),
      headers={'content-type': 'application/json'}
    )
    assert rep.status_code == 400
    assert rep.get_json()['msg'] == 'Bad credentials'


def test_refresh(client, db, user, admin_refresh_headers):
    rep = client.post('/auth/refresh', headers=admin_refresh_headers)
    assert rep.status_code == 200