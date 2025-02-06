from flask import Flask
from utilities.logger import logger

app = Flask(__name__)


# showing different logging levels
logger.debug("debug log info")
logger.info("Info log information")
logger.warning("Warning log info")
logger.error("Error log info")
logger.critical("Critical log info")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)  # Enables auto-reload