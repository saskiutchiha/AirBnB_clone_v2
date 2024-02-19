#!/usr/bin/python3 
from flask import Flask
"""Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'
"""
app = Flask(__name__)
@app.route("/")
def helllo():
    return "Hello HBNB!"
if __name__ == "__main__":
 app.run(host="0.0.0.0",port=5000)
