from flask_restful import Resource, Api
from flask import jsonify, Blueprint

course_list = [
    {"id": 1, "name": "COS340a"},
    {"id": 2, "name": "COS310a"},
    {"id": 3, "name": "COS220b"}
]


course_blueprint = Blueprint('course_blueprint', __name__, template_folder='templates')
api = Api(course_blueprint)


class Course_one(Resource):
    

    # The POST method implementation  ---Crud (Create of CRUD)           
    def post(self,course_id,name):

        id_exist = False
        for i in range(len(course_list)):
            if course_list[i-1]['id'] == course_id:
                id_exist = True
    
        if id_exist == False:
            course_list.append(dict({'id': course_id, 'name': name}))
            return jsonify(course_list)
        else:
            return "ID already exist"

    # The PUT method implementation ---crUd (Update of CRUD)
    def put(self,course_id,name):

        for a in course_list:
            if a["id"] == course_id:
                a.update({'name': name})
                return jsonify(a)

        course_list.append(dict({'id': course_id, 'name': name}))
        return jsonify(course_list)
    

class Course_two(Resource):

     # The GET method implementation  ---cRud (Retrieve of CRUD)
    def get(self, course_id):
        flag = False
        for course in course_list:
            if course["id"] == course_id:
                flag = True
                return jsonify(course)
        if flag == False:    
            return "ID not Found!"


    # The DELETE method implementation ---cruD (Delete of CRUD)        
    def delete(self, course_id):
        flag = False
        for i in range(len(course_list)): 
            if course_list[i]['id'] == course_id: 
                del course_list[i]
                flag = True
                return "Course deleted!"

        if flag == False:
            return "ID not Found!"


class All_courses(Resource):
    def get(self):
        return jsonify(course_list)

api.add_resource(Course_one, '/course/<int:course_id>/<name>')
api.add_resource(Course_two, '/course/<int:course_id>/')
api.add_resource(All_courses, '/courses/')