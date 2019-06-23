from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required

from application.penaltycodes.models import PenaltyCode
from application.penaltycodes.forms import PenaltycodeForm


@app.route("/penaltycodes", methods=["GET"])
def penaltycodes_index():
    return render_template("penaltycodes/list.html", penaltycodes=PenaltyCode.query.all())


@app.route("/penaltycodes/new/")
@login_required
def penaltycodes_form():
    return render_template("penaltycodes/new.html", form=PenaltycodeForm())

@app.route("/penaltycodes/", methods=["POST"])
@login_required
def penaltycodes_create():
    form = PenaltycodeForm(request.form)

    if not form.validate():
        return render_template("penaltycodes/new.html", form=form)
        
    p = PenaltyCode(form.code.data, form.description.data)

    db.session().add(p)
    db.session().commit()

    return redirect(url_for("penaltycodes_index"))
