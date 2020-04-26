import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.model):

    __tablename__="user information"
    id= db.column(db.integer, primary_key=True)
    Username= db.Column(db.string, nullable=False)
    Password= db.column(db.string, nullable=False, hidden=True)
    Setinfo= db.relationship("app", backref="User", lazy=True)
    Setinfo= db.relationship("apppassword", backref="User", lazy=True)


    def addapp(self, app):
        add = app(app=app, user_id=self.id)
        db.session.add(add)

class app(db.model):
    __tablename__= "App"
    id = db.column(db.integer, primary_key=True)
    user_id = db.column(db.integer, db.ForeignKey("User.id"), nullable=False)
    app= db.column(db.string, primary_key=True)
    Setinfo= db.relationship("apppassword", backref="app", lazy=True)

    def addapppassword(self, user_id, Password):
        adp = apppassword(user_id=user_id, app_name=self.app, Password=Password)
        db.session.add(adp)
        db.session.commit()


class apppassword(db.model):
    __tablename__= "apppassword"
    id = db.column(db.integer, primary_key=True)
    user_id = db.column(db.integer, db.ForeignKey("User.id"), nullable=False)
    app_name = db.column(db.integer, db.ForeignKey("app.app"), nullable=False)
    Password = Username= db.Column(db.string, nullable=False)

    
