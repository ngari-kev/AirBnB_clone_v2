#!/usr/bin/python3
"""This module starts a web application."""

from flask import Flask, render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello_HBNB():
    """Returns Hello HBNB."""
    return "Hello HBNB!"


@app.route("/hbnb")
def hello():
    """Returns HBNB."""
    return "HBNB"


@app.route("/c/<text>")
def text(text):
    """Return C followed by the value of text"""
    text = text.replace('_', ' ')
    return "C %s" % text


@app.route("/python/", defaults={'text': 'is_cool'})
@app.route("/python/<text>")
def python(text):
    """Returns Python followed by the value of text."""
    text = text.replace('_', ' ')
    return "Python {}".format(text)


@app.route("/number/<int:n>")
def number(n):
    """Returns n which is an integer with some text"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>")
def html_number(n):
    """Returns n which is an integer with some text."""
    return render_template('5-number.html', num=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
