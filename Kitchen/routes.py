from flask import Blueprint, render_template
import db

kitchen_bp = Blueprint("kitchen",__name__)

@kitchen_bp.route("/kitchen")
def kitchen():
    order = db.allorders()
    return render_template("kitchen.html", items=order)

@kitchen_bp.route("/completed/<tno>")
def completed(tno):
    db.removeorder(tno)
    order = db.allorders()
    return render_template("kitchen.html", items=order)