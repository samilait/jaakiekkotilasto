from application import app, db
from flask import redirect, render_template, request, url_for
from application.players.models import Player


@app.route("/players", methods=["GET"])
def players_index():
    return render_template("players/list.html", players = Player.query.all())

@app.route("/players/new/")
def players_form():
    return render_template("players/new.html")


@app.route("/players/", methods=["POST"])
def players_create():
    p = Player(request.form.get("name"), request.form.get("number"), request.form.get("position"))

    db.session().add(p)
    db.session().commit()

    return redirect(url_for("players_index"))
