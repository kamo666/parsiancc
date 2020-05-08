from flask import current_app, request, jsonify
from functools import wraps
import jwt

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'token' in request.headers:
            token = request.headers['token']
        if not token:
           return jsonify({'message' : 'Token is missing!'}), 403
        try:
            data = jwt.decode(token, current_app.config['SECRET_KEY'])
        except:
            return jsonify({'message' : 'Token is invalid!'}), 403
        return f(*args, **kwargs)
    return decorated
