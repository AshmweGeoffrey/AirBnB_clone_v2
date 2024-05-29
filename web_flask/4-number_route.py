#!/usr/bin/python3

from flask import Flask

app=Flask(__name__)

@app.route('/')
def hello():
    """ /: display “Hello HBNB!” """
    return "Hello HBNB"
@app.route('/hbnb')
def hello1():
    """ /hbnb: display “HBNB” """
    return "HBNB"
@app.route('/c/<text>')
def hello2(text):
    """ /c/<text>: display “C ”, followed by the value of the text variable (replace underscore _ symbols with a space ) """
    return "C {}".format(text.replace("_"," "))
@app.route('/python')
@app.route('/python/<text>')
def hello3(text="is cool"):
    """ /python/<text>: display “Python ”, followed by the value of the text variable (replace underscore _ symbols with a space )"""
    return "Python {}".format(text.replace("_"," "))
@app.route('/number/<int:n>')
def hello4(n):
    if type(n) is int:
        return "{:d}".format(n)
if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=5000)
