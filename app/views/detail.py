from flask import Flask, render_template, request, Blueprint
import sqlite3
from app.controllers import connection_close


bp = Blueprint("detail", __name__, template_folder="../templates")


@bp.route("/detail/<IdentityNumber>", methods=["GET", "POST"])
def detail_form(IdentityNumber):
        vt = sqlite3.connect('C:/Users/local-host/PycharmProjects/MitesFeedbackForm/grhyhh.sqlite')
        im = vt.cursor()
        im.execute("SELECT * FROM MitesFeedbackForm ")
        my_data = im.fetchall()
        list_for_dicts_from_db = []
        for index in my_data:
            data_dict_to_convert_from_db = dict()
            data_dict_to_convert_from_db["Name"] = index[0]
            data_dict_to_convert_from_db["Surname"] = index[1]
            data_dict_to_convert_from_db["IdentityNumber"] = index[2]
            data_dict_to_convert_from_db["Email"] = index[3]
            data_dict_to_convert_from_db["PhoneNumber"] = index[4]
            data_dict_to_convert_from_db["ApplicationDate"] = index[5]
            data_dict_to_convert_from_db["HowToApply"] = index[6]
            data_dict_to_convert_from_db["Freetext"] = index[7]
            list_for_dicts_from_db.append(data_dict_to_convert_from_db)
        ide_numb = f'{IdentityNumber}'
        sorted_data = dict()
        for x in list_for_dicts_from_db:
            if x["IdentityNumber"] == int(ide_numb):
                sorted_data = x
        if request.method == "GET":
            context_data = {
                "data": list_for_dicts_from_db,
                "IdentityNumber": IdentityNumber,
                "sorted_data": sorted_data
            }
            connection_close()
            return render_template("detail.html", **context_data)
