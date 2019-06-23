from flask_wtf import FlaskForm
from wtforms import StringField


class PenaltycodeForm(FlaskForm):
    code = StringField("Code")
    description = StringField("Description")

    class Meta:
        csrf = False
