from flask import Blueprint, render_template, request
import db

waiter_bp = Blueprint("waiter",__name__)

@waiter_bp.route("/waiter")
def waiter():
    return render_template("waiter.html")

@waiter_bp.route("/sendtokitchen", methods=["GET","POST"])
def sendtokitchen():
    tablenumber = request.form.get("tablenumber")
    orderdetails = request.form.get("orderdetails")
    priority = request.form.get("priority")

    db.addWaiterForm(tablenumber,orderdetails,priority)
    return render_template("waiter.html")