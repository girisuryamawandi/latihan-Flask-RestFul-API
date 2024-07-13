# app.py
from flask import Flask
from flask_restful import Api
from models import db
from resources import TaskListResource, TaskResource
from databaseSetting import Config

app = Flask(__name__)
app.config.from_object(Config)
api = Api(app)
db.init_app(app)

# @app.before_first_request
# def create_tables():
#     db.create_all()
    
with app.app_context():
    db.create_all()

api.add_resource(TaskListResource, '/tasks')
api.add_resource(TaskResource, '/tasks/<int:task_id>')

if __name__ == '__main__':
    app.run(debug=True)