# -*- coding: utf-8 -*-

from smoke_backend.extensions import db, pwd_context


class Student(User):
    """Student class with basic permissions
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    active = db.Column(db.Boolean, default=True) 
    permissions = db.Column(db.String, default='student')
    
    def __init__(self, **kwargs):
        super(Student, self).__init__(**kwargs)
        self.password = pwd_context.hash(self.password)
