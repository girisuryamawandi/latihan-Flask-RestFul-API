from flask import Flask, jsonify, request
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from models import db, Users, Task
from resources import TaskListResource, TaskResource
from databaseSetting import Config
from auth import basic_auth_required

app = Flask(__name__)
app.config.from_object(Config)
api = Api(app)

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

    if Users.query.filter_by(username=username).first():
        return jsonify({"msg": "User already exists"}), 400

    new_user = Users(username=username)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"msg": "User created successfully"}), 201

@app.route('/protected', methods=['GET'])
@basic_auth_required
def protected():
    return jsonify({"msg": "You have access to this resource"}), 200

api.add_resource(TaskListResource, '/tasks')
api.add_resource(TaskResource, '/tasks/<int:task_id>')

if __name__ == '__main__':
    app.run(debug=True)