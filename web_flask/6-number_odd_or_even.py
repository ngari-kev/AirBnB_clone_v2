#!/usr/bin/python3
"""This module starts a web application listening on 0.0.0.0, port 5000."""

from flask import Flask, render_template


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


@app.route("/number_template/<int:n>")
def number_template(n):
    """Displays n which is an integer with some text."""
    return render_template('5-number.html', num=n)


@app.route("/number_odd_or_even/<int:n>")
def odd_or_even(n):
    """Invokes a html page depending on parity of n"""
    res = 'even' if n % 2 == 0 else 'odd'
    return render_template('6-number_odd_or_even.html', num=n, parity=res)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
