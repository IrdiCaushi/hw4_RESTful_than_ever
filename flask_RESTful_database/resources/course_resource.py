from flask_restful import Resource
from flask import jsonify, render_template
from extensions import db
from models.model import StudentModel
from models.model import CourseModel
from models.model import EventModel


class Course_one(Resource):
    

    # The POST method implementation  ---Crud (Create of CRUD)           
    def post(self,id_number,name):

        course = CourseModel(id_number=id_number, name=name)
        db.session.add(course)
        db.session.commit()
        return jsonify({'message': 'New course successfully created.'})

    # The PUT method implementation ---crUd (Update of CRUD)
    def put(self,id_number,name):

        course = CourseModel.query.get(id_number)
        course.name = name
        db.session.commit()
        return jsonify({'message': 'Course successfully updated.'})
    

class Course_two(Resource):

     # The GET method implementation  ---cRud (Retrieve of CRUD)
    def get(self, id_number):
        return render_template('show.html', items = CourseModel.query.filter_by(id_number=id_number) )


    # The DELETE method implementation ---cruD (Delete of CRUD)        
    def delete(self, id_number):
        CourseModel.query.filter_by(id_number=id_number).delete()
        db.session.commit()
        return jsonify({'message': 'Student successfully deleted.'})


class All_courses(Resource):
    def get(self):
        return render_template('show_all.html', items = CourseModel.query.all() )