from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required

from application.players.models import Player
from application.players.forms import PlayerForm
from application.teams.models import Team


@app.route("/players", methods=["GET"])
def players_index():
    return render_template("players/list.html", players=Player.all_players())  # .query.all())


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
    
    team_id = Team.find_team_id(str(form.team_name.data))

    p = Player(form.name.data, form.number.data, form.position.data, team_id[0])    

    db.session().add(p)
    db.session().commit()

    return redirect(url_for("players_index"))
