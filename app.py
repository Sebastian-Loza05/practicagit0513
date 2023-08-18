from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')

def hello():
    return '<h1>Hello, World1!</h1>'

@app.route('/sumar/<param1>/<param2>')
def sumar(param1, param2):
    pam1 = int(param1)
    pam2 = int(param2)

    return str(pam1 + pam2)
