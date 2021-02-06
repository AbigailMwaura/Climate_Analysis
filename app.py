from flask import flask
@app.route('/')
def hello_world():
    return 'Hello world'