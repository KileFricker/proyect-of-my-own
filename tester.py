from flask import Flask, render_template, jsonify, request, url_for, redirect
from classer import *
import os
from codificador import codificador

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://emghmbfduzrqfd:d3d8b6906a02336c79d466a5eec0a4411abd1ae0444707834b0304922d8ae7ba@ec2-34-230-149-169.compute-1.amazonaws.com:5432/d2qm6ulko4sunr"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)



Id = User.query.filter_by(Username=Admin)
id = Id.id
print(id)
