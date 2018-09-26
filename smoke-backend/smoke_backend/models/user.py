# -*- coding: utf-8 -*-

from smoke_backend.extensions import db, pwd_context
from smoke_backend.models.modelhelpers.enum_privilege import Privileges as p_enum

class User(db.Model):
    """Basic user model, utilizing an enum helper to give predefined value for permission level
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    active = db.Column(db.Boolean, default=True)
    permission = db.Column(db.Enum(p_enum), default=p_enum.STUDENT)

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        self.password = pwd_context.hash(self.password)
