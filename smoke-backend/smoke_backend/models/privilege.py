from smoke_backend.extensions import db


class Privilege(db.Model):

    id = db.Column('id', db.Integer, primary_key=True)
    permission_level = db.Column(
        'permission_level', db.Integer, unique=True)

    def __init__(self, **kwargs):
        super(Privilege, self).__init__(**kwargs)
