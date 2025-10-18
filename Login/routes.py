from flask import Blueprint, render_template, session, request

login_bp = Blueprint("login",__name__)

@login_bp.route("/")
def login():
    return render_template("login.html")

@login_bp.route("/submit", methods = ["GET","POST"])
def submit():
    if request.form.get("username") == "admin" and request.form.get("password") == "admin":
        session["user"]="admin"
        return render_template("dashboard.html")
    return render_template("login.html")
