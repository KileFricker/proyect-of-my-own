import csv
import os

from flask import Flask, render_template, request
from classer import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("postgres://emghmbfduzrqfd:d3d8b6906a02336c79d466a5eec0a4411abd1ae0444707834b0304922d8ae7ba@ec2-34-230-149-169.compute-1.amazonaws.com:5432/d2qm6ulko4sunr")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
    f = open("apps.csv")
    reader = csv.reader(f)
    for app in reader:
        apped = apps(apps=app)
        db.session.add(apped)
        print(f"Added app called {app}")
    db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        main()
