"""
Single value SQLAlchemy model representing the privilege of a user.

Typical privileged groups include a 'Teacher' (the user defining the test
cases) or a 'Student' (the user defining the code to test).

Privileged classes are ranked by an integer value.
"""
from smoke_backend.extensions import db


class Privilege(db.Model):

    id = db.Column('id', db.Integer, primary_key=True)
    permission_level = db.Column(
        'permission_level', db.Integer, unique=True)

    def __init__(self, **kwargs):
        super(Privilege, self).__init__(**kwargs)
