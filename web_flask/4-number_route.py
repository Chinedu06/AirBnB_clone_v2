#!/usr/bin/python3
"""
This module starts a Flask web application that listens on 0.0.0.0, port 5000
and has the following routes:
- /: displays "Hello HBNB!"
- /hbnb: displays "HBNB"
- /c/<text>: displays "C " followed by the value of the text variable
  (replaces underscores with spaces)
- /python/<text>: displays "Python " followed by the value of the text variable
  (replaces underscores with spaces). The default value of text is "is cool".
- /number/<n>: displays "<n> is a number" only if <n> is an integer
"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Displays 'Hello HBNB!' at the root route.
    """
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Displays 'HBNB' at the /hbnb route.
    """
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Displays 'C ' followed by the value of the text variable
    (replaces underscores with spaces) at the /c/<text> route.
    """
    return "C {}".format(text.replace('_', ' '))

@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    """
    Displays 'Python ' followed by the value of the text variable
    (replaces underscores with spaces) at the /python/<text> route.
    The default value of text is 'is cool'.
    """
    return "Python {}".format(text.replace('_', ' '))

@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    Displays '<n> is a number' only if <n> is an integer at the /number/<n> route.
    """
    return "{} is a number".format(n)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

