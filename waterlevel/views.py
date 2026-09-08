from flask import (
    Blueprint, render_template, request
)
from waterlevel.db import get_db

bp = Blueprint("views", __name__)

@bp.route("/add", methods = ["POST"])
def add():
    if request.method == "POST":
        content = request.json
        waterlevel = content["waterlevel"]
        db = get_db()
        db.execute(
             "INSERT INTO cistern (waterlevel)"
             " VALUES (?)",
             (waterlevel,)
        )
        db.commit()
    return "post"

@bp.route("/")
def show():
    db = get_db()
    data = db.execute("SELECT measured, waterlevel "
                            "FROM cistern "
                            "WHERE measured = ("
                                "SELECT MAX(measured) " \
                                "FROM cistern" 
                            ")"
                            ).fetchone()
    waterlevel = data["waterlevel"]
    percentage = waterlevel / 3000
    return render_template("views/show.html", waterlevel = waterlevel, percentage = percentage)

@bp.route("/history")
def history():
    db = get_db()
    data = db.execute("SELECT measured, waterlevel "
                            "FROM cistern "
                            ).fetchall()
    waterlevel =  []
    measured = []
    for row in data:
        waterlevel.append(row["waterlevel"])
        measured.append(row["measured"])
    return render_template("views/history.html", waterlevel = waterlevel, measured = measured)
