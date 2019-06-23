from flask_wtf import FlaskForm
from wtforms import StringField, validators, SelectField
from application.players.models import Player


class GoalForm(FlaskForm):

    # self.match_id = match_id
    # self.team_id = team_id
    # self.time = time
    # self.scorer_id = scorer_id
    # self.assistant_1_id = assistant_1_id
    # self.assistant_2_id = assistant_2_id

    # team_choices = Team.all_team_data()
    # team_name = SelectField(u'Team name', choices=team_choices, coerce=int)

    time = StringField("Time (mm:ss)")

    # scorer_choices = Player.team_players(team_id)
    scorer_name = SelectField(u'Scorer', coerce=int)

    # assistant_1_choices = Player.team_players(team_id)
    assistant_1_name = SelectField(u'Assistant 1', coerce=int)  # , choices=assistant_1_choices, coerce=int)

    # assistant_2_choices = Player.team_players(team_id)
    assistant_2_name = SelectField(u'Assistant 2', coerce=int)  # choices=assistant_2_choices, coerce=int)

    def __init__(self, team_id, *args, **kwargs):
        FlaskForm.__init__(self, *args, **kwargs)
        self.team_id = team_id
        self.scorer_name.choices = Player.team_players(team_id)
        self.assistant_1_name.choices = Player.team_players(team_id)
        self.assistant_2_name.choices = Player.team_players(team_id)
 
    class Meta:
        csrf = False