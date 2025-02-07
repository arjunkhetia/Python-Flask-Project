# Python (Flask) Server - Project   ![Version][version-image]

![Linux Build][linuxbuild-image]
![Windows Build][windowsbuild-image]
![NSP Status][nspstatus-image]
![Test Coverage][coverage-image]
![Dependency Status][dependency-image]
![devDependencies Status][devdependency-image]

The quickest way to get start with Python (Flask) - Server, just clone the project:

```bash
$ git clone https://github.com/arjunkhetia/Python-Flask-Project.git
```

Install dependencies:

```bash
$ pip install -r requirements.txt

OR

$ python3 -m pip install -r requirements.txt --break-system-packages
```

Start Flask Server app at `http://localhost:5000/`:

```bash
$ python server.py

OR

$ python3 server.py
```

# Flask

Flask is a lightweight WSGI web application framework. It is designed to make getting started quick and easy, with the ability to scale up to complex applications. (WSGI is the Web Server Gateway Interface. It is a specification that describes how a web server communicates with web applications, and how web applications can be chained together to process one request.)

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
```

# Flask-Compress

Flask-Compress allows you to easily compress your Flask application's responses with gzip, deflate, brotli or zstd. Flask-Compress both adds the various headers required for a compressed response and compresses the response data. This makes serving compressed static files extremely easy.

```python
from flask_compress import Compress

# Initializing flask app
app = Flask(__name__)

# Initialize Flask-Compress
compress = Compress()
compress.init_app(app)
```

# Flask-CORS

A Flask extension for handling Cross Origin Resource Sharing (CORS), making cross-origin AJAX possible. By default, submission of cookies across domains is disabled due to the security implications. 

```python
from flask_cors import CORS

# Initializing flask app
app = Flask(__name__)
CORS(app)

# Resource specific CORS
# cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
```

# Flask-MonitoringDashboard

A dashboard for automatic monitoring of Flask web-services. The Flask Monitoring Dashboard is an extension for Flask applications that offers four main functionalities:

- Monitor the performance and utilization
- Profile requests and endpoints
- Collect extra information about outliers
- Collect additional information about our Flask-application

```python
import flask_monitoringdashboard as dashboard

app = Flask(__name__)
dashboard.config.init_from(file='config/dashboard-config.cfg')

# Make sure that you first configure the dashboard, before binding it to your Flask application
dashboard.bind(app)
app.run()
```

dashboard-config.cfg - 

```cfg
[dashboard]
APP_VERSION=1.0
GIT=https://github.com/arjunkhetia/Python-Flask-Project/.git/
BLUEPRINT_NAME=dashboard
CUSTOM_LINK=dashboard
MONITOR_LEVEL=3
OUTLIER_DETECTION_CONSTANT=2.5
SAMPLING_PERIOD=20
ENABLE_LOGGING=True
BRAND_NAME=Flask Monitoring Dashboard
TITLE_NAME=Flask-MonitoringDashboard
DESCRIPTION=Automatically monitor the evolving performance of Flask/Python web services
SHOW_LOGIN_BANNER=True
SHOW_LOGIN_FOOTER=True

[authentication]
USERNAME=admin
PASSWORD=admin
GUEST_USERNAME=guest
GUEST_PASSWORD=['dashboardguest!', 'second_pw!']
SECURITY_TOKEN=13579925565507531

[database]
DATABASE=sqlite:///flask_monitoringdashboard.db

[visualization]
TIMEZONE=Asia/Kolkata
COLORS={'main':'[0,97,255]', 'static':'[255,153,0]'}
```

[version-image]: https://img.shields.io/badge/Version-1.0.0-orange.svg
[linuxbuild-image]: https://img.shields.io/badge/Linux-passing-brightgreen.svg
[windowsbuild-image]: https://img.shields.io/badge/Windows-passing-brightgreen.svg
[nspstatus-image]: https://img.shields.io/badge/nsp-no_known_vulns-blue.svg
[coverage-image]: https://img.shields.io/coveralls/expressjs/express/master.svg
[dependency-image]: https://img.shields.io/badge/dependencies-up_to_date-brightgreen.svg
[devdependency-image]: https://img.shields.io/badge/devdependencies-up_to_date-yellow.svg