from smoke_backend.extensions import db, pwd_context

class User(db.Model):
    """Basic user model
    utilizing an enum helper to give predefined
    value for permission level
    """
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    active = db.Column(db.Boolean, default=True)
    privilege_id = db.Column(
        db.Integer, db.ForeignKey('privilege.id'), default=1)

    # Relationship
    privilege = db.relationship('Privilege')

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        self.password = pwd_context.hash(self.password)
