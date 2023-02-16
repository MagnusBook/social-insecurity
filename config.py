import os

# contains application-wide configuration, and is loaded in __init__.py


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "secret"  # TODO: Use this with wtforms
    SQLITE3_DATABASE = "app/database.db"
    UPLOAD_PATH = "app/static/uploads"
    ALLOWED_EXTENSIONS = {}  # TODO: Might use this at some point, probably don't want people to upload any file type
    WTF_CSRF_ENABLED = False  # TODO: I should probably implement this wtforms feature, but it's not a priority
