from flask_wtf import FlaskForm
from wtforms import StringField, validators, SelectField
from application.players.models import Player
from application.penaltycodes.models import PenaltyCode


class PenaltyForm(FlaskForm):

    start_time = StringField("Start Time (mm:ss)")
    length = StringField("Length (min)")

    reciever_name = SelectField(u'Receiver', coerce=int)
    penaltycode = SelectField(u'Penalty type', coerce=int)

    def __init__(self, team_id, *args, **kwargs):
        FlaskForm.__init__(self, *args, **kwargs)
        self.team_id = team_id
        self.reciever_name.choices = Player.team_players(team_id)
        self.penaltycode.choices = PenaltyCode.all_penaltycode_data()
 
    class Meta:
        csrf = False