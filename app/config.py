"""Provides the configuration for the Social Insecurity application.

This file is used to set the configuration for the application.

Example:
    from flask import Flask
    from app.config import Config

    app = Flask(__name__)
    app.config.from_object(Config)

    # Use the configuration
    secret_key = app.config["SECRET_KEY"]
"""

import os


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "secret"  # TODO: Use this with wtforms
    SQLITE3_DATABASE = "app/sqlite3.db"
    UPLOAD_PATH = "app/static/uploads"
    ALLOWED_EXTENSIONS = {}  # TODO: Might use this at some point, probably don't want people to upload any file type
    WTF_CSRF_ENABLED = False  # TODO: I should probably implement this wtforms feature, but it's not a priority
