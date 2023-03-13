"""Provides a SQLite3 database extension for Flask.

This extension provides a simple interface to the SQLite3 database.

Example:
    from flask import Flask
    from app.database import SQLite3

    app = Flask(__name__)
    db = SQLite3(app)
"""

from __future__ import annotations

import os
import sqlite3
from typing import Any, Optional, cast

from flask import Flask, current_app


class SQLite3:
    """Provides a SQLite3 database extension for Flask.

    This class provides a simple interface to the SQLite3 database.
    It also initializes the database if it does not exist yet.

    Example:
        from flask import Flask
        from app.database import SQLite3

        app = Flask(__name__)
        db = SQLite3(app)

        # Use the database
        # db.query("SELECT * FROM Users;")
        # db.query("SELECT * FROM Users WHERE id = 1;", one=True)
        # db.query("INSERT INTO Users (name, email) VALUES ('John', 'test@test.net');")
    """

    def __init__(self, app: Optional[Flask] = None, path: Optional[str] = None) -> None:
        if app is not None:
            self.init_app(app, path)

    def init_app(self, app: Flask, path: Optional[str] = None) -> None:
        """Initalizes the application with the extension."""
        self._path = path or cast(str, app.config.setdefault("SQLITE3_DATABASE", "sqlite3.db"))
        self._connection: Optional[sqlite3.Connection] = None

        self._register(app)
        app.before_first_request(self._init_database)
        app.before_request(self._open_connection)
        app.teardown_appcontext(self._close_connection)

    @property
    def connection(self) -> sqlite3.Connection:
        """Returns the connection to the SQLite3 database."""
        if not self._connection:
            self._connection = sqlite3.connect(self._path)
            self.connection.row_factory = sqlite3.Row
        return self._connection

    def query(self, query: str, one: bool = False) -> Any:
        """Queries the database and returns the result.'

        params:
            query: The SQL query to execute.
            one: Whether to return a single row or a list of rows.

        returns: A single row, a list of rows or None.

        """
        cursor = self.connection.execute(query)

        if one:
            response = cursor.fetchone()
        else:
            response = cursor.fetchall()

        cursor.close()
        self.connection.commit()
        return response

    # TODO: Add more specific query methods to simplify code

    def _register(self, app: Flask) -> None:
        if not hasattr(app, "extensions"):
            app.extensions = {}

        if "sqlite3" not in app.extensions:
            app.extensions["sqlite3"] = self
        else:
            raise RuntimeError("Flask extension already initialized")

    def _init_database(self) -> None:
        if not os.path.exists(current_app.instance_path + self._path):
            with current_app.open_resource("schema.sql", mode="r") as file:
                self.connection.executescript(file.read())
                self.connection.commit()

    def _open_connection(self) -> None:
        if not self._connection:
            self._connection = sqlite3.connect(self._path)
            self.connection.row_factory = sqlite3.Row

    def _close_connection(self, exception: Optional[BaseException] = None) -> None:
        if self._connection:
            self._connection = self._connection.close()
