from functools import wraps
from flask import flash, session,redirect,url_for,render_template   

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user' not in session:
            flash('Login required')
            return render_template("login.html")
        return f(*args, **kwargs)
        
    return decorated_function