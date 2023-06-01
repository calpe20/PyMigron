from flask import session
from flask import jsonify
from functools import wraps


def verify_token(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = 'hola'
        if token == 'hola':
            return f(*args, **kwargs)
        else:
            return jsonify({'error': 'Token not valid!'})
    return decorated_function