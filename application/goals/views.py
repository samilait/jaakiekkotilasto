from application import app, db, login_required
from flask import redirect, render_template, request, url_for
from flask_login import current_user

from application.goals.models import Goal
from application.goals.forms import GoalForm
from application.players.models import Player
from application.teams.models import Team
from application.matches.models import Match


@app.route("/goals/new/<match_id>/<team_name>", methods=["POST"])
@login_required(role="ADMIN")
def goals_form(match_id, team_name):
    team_id = Team.find_team_id(team_name)
    return render_template("goals/new.html", form=GoalForm(team_id[0]), match_id=match_id, team_id=team_id[0])


@app.route("/goals/<match_id>/<team_id>/", methods=["POST"])
@login_required(role="ADMIN")
def goals_add_goal(match_id, team_id):

    form = GoalForm(team_id, request.form)  # , team_id)  # , team_id)

    if not form.validate():
        return render_template("goals/new.html", form=form)
    
    time = form.time.data

    sel_scorer_name = str(dict(form.scorer_name.choices).get(form.scorer_name.data))
    scorer_id = Player.find_player_id(sel_scorer_name)

    sel_assistant_1_name = str(dict(form.assistant_1_name.choices).get(form.assistant_1_name.data))
    assistant_1_id = Player.find_player_id(sel_assistant_1_name)

    sel_assistant_2_name = str(dict(form.assistant_2_name.choices).get(form.assistant_2_name.data))
    assistant_2_id = Player.find_player_id(sel_assistant_2_name)

    g = Goal(match_id, team_id, time, scorer_id[0], assistant_1_id[0], assistant_2_id[0])

    db.session().add(g)
    db.session().commit()

    m = Match.query.get(match_id)
    if str(m.home_team_id) == str(team_id):
        m.home_team_score = m.home_team_score + 1
    else:
        m.away_team_score = m.away_team_score + 1
    
    db.session().commit()

    return redirect(url_for("matches_index"))

