from flask import Flask, render_template, request, Blueprint
import sqlite3
from app.controllers import connection_close


bp = Blueprint("form", __name__, template_folder="../templates")


@bp.route("/", methods=["GET", "POST"])
def feedback_form():
    if request.method == 'POST':
        Name = request.form.get('Name')
        Surname = request.form.get('Surname')
        IdentityNumber = request.form.get("IdentityNumber")
        Email = request.form.get("Email")
        PhoneNumber = request.form.get("PhoneNumber")
        ApplicationDate = request.form.get("Application ate")
        HowToApply = request.form.get("HowToApply")
        Freetext = request.form.get("Freetext")
        vt = sqlite3.connect('grhyhh.sqlite')
        im = vt.cursor()
        im.execute(f"INSERT INTO MitesFeedbackForm(Name,Surname,IdentityNumber,Email,PhoneNumber,ApplicationDate,HowToApply,Freetext) VALUES(?,?,?,?,?,?,?,?)",(
        Name,
        Surname,
        IdentityNumber,
        Email,
        PhoneNumber,
        ApplicationDate,
        HowToApply,
        Freetext
    ))
    connection_close()
    return render_template("feedback_form.html")
