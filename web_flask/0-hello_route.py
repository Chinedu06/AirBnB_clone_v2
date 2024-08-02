#!/usr/bin/python3
"""
This module starts a Flask web application that listens on 0.0.0.0, port 5000
and displays “Hello HBNB!” on the root route.
"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Displays 'Hello HBNB!' at the root route.
    """
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

