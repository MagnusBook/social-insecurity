#!/usr/bin/env python

"""Configured as entry point for the Social Insecurity application.

To start the application enter 'pdm run flask --debug run' in a terminal.

As an alternative, this file can also be run directly with 'pdm run python socialinsecurity.py'.
"""

from app import app

if __name__ == "__main__":
    app.run(debug=True)
