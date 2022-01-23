from flask import Blueprint, request, jsonify

math = Blueprint('math', __name__)

@math.route('/api/addition', methods=['GET'])
def addition():
    a = request.args.get('a', default=1, type=float)
    b = request.args.get('b', default=1, type=float)
    resultat = a + b
    return f'addition ! {resultat}'

@math.route('/api/division/<a>/<b>', methods=['GET'])
def division(a, b):
    a = int(a)
    b = int(b)
    resultat = a / b
    return f'division : {resultat}'

@math.route('/api/soustraction', methods=['DELETE'])
def soustraction():
    return "ok"


