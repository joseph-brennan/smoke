# -*- coding: utf-8 -*-
from . import User
from smoke_backend.extensions import db, pwd_context


class Admin(User):
    """Basic user model
    """
    permissions = db.Column(db.String(8), default='admin')

    def __init__(self, **kwargs):
        super(Admin, self).__init__(**kwargs)
        self.password = pwd_context.hash(self.password)
