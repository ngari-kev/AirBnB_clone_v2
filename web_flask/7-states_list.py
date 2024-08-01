#!/usr/bin/python3

"""Flask Web application"""

from flask import Flask, render_template
from models import storage
from models import *

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Lists states in alphabetical order on a HTML page"""
    states = sorted(list(storage.all("State").values()))
    return render_template('7-state_list.html', states=states)

@app.teardown_appcontext
def teardown(exception):
    """closes the storage upon teardown"""
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port = '5000')