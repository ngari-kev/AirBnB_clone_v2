#!/usr/bin/python3
"""This module starts a web application."""

from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_HBNB():
    """Returns Hello HBNB."""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello():
    """Returns HBNB."""
    return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def text(text):
    """Return C followed by name"""
    text = text.replace('_', ' ')
    return "C %s" % text


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
