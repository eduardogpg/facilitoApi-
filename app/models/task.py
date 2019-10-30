import logging
import datetime

from . import db

from sqlalchemy import desc, asc
from sqlalchemy.event import listen

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    tasks = db.relationship("Task")
    username = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False, default=db.func.current_timestamp())
    
class Task(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User', back_populates='tasks')
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.Text, nullable=False)
    deadline = db.Column(db.DateTime(), nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False, default=db.func.current_timestamp())

    def __str__(self):
        return self.title

    @classmethod
    def new(cls, title, description, user_id, deadline):
        return Task(title=title, description=description, user_id=user_id, deadline=deadline)

    @classmethod
    def ordered_by_created_at(cls, order='desc', page=1, per_page=10):
        sort = asc(Task.created_at) if order == "desc" else desc(Task.created_at)
        return Task.query.order_by(sort).paginate(page, per_page=per_page).items

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except:
            return False

    def delete(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except:
            return False

def insert_users(*args, **kwargs):
    db.session.add(User(username='codi'))

    db.session.commit()

listen(User.__table__, 'after_create', insert_users)
