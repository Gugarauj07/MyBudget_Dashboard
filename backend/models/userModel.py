from flask_sqlalchemy import SQLAlchemy
from config import app_config

config = app_config['development']
db = SQLAlchemy(config.APP)

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(100))

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
    
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email
        }