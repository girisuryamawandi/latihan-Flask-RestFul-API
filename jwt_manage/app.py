from flask import Flask, jsonify, request
from flask_restful import Api
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from models import db, User_jwt, Task
from resources import TaskListResource, TaskResource
from databaseSetting import Config

app = Flask(__name__)
app.config.from_object(Config)
api = Api(app)

# Setup the Flask-JWT-Extended extension
jwt = JWTManager(app)

db.init_app(app)


with app.app_context():
    db.create_all()

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"msg": "Username and password required"}), 400

    if User_jwt.query.filter_by(username=username).first():
        return jsonify({"msg": "User already exists"}), 400
    
    print(password)

    new_user = User_jwt(username=username)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"msg": "User created successfully"}), 201

# Endpoint for login to get JWT token
@app.route('/login', methods=['POST'])
def login():
    print(request.json.get('username', None))
    print(request.json.get('password', None))
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    # This is just an example, you should validate the username and password properly
    print('masuk')
    user = User_jwt.query.filter_by(username=username).first()
    
    if user is None or not user.check_password(password):
        return jsonify({"msg": "Bad username or password"}), 401
    

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)

# Protect a route with jwt_required, which requires a vali  d access token to be present in the request
@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    # Access the identity of the current user with get_jwt_identity
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

api.add_resource(TaskListResource, '/tasks')
api.add_resource(TaskResource, '/tasks/<int:task_id>')

if __name__ == '__main__':
    app.run(debug=True)