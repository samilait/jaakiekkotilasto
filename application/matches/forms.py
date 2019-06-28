from flask_wtf import FlaskForm
from wtforms import StringField, validators, SelectField
from wtforms.fields.html5 import DateField
from application.teams.models import Team


class MatchForm(FlaskForm):

    id = StringField("Match ID")
    match_date = DateField("Match date", format='%Y-%m-%d')

    team_choices = Team.all_team_data()
    home_team = SelectField(u'Home team', choices=team_choices, coerce=int)
    away_team = SelectField(u'Away team', choices=team_choices, coerce=int)
 
    class Meta:
        csrf = False