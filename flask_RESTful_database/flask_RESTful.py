from flask import Flask, jsonify, render_template
from extensions import db
from models.model import StudentModel
from models.model import CourseModel
from models.model import EventModel
import json
from flask import request

from flask_restful import Resource, Api
from resources.course_resource import Course_one, All_courses, Course_two
from resources.student_resource import Student_one, All_students, Student_two
from resources.event_resource import Event_one, All_events, Event_two


app = Flask(__name__)

api = Api(app)


# DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'some-secret-string'

db.init_app(app)


@app.before_first_request
def create_tables():
    db.create_all()

 
api.add_resource(Course_one, '/course/<int:id_number>/<name>')
api.add_resource(Course_two, '/course/<int:id_number>/')

api.add_resource(Student_one, '/student/<int:id_number>/<name>')
api.add_resource(Student_two, '/student/<int:id_number>/')

api.add_resource(Event_one, '/event/<int:id_number>/<name>')
api.add_resource(Event_two, '/event/<int:id_number>/')


api.add_resource(All_courses, '/courses/')
api.add_resource(All_students, '/students/')
api.add_resource(All_events, '/events/')