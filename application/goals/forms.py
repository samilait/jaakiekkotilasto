from flask_wtf import FlaskForm
from wtforms import StringField, validators, SelectField, DateTimeField
from application.players.models import Player


class GoalForm(FlaskForm):

    time = DateTimeField("Time (mm:ss)", format='%M:%S')

    scorer_name = SelectField(u'Scorer', coerce=int)

    assistant_1_name = SelectField(u'Assistant 1', coerce=int)

    assistant_2_name = SelectField(u'Assistant 2', coerce=int)

    def __init__(self, team_id, *args, **kwargs):
        FlaskForm.__init__(self, *args, **kwargs)
        self.team_id = team_id
        self.scorer_name.choices = Player.team_players(team_id)
        self.assistant_1_name.choices = Player.team_players(team_id)
        self.assistant_2_name.choices = Player.team_players(team_id)
 
    class Meta:
        csrf = False