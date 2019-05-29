from flask_wtf import FlaskForm
from wtforms import StringField


class PlayerForm(FlaskForm):
    name = StringField("Name (First Surname)")
    number = StringField("Number")
    position = StringField("Position (VL,OL,KH,VP,OP,MV)")
 
    class Meta:
        csrf = False