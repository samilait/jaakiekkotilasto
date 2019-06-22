from application import app, db, login_required
from flask import redirect, render_template, request, url_for
from flask_login import current_user

from application.players.models import Player
from application.players.forms import PlayerForm
from application.teams.models import Team


@app.route("/players", methods=["GET"])
def players_index():
    return render_template("players/list.html", players=Player.all_players())  # .query.all())


@app.route("/players/new/")
@login_required(role="ADMIN")
def players_form():
    return render_template("players/new.html", form = PlayerForm())


@app.route("/players/<player_id>/", methods=["POST"])
@login_required(role="ADMIN")
def players_change_position(player_id):

    p = Player.query.get(player_id)
    p.position = request.form.get("position")

    # if t.account_id != current_user.id:
    #     # tee jotain, esim. 
    #     return login_manager.unauthorized()
    
    db.session().commit()
  
    return redirect(url_for("players_index"))


@app.route("/players/", methods=["POST"])
@login_required(role="ADMIN")
def players_create():
    form = PlayerForm(request.form)

    if not form.validate():
        return render_template("players/new.html", form = form)
    
    sel_team_name = str(dict(form.team_name.choices).get(form.team_name.data))
    
    team_id = Team.find_team_id(sel_team_name)

    p = Player(form.name.data, form.number.data, form.position.data, team_id[0])    

    db.session().add(p)
    db.session().commit()

    return redirect(url_for("players_index"))
