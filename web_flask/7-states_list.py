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
    """Closes the SQLAlchemy Session."""
    storage.close()


@app.route('/states_list')
def HTMLPage():
    """Displays a HTML page of list of states inside the tag body."""
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
