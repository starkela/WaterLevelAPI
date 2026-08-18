import os
from flask import Flask, request, render_template, jsonify
from . import db


app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(
    SECRET_KEY='dev',
    DATABASE=os.path.join(app.instance_path, 'cistern.sqlite'),
)
db.init_app(app)

@app.route("/add", methods = ["POST"])
def add():
    if request.method == "POST":
        content = request.json
        waterlevel = content["waterlevel"]
        database = db.get_db()
        database.execute(
             "INSERT INTO cistern (waterlevel)"
             " VALUES (?)",
             (waterlevel,)
        )
        database.commit()
    return render_template("add.html")

@app.route("/show")
def show():
    database = db.get_db()
    data = database.execute("SELECT measured, waterlevel "
                            "FROM cistern "
                            "WHERE measured = ("
                                "SELECT MAX(measured) " \
                                "FROM cistern" 
                            ")"
                            ).fetchone()
    waterlevel = data["waterlevel"]
    percentage = waterlevel / 3000
    return render_template("show.html", current_level = waterlevel, percentage = percentage)

@app.route("/history")
def history():
    database = db.get_db()
    data = database.execute("SELECT measured, waterlevel "
                            "FROM cistern "
                            ).fetchall()
    waterlevel =  []
    measured = []
    for row in data:
        waterlevel.append(row["waterlevel"])
        measured.append(row["measured"])
    return render_template("history.html", waterlevel = waterlevel, measured = measured)
