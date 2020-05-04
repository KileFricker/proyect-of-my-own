from flask import Flask, render_template, jsonify, request, url_for, redirect
from classer import *
import os
from codificador import codificador
from sqlalchemy import *

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
        Password = codificador(Password)
        User.useradd(Username, Password)
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
    Password = str(codificador(Password))
    HI = User.query.filter_by(Username=Username, Password=Password).count()
    if HI == 1:
        if 1 == 1:
            return redirect(url_for('initial', Username=Username, Password=Password))
        return render_template("MainPage.html", Username=Username)
    else:
        return render_template("Invalid.html")




@app.route("/initial", methods=["GET", "POST"])
def initial():
    Username = request.args.get('Username', None)
    Password = request.args.get('Username', None)
    Iduser = User.query.with_entities(User.id).filter_by(Username=Username).first()   #db.execute("SELECT id FROM user_information WHERE Username= :Username")
    apps_2 =  app_1.query.with_entities(app_1.apps_id).filter_by(user_id=Iduser) #db.execute("SELECT * FROM app WHERE user_id= :Id")
    apps_name = apps.query.filter_by(id=apps_2).all() #db.execute("SELECT apps FROM apps WHERE id = :apps.apps_id")
    apps_password = app_1.query.filter_by(apps_id=apps_2).all()
    apps_3 = apps.query.with_entities(apps.apps).all()
    if request.method == "POST":
        appd = request.form.get("selected_app")
        bad_chars = [';', ':', '!', "*", '}', '{', ',', "'"]
        for i in bad_chars:
             appd = appd.replace(i, "")
        app_ided= apps.query.with_entities(apps.id).filter_by(apps=appd).first()
        app_ided= sqlalchemy.sql.expression.ClauseElement.compile(app_ided)
        Iduser = sqlalchemy.sql.expression.ClauseElement.compile(Iduser)
        password = request.form.get("apps_password")
        users_app_add(user_id=Iduser, apps_id=app_ided,Password=password)


    return render_template("apps.html", apps_3= apps_3, apps_name=apps_name, apps_password= apps_password, Iduser=Iduser)
