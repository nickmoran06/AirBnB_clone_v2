#!/usr/bin/python3
# Script that starts a flask web application

from flask import Flask, render_template
from models import storage
from models import *
app = Flask(__name__)


@app.teardown_appcontext
def Close_session(exception=None):
    """Teardown to close the session storage"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def Cities_states():
    """Method to display an specific HTML page"""
    states_list = list(storage.all("State").values())
    states = sorted(states_list, key=lambda state: state.name)
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
