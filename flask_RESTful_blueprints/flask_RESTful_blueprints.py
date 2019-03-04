from flask import Flask, jsonify, Blueprint
from flask_restful import Resource, Api
from blueprints.course_blueprint import course_blueprint
from blueprints.student_blueprint import student_blueprint
from blueprints.event_blueprint import event_blueprint


app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello from Irdi Caushaj'


app.register_blueprint(course_blueprint, url_prefix='/v1')

app.register_blueprint(student_blueprint, url_prefix='/v2')

app.register_blueprint(event_blueprint, url_prefix='/v3')
