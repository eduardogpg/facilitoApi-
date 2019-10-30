from flask import Flask

app = Flask(__name__)

from .models import db
from .models.task import Task

from .views import api_v1

def create_app(enviroment):
    
    app.config.from_object(enviroment)
    app.register_blueprint(api_v1)

    with app.app_context():
        db.init_app(app)
        db.create_all()
    
    return app
