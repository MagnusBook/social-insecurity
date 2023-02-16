from flask import Flask

from app.database import SQLite3
from config import Config

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

# Import the routes after the app is configured
from app import routes
