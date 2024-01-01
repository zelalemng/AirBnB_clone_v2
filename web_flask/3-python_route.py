#!/usr/bin/python3
"""
start web flask application.
"""
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_route():
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb_route():
    return "HBNB"

@app.route('/c/is_fun', strict_slashes=False)
def c_is_fun_route():
    return "C is fun"

@app.route('/c/cool', strict_slashes=False)
def c_cool_route():
    return "C cool"

@app.route('/c', strict_slashes=False)
def c_route():
    return ('c')

@app.route('/python/is_magic', strict_slashes=False)
def Python_is_magic_route():
    return "Python is magic"

@app.route('/python', strict_slashes=False)
def Python_is_cool_route():
    return "Python is cool"

@app.route('/python/<text>', strict_slashes=False)
def is_cool_route():
    return "is cool"

@app.route('/python/', strict_slashes=False)
def Python_is_cool_route():
    return "Python is cool"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
