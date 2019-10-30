from marshmallow import Schema, fields
from marshmallow.validate import Length, Range

class UserSchema(Schema):
    class Meta:
        fields = ('id', 'username', 'created_at')

class TaskSchema(Schema):
    user = fields.Nested(UserSchema)
    
    class Meta: 
        fields = ('id', 'title', 'description', 'deadline', 'user')

class ParamsTaskSchema(Schema):
    title = fields.Str(required=True, validate=Length(max=50))
    description = fields.Str(required=True, validate=Length(max=500))
    deadline = fields.DateTime(required=True)

class ParamsCreateTaskSchema(ParamsTaskSchema):
    user_id = fields.Int(required=True, validate=Range(min=1))

class ParamsUpdateTaskSchema(ParamsTaskSchema):
    pass

task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)

create_task_schema = ParamsCreateTaskSchema()
update_task_schema = ParamsUpdateTaskSchema()