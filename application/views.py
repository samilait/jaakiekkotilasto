from flask import render_template
from application import app
from application.players.models import Player


@app.route("/")
def index():
    return render_template("index.html", num_of_forwards=Player.num_of_forwards())
