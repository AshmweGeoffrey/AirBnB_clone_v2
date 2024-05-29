#!/usr/bin/python3

from flask import Flask

app=Flask(__name__)


@app.route('/')
def hello():
    """ /: display Hello HBNB!"""
    
    return "Hello HBNB!"
@app.route('/hbnb')
def hello1():
    """ /hbnb: display “HBNB” """
    return "HBNB!"
@app.route('/c/<text>')
def hello2(text):
    """ /c/<text>: display “C ” followed by the value of the text variable (replace underscore _ symbols with a space ) """
    return "C {}".format(text.replace('_', ' '))
if __name__=="__main__":
    app.run(host='0.0.0.0',port=5000 ,debug=True)
