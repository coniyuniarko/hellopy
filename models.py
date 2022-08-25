from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    role = db.Column(db.String(8))
    password = db.Column(db.String(255))

    def __repr__(self):
        return '<User %r>' % self.username
    
    def __init__(self, username, password, email, role):
        self.username = username
        self.password = generate_password_hash(password)
        self.email = email
        self.role = role
    
    def is_password_valid(self, password):
        return check_password_hash(self.password, password)
