from application import app, db, login_required
from flask import redirect, render_template, request, url_for
from flask_login import current_user

from application.penalties.models import Penalty
from application.penalties.forms import PenaltyForm
from application.players.models import Player
from application.teams.models import Team
from application.matches.models import Match
from application.penaltycodes.models import PenaltyCode


@app.route("/penalties/new/<match_id>/<team_name>", methods=["POST"])
@login_required(role="ADMIN")
def penalties_form(match_id, team_name):
    team_id = Team.find_team_id(team_name)
    return render_template("penalties/new.html", form=PenaltyForm(team_id[0]), match_id=match_id, team_id=team_id[0])


@app.route("/penalties/<match_id>/<team_id>/", methods=["POST"])
@login_required(role="ADMIN")
def penalties_add_penalty(match_id, team_id):

    form = PenaltyForm(team_id, request.form)

    if not form.validate():
        return render_template("matches/list.html", form=form)
    
    start_time = form.start_time.data
    length = form.length.data
    end_time = "20:00"

    sel_reciever_name = str(dict(form.reciever_name.choices).get(form.reciever_name.data))
    reciever_id = Player.find_player_id(sel_reciever_name)

    sel_penalty_desc_code = str(dict(form.penaltycode.choices).get(form.penaltycode.data))
    sel_penaltycode = (sel_penalty_desc_code[-4:])[:3]
    penalty_id = PenaltyCode.find_penaltycode_id(sel_penaltycode)

    p = Penalty(match_id, team_id, start_time, length, end_time, reciever_id[0], penalty_id[0])

    db.session().add(p)
    db.session().commit()

    return redirect(url_for("matches_index"))

