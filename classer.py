import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):

    __tablename__="user_information"
    id= db.Column(db.Integer, primary_key=True)
    Username= db.Column(db.String,  unique=True)
    Password= db.Column(db.String, nullable=False)
    Setinfo= db.relationship("app", backref="User", lazy=True)

    def useradd(Username, Password):
        createuser = User(Username=Username, Password=Password)
        db.session.add(createuser)
        db.session.commit()


class apps(db.Model):
    __tablename__= "apps"
    id = db.Column(db.Integer, primary_key=True)
    apps = db.Column(db.String, nullable=False)
    Setinfo= db.relationship("app", backref="apps", lazy=True)


class app(db.Model):
    __tablename__= "app"
    id = db.Column(db.Integer, primary_key=True)
    apps_id = db.Column(db.Integer, db.ForeignKey("apps.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user_information.id"), nullable=False)
    Password= db.Column(db.String, nullable=False)
