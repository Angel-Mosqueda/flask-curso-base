# from my_app import app
from flask import Blueprint

hello = Blueprint('hello', __name__)

@hello.route('/')
@hello.route('/hello1')
def fhello():
    return "Hola mundo 1"