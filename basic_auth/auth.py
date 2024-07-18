from functools import wraps
from flask import request, jsonify
from models import Users

def basic_auth_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not auth.username or not auth.password:
            return jsonify({"msg": "Missing or invalid credentials"}), 401
        
        user = Users.query.filter_by(username=auth.username).first()
        if user is None or not user.check_password(auth.password):
            return jsonify({"msg": "Invalid username or password"}), 401

        return f(*args, **kwargs)
    return decorated