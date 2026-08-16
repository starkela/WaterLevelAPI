from flask import Flask, request, render_template
app = Flask(__name__)

all_data = []

@app.route("/add", methods = ("POST", "GET"))
def add():
    if request.method == "POST":
        waterlevel = request.form["waterlevel"]
        all_data.append(waterlevel)
    return render_template("add.html")

@app.route("/show")
def show():
    if len(all_data) != 0:
            return render_template("show.html", current_level = all_data[-1])
    return render_template("show.html", current_level = "None")

@app.route("/history")
def history():
    return render_template("history.html", water_level = all_data)



