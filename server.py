from flask import Flask, render_template
# from utilities.logger import logger
import flask_monitoringdashboard as dashboard
# from random import randint
from flask_compress import Compress
from flask_cors import CORS
from routes import register_routes
import os

compress = Compress()
SECRET_KEY = os.urandom(32)

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
CORS(app)
compress.init_app(app)

dashboard.config.init_from(file='config/dashboard-config.cfg')

# Add new graph to monitoring dashboard
# def numberOfNewCustomers():
#     return float(randint(1,5))
# numberOfNewCustomers_schedule = {'seconds': 10}
# dashboard.add_graph("Every 10 Seconds", numberOfNewCustomers, "interval", **numberOfNewCustomers_schedule)

# showing different logging levels
# logger.debug("debug log info")
# logger.info("Info log information")
# logger.warning("Warning log info")
# logger.error("Error log info")
# logger.critical("Critical log info")

@app.route("/")
def home():
    return render_template("index.html", data={
        'title': "Home Page",
        'message': "Welcome to Flask!",
        'array': ['1', '2', '3', '4', '5'],
        'user': "Arjun Khetia"
    })

# Register blueprints (modular routes)
register_routes(app)

dashboard.bind(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)  # Enables auto-reload