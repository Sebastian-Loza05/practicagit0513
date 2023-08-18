from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')

def hello():
    return '<h1>Hello, World dos!</h1>'

@app.route('/multiplicar/<param1>/<param2>')
def multiplicar(param1, param2):
    valor = int(param1) * int(param2)
    return str(valor)
