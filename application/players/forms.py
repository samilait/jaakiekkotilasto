from flask_wtf import FlaskForm
from wtforms import StringField, validators

class PlayerForm(FlaskForm):
    name = StringField("Name (First Surname)", [validators.InputRequired()])

    def validate_name(form, field):
        first_last = str(field.data).split(" ")
        if first_last.__len__() < 2:
            raise validators.ValidationError('Input: Firstname Lastname (space in between)')
        elif len(first_last[0]) < 2 or len(first_last[1]) < 2:
            raise validators.ValidationError('First or last name must be at least 2 characters')

    number = StringField("Number")
    position = StringField("Position (VL,OL,KH,VP,OP,MV)")
 
    class Meta:
        csrf = False