from flask import Flask

from Login.routes import login_bp
from Dashboard.routes import dashboard_bp
from WaiterForm.routes import waiter_bp
from Kitchen.routes import kitchen_bp
from Stock.routes import stock_bp


app = Flask(__name__)
app.secret_key = "dkjr234hrlk2jl4lhkj23jdslkjfhh42kjhdsflhvjhw44hj23hkj4jkhl23jh423jhk4hjk23hjk4j32khjkh"

app.register_blueprint(login_bp)
app.register_blueprint(dashboard_bp)
app.register_blueprint(waiter_bp)
app.register_blueprint(kitchen_bp)
app.register_blueprint(stock_bp)


app.run(debug = True)



