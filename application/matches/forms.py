from flask_wtf import FlaskForm
from wtforms import StringField, validators, SelectField
from wtforms.fields.html5 import DateField
from application.teams.models import Team


class MatchForm(FlaskForm):
    match_date = DateField("Match date", format='%Y-%m-%d')

    team_choices = Team.all_team_data()
    home_team = SelectField(u'Home team', choices=team_choices, coerce=int)
    away_team = SelectField(u'Away team', choices=team_choices, coerce=int)

    # def validate_team_name(form, field):
    #     sel_team_name = str(dict(field.choices).get(field.data))
    #     a = Team.find_team_id(sel_team_name)
    #     if not a:
    #         raise validators.ValidationError('Team name must match with team names already in database (list teams to see options)')

 
    class Meta:
        csrf = False