from flask import jsonify
from flask import request
from flask import Blueprint

from .responses import response
from .responses import bad_request

from .models.task import Task
from .schemas import task_schema, tasks_schema
from .schemas import create_task_schema
from .schemas import update_task_schema

api_v1 = Blueprint('api', __name__, url_prefix='/api/v1')

def set_task(function):
    def wrap(*args, **kwargs):
        task_id = kwargs.get('id', 0)
        task = Task.query.filter_by(id=task_id).first()

        if task is None:
            return bad_request()
        
        return function(task)

    wrap.__name__ = function.__name__
    return wrap

@api_v1.route('/tasks', methods=['GET'])
def get_tasks():
    page = int(request.args.get('page', 1))
    order = request.args.get('order', 'desc')
    show_users = request.args.get('user', 'false') == 'true'
    
    #tasks = Task.query.all()
    tasks = Task.ordered_by_created_at(order, page)
    
    return  response(tasks_schema.dump(tasks))

@api_v1.route('/tasks/<id>', methods=['GET'])
@set_task
def get_task(task):
    result = task_schema.dump(task, many=False)
    return response(result)

@api_v1.route('/tasks', methods=['POST'])
def create_task():
    json = request.get_json(force=True) 

    if create_task_schema.validate(json):
        return bad_request()

    user_id = int(json['user_id'])
    #Validate if user exists!
    task = Task.new(json['title'], json['description'], user_id, json['deadline'])

    if task.save():
        return response(task_schema.dump(task))
    
    return bad_request()

@api_v1.route('/tasks/<id>', methods=['PUT'])
def update_task(id):
    json = request.get_json(force=True)
    task = Task.query.filter_by(id=id).first()

    if create_task_schema.validate(json):
        return bad_request()

    task.title = json.get('title', task.title)
    task.description = json.get('description', task.description)
    task.deadline = json.get('deadline', task.deadline)
    
    if task.save():
        return response(task_schema.dump(task))

@api_v1.route('/tasks/<id>', methods=['DELETE'])
@set_task
def delete_task(task):
    task.delete()
    
    return response(task.json())