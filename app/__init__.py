"""Provides the app package for the Social Insecurity application. The package contains the Flask app and all of the extensions and routes."""

import os

from flask import Flask

from app.config import Config
from app.database import SQLite3

# from flask_login import LoginManager
# from flask_bcrypt import Bcrypt
# from flask_wtf.csrf import CSRFProtect

# Instantiate and configure the app
app = Flask(__name__)
app.config.from_object(Config)

# Instantiate the sqlite database extension
sqlite = SQLite3(app)

# TODO: Handle login management better, maybe with flask_login?
# login = LoginManager(app)

# TODO: The passwords are stored in plaintext, this is not secure at all. I should probably use bcrypt or something
# bcrypt = Bcrypt(app)

# TODO: The CSRF protection is not working, I should probably fix that
# csrf = CSRFProtect(app)


@app.before_first_request
def create_upload_folder():
    if not os.path.exists(app.config["UPLOAD_PATH"]):
        os.makedirs(app.config["UPLOAD_PATH"])


# Import the routes after the app is configured
from app import routes  # noqa: E402,F401
