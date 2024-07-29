#!/usr/bin/python3
"""This module starts a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)
app.url_map.strict_slashes = False


# Declare a method to handle @app.teardown_appcontext
@app.teardown_appcontext
def teardown(exception):
    """Closes the SQLAlchemy Session.(Handle teardown)"""
    storage.close()


@app.route('/states/<id>')
@app.route('/states', defaults={'id': None})
def states(id):
    """Renders states."""
    states = storage.all(State)
    if id:
        id = 'State.' + id
    return render_template('9-states.html', states=states, id=id)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
