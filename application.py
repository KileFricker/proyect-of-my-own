from flask import Flask, render_template, jsonify, request
from classer import *
import os


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://emghmbfduzrqfd:d3d8b6906a02336c79d466a5eec0a4411abd1ae0444707834b0304922d8ae7ba@ec2-34-230-149-169.compute-1.amazonaws.com:5432/d2qm6ulko4sunr"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

@app.route("/")
def index():
    return render_template("firstpage.html")


@app.route("/logup")
def logup():
    return render_template("logup.html")

@app.route("/success", methods=["POST"])
def success():
    Password = request.form.get("Password")
    Bn = request.form.get("Password_repeat")
    Username = request.form.get("username")
    if Password == Bn:
        #User.useradd(Username, Password)
        return render_template("sucess.html")
    else:
        return render_template("error.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/main", methods=["POST"])
def main():
    Username = request.form.get("username")
    Password = request.form.get("Password")
    HI = User.query.filter_by(Username=Username, Password=Password).count()
    if HI == 1:
        return render_template("MainPage.html", Username=Username)
    else:
        return render_template("Invalid.html")
