from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Pitch(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    category = db.Column(db.String(300))
    comments = db.relationship('Comment', backref='pitch_id', lazy='dynamic')
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    comments = db.relationship('Comment', backref='user_id', lazy='dynamic')
    username = db.Column(db.String(150))

    def __repr__(self):
        return f'User {self.username}'

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(2000))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitch.id'))
