from flask_wtf import FlaskForm
from wtforms import StringField, validators, SelectField
from application.teams.models import Team


class PlayerForm(FlaskForm):
    name = StringField("Name (First Surname)", [validators.InputRequired()])

    def validate_name(form, field):
        first_last = str(field.data).split(" ")
        if first_last.__len__() < 2:
            raise validators.ValidationError('Input: Firstname Lastname (space in between)')
        elif len(first_last[0]) < 2 or len(first_last[1]) < 2:
            raise validators.ValidationError('First or last name must be at least 2 characters')

    number = StringField("Number")

    def validate_number(form, field):
        int_number = int(field.data)
        if not (0 < int_number and int_number < 100):
            raise validators.ValidationError('Number must be between 1 and 99')

    position = StringField("Position (VL,OL,KH,VP,OP,MV)")

    def validate_position(form, field):
        positions = ['VL', 'OL', 'KH', 'VP', 'OP', 'MV']
        if not (str(field.data) in positions):
            raise validators.ValidationError('Position must be: VL,OL,KH,VP,OP,MV')

    team_choices = Team.all_team_data()
    team_name = SelectField(u'Team name', choices=team_choices, coerce=int)

    def validate_team_name(form, field):
        sel_team_name = str(dict(field.choices).get(field.data))
        a = Team.find_team_id(sel_team_name)
        if not a:
            raise validators.ValidationError('Team name must match with team names already in database (list teams to see options)')

 
    class Meta:
        csrf = False