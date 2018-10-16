import json
import factory
from pytest_factoryboy import register

from smoke_backend.models import User
from smoke_backend.extensions import db


@register
class UserFactory(factory.Factory):

    username = factory.Sequence(lambda n: 'user%d' % n)
    email = factory.Sequence(lambda n: 'user%d@mail.com' % n)
    password = "mypwd"
    privilege_id = 1

    class Meta:
        model = User


def test_logout(client, db, admin_headers):
    rep = client.delete('/auth/logout', headers=admin_headers)

    assert rep.status_code == 200
    assert 'Successful' in rep.get_json()['msg']
