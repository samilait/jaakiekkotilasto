from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required

from application.teams.models import Team
from application.teams.forms import TeamForm


@app.route("/teams", methods=["GET"])
def teams_index():
    return render_template("teams/list.html", teams=Team.query.all())


@app.route("/teams/new/")
@login_required
def teams_form():
    return render_template("teams/new.html", form=TeamForm())


# @app.route("/teams/<team_id>/", methods=["POST"])
# @login_required
# def players_change_position(player_id):

#     p = Player.query.get(player_id)
#     p.position = request.form.get("position")
#     db.session().commit()
  
#     return redirect(url_for("players_index"))


@app.route("/teams/", methods=["POST"])
@login_required
def teams_create():
    form = TeamForm(request.form)

    if not form.validate():
        return render_template("teams/new.html", form=form)
        
    t = Team(form.name.data)    

    db.session().add(t)
    db.session().commit()

    return redirect(url_for("teams_index"))

@app.route("/teams/statistics", methods=["GET"])
def teams_statistics():
    return render_template("teams/statistics.html", 
            goals=Team.team_goals(),
            penalties=Team.team_penalties())

