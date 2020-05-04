from flask import Flask, render_template, jsonify, request, url_for, redirect
from classer import *
import os
from codificador import codificador

db = SQLAlchemy()

class User(db.Model):

    __tablename__="user_information"
    id= db.Column(db.Integer, primary_key=True)
    Username= db.Column(db.String,  unique=True)
    Password= db.Column(db.String, nullable=False)
    Setinfo= db.relationship("app", backref="User", lazy=True)


Id = User.query.filter_by(Username=Admin)
id = Id.id
print(id)
