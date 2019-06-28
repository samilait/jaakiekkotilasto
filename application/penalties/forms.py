from flask_wtf import FlaskForm
from wtforms import StringField, validators, SelectField, DateTimeField
from application.players.models import Player
from application.penaltycodes.models import PenaltyCode


class PenaltyForm(FlaskForm):

    start_time = DateTimeField("Start Time (mm:ss)", format='%M:%S')
    length = StringField("Length (min: 2, 4, 5, 10, 20)")

    def validate_length(form, field):
        if (str(field.data)).isdigit():
            int_length = int(str(field.data))
            allowed = [2, 4, 5, 10, 20]
            if not (int_length in allowed):
                raise validators.ValidationError('Length must be: 2, 4, 5, 10, 20')
        else:
            raise validators.ValidationError('Value must be numeric')
            
    reciever_name = SelectField(u'Receiver', coerce=int)
    penaltycode = SelectField(u'Penalty type', coerce=int)

    def __init__(self, team_id, *args, **kwargs):
        FlaskForm.__init__(self, *args, **kwargs)
        self.team_id = team_id
        self.reciever_name.choices = Player.team_players(team_id)
        self.penaltycode.choices = PenaltyCode.all_penaltycode_data()
 
    class Meta:
        csrf = False