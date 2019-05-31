from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required

from application.players.models import Player
from application.players.forms import PlayerForm


@app.route("/players", methods=["GET"])
def players_index():
    return render_template("players/list.html", players = Player.query.all())


@app.route("/players/new/")
@login_required
def players_form():
    return render_template("players/new.html", form = PlayerForm())


@app.route("/players/<player_id>/", methods=["POST"])
@login_required
def players_change_position(player_id):

    p = Player.query.get(player_id)
    p.position = request.form.get("position")
    db.session().commit()
  
    return redirect(url_for("players_index"))


@app.route("/players/", methods=["POST"])
@login_required
def players_create():
    form = PlayerForm(request.form)

    if not form.validate():
        return render_template("players/new.html", form = form)
        
    p = Player(form.name.data, form.number.data, form.position.data)    

    db.session().add(p)
    db.session().commit()

    return redirect(url_for("players_index"))
