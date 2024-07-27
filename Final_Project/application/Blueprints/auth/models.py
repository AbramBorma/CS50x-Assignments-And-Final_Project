from application.extensions import db
from werkzeug.security import generate_password_hash
from application.Blueprints.venues.models import Venue
from sqlalchemy import ForeignKey

''' Creating all the authentication models. '''

class User(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    question_id = db.Column(db.Integer, ForeignKey('questions.id'), nullable=False)
    question = db.relationship('Questions', backref='user')
    answer = db.Column(db.String(128), nullable=True)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

class Questions(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(512), unique=True, nullable=False)