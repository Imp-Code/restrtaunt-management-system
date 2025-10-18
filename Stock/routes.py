from flask import Blueprint, render_template, request
import db

stock_bp = Blueprint("stock",__name__)

@stock_bp.route("/stock",methods=["GET","POST"])
def stock():
    item = db.allstock()
    return render_template("stock.html", items = item)

@stock_bp.route("/update",methods=["GET","POST"])
def update():
    item = request.form.get("item")
    quantity = request.form.get("quantity")
    status = request.form.get("status")
    command = request.form.get("command")

    if command == "add":
        db.addstock(item,quantity,status)
    if command == "remove":
        db.removestock(item)

    itemtwo = db.allstock() 
    return render_template("stock.html", items = itemtwo)