#!/usr/bin/python3
"""
Starts a Flask web application
"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBTN():
    """Returns Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Returns HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def C_text(text):
    """Display “C ”, followed by the value of the text variable"""
    return 'C ' + text.replace("_", " ")


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is_cool"):
    """Display “Python ”, followed by the value of the text variable"""
    return 'Python ' + text.replace("_", " ")


@app.route('/number/<int:n>', strict_slashes=False)
def integer(n):
    """Display “n is a number” only if n is an integer"""
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def rendering_HTML(n):
    """Display a HTML page only if n is an integer"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def type_number(n):
    """display a HTML page only if n is an integer"""
    if n % 2 == 0:
        typ = 'even'
    else:
        typ = 'odd'
    return render_template('6-number_odd_or_even.html', n=n, typ=typ)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
