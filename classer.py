import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):

    __tablename__="user_information"
    id= db.Column(db.Integer, primary_key=True)
    Username= db.Column(db.String,  unique=True)
    Password= db.Column(db.String, nullable=False)
    Setinfo= db.relationship("app_1", backref="User", lazy=True)

    def useradd(Username, Password):
        createuser = User(Username=Username, Password=Password)
        db.session.add(createuser)
        db.session.commit()


class apps(db.Model):
    __tablename__= "apps"
    id = db.Column(db.Integer, primary_key=True)
    apps = db.Column(db.String, nullable=False)
    Setinfo= db.relationship("app_1", backref="apps", lazy=True)


class app_1(db.Model):
    __tablename__= "app_1"
    id = db.Column(db.Integer, primary_key=True)
    apps_id = db.Column(db.Integer, db.ForeignKey("apps.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user_information.id"), nullable=False)
    Password= db.Column(db.String, nullable=False)

def users_app_add(user_id, apps_id, Password):
    createPassword= app_1(user_id=user_id, apps_id=apps_id, Password=Password)
    db.session.add(createPassword)
    db.session.commit()
