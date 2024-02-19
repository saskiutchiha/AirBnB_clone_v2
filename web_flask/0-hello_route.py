#!/usr/bin/python3 
from flask import Flask
"""Starts Flask web app
Listening on 0.0.0.0:5000
Route '/' displays "Hello HBNB!"
"""

app = Flask(__name__)
@app.route("/")
def helllo():
    """
    This function is associated with the route '/'.
    When this route is accessed, it returns the string 'Hello HBNB!'
    """
    return "Hello HBNB!"
if __name__ == "__main__":
 app.run(host="0.0.0.0",port=5000)
