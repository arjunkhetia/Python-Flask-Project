from flask import Flask
# from utilities.logger import logger
import flask_monitoringdashboard as dashboard
from random import randint

app = Flask(__name__)

dashboard.config.init_from(file='config/dashboard-config.cfg')

# Add new graph to monitoring dashboard
def numberOfNewCustomers():
    return float(randint(1,5))
numberOfNewCustomers_schedule = {'seconds': 10}
dashboard.add_graph("Every 10 Seconds", numberOfNewCustomers, "interval", **numberOfNewCustomers_schedule)


# showing different logging levels
# logger.debug("debug log info")
# logger.info("Info log information")
# logger.warning("Warning log info")
# logger.error("Error log info")
# logger.critical("Critical log info")

dashboard.bind(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)  # Enables auto-reload