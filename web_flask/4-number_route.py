#!/usr/bin/python3
"""This module starts a web application listening on 0.0.0.0, port 5000."""

from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    """Displays Hello HBNB."""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def display_text(text):
    """Displays C followed by text"""
    return "C " + text.replace('_', ' ')


@app.route("/python/", defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_with_text(text):
    """Displays Python followed by the value of text."""
    return "Python " + text.replace('_', ' ')


@app.route("/number/<int:n>")
def number(n):
    """Displays `n` which is an integer with some text"""
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
