from application import app, db, login_required
from flask import redirect, render_template, request, url_for
from flask_login import current_user

from application.matches.models import Match
from application.matches.forms import MatchForm
from application.teams.models import Team
import babel


@app.route("/matches", methods=["GET"])
def matches_index():
    return render_template("matches/list.html", matches=Match.all_matches())


@app.route("/matches/new/")
@login_required(role="ADMIN")
def matches_form():
    return render_template("matches/new.html", form = MatchForm())


# @app.route("/players/<player_id>/", methods=["POST"])
# @login_required
# def players_change_position(player_id):

#     p = Player.query.get(player_id)
#     p.position = request.form.get("position")

#     # if t.account_id != current_user.id:
#     #     # tee jotain, esim. 
#     #     return login_manager.unauthorized()
    
#     db.session().commit()
  
#     return redirect(url_for("players_index"))


@app.route("/matches/", methods=["POST"])
@login_required(role="ADMIN")
def matches_create():
    form = MatchForm(request.form)

    if not form.validate():
        return render_template("matches/new.html", form = form)
    
    home_team_name = str(dict(form.home_team.choices).get(form.home_team.data))
    away_team_name = str(dict(form.away_team.choices).get(form.away_team.data))

    home_team_id = Team.find_team_id(home_team_name)
    away_team_id = Team.find_team_id(away_team_name)

    m = Match(form.match_date.data, home_team_id[0], away_team_id[0])    
 
    db.session().add(m)
    db.session().commit()

    m.match_accounts.append(current_user)
    db.session().commit()

    return redirect(url_for("matches_index"))


def format_datetime(value):
    format = "y-MM-d"
    p_date = babel.dates.parse_date(value)
    return babel.dates.format_datetime(p_date , format, tzinfo=None)


app.jinja_env.filters['datetime'] = format_datetime
