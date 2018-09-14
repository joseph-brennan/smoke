# -*- coding: utf-8 -*-

from smoke_backend.extensions import db, pwd_context


class User(db.Model):
    """Basic user model.
       set up a User classs with properties which will be set up
       in a database table (unique, null or not null) and the data type
       Each entity will have 5 properties with id property as primary key """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    active = db.Column(db.Boolean, default=True)

    def __init__(self, **kwargs):
        """ Constructor for User class, it is hashing the password provided
            by the user
        """        
        super(User, self).__init__(**kwargs)
        self.password = pwd_context.hash(self.password)
