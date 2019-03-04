from flask_restful import Resource, Api
from flask import jsonify, Blueprint

event_list = [
    {"id": 1, "event": "Quiz 1"},
    {"id": 2, "event": "Mid-Term"},
    {"id": 3, "event": "Final"}
]

event_blueprint = Blueprint('event_blueprint', __name__, template_folder='templates')
api = Api(event_blueprint)

class Event_one(Resource):
    
    
    # The POST method implementation  ---Crud (Create of CRUD)               
    def post(self, event_id, event):
        id_exist = False
        for i in range(len(event_list)):
            if event_list[i-1]['id'] == event_id:
                id_exist = True
        
        if id_exist == False:
            event_list.append(dict({'id': event_id, 'event': event}))
            return jsonify(event_list)
        else:
            return "ID already exist"

    # The PUT method implementation ---crUd (Update of CRUD)
    def put(self, event_id, event):

        for a in event_list:
            if a["id"] == event_id:
                a.update({'event': event})
                return jsonify(a)

        event_list.append(dict({'id': event_id, 'event': event}))
        return jsonify(event_list)

    
class Event_two(Resource):
    
    # The GET method implementation  ---cRud (Retrieve of CRUD)
    def get(self, event_id):
        flag = False
        for event in event_list:
            if event["id"] == event_id:
                flag = True
                return jsonify(event)
        if flag == False:    
            return "ID not Found!"

    # The DELETE method implementation ---cruD (Delete of CRUD)
    def delete(self, event_id):
        flag = False
        for i in range(len(event_list)): 
            if event_list[i]['id'] == event_id: 
                del event_list[i] 
                flag = True
                return "Event deleted!"

        if flag == False:
            return "ID not Found!"
    

class All_events(Resource):
    def get(self):
        return jsonify(event_list)


api.add_resource(Event_one, '/event/<int:event_id>/<event>')
api.add_resource(Event_two, '/event/<int:event_id>/')
api.add_resource(All_events, '/events/')