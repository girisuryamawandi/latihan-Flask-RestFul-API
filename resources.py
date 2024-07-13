# resources.py
from flask_restful import Resource, reqparse
from models import Task, db

task_parser = reqparse.RequestParser()
task_parser.add_argument('title', type=str, required=True, help='Title is required')
task_parser.add_argument('description', type=str)
task_parser.add_argument('done', type=bool)

class TaskListResource(Resource):
    def get(self):
        tasks = Task.query.all()
        return [{'id': task.id, 'title': task.title, 'description': task.description, 'done': task.done} for task in tasks]

    def post(self):
        args = task_parser.parse_args()
        task = Task(title=args['title'], description=args['description'], done=args['done'])
        db.session.add(task)
        db.session.commit()
        return {'id': task.id, 'title': task.title, 'description': task.description, 'done': task.done}, 201

class TaskResource(Resource):
    def get(self, task_id):
        task = Task.query.get_or_404(task_id)
        return {'id': task.id, 'title': task.title, 'description': task.description, 'done': task.done}

    def put(self, task_id):
        args = task_parser.parse_args()
        task = Task.query.get_or_404(task_id)
        task.title = args['title']
        task.description = args['description']
        task.done = args['done']
        db.session.commit()
        return {'id': task.id, 'title': task.title, 'description': task.description, 'done': task.done}

    def delete(self, task_id):
        task = Task.query.get_or_404(task_id)
        db.session.delete(task)
        db.session.commit()
        message = f'delete {task_id} done'
        print(message)
        return 'deleted', 204
