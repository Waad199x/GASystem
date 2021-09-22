from flask import Flask, request, jsonify, abort, Response
import json
from flask_cors import CORS
from .database.models import db_drop_and_create_all, setup_db, Group

from .auth.auth import AuthError, requires_auth
from typing import Dict


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    CORS(app)
    setup_db(app)

    return app


app = create_app()

'''
# ROLE TYPES

    `Teachers role`
        - Can get the groups information only.
        - For each group they can view the students list info

    `Supervisor role`
        Can do the following :
        - view the information of the groups
        - Edit,add,delete the group information (teachers+students info)

    `Manager role`
        Can do the following :
        - Everything the other roles do
        - Edit, create, delete a whole group not only the infos

    The URL to access the frontend is http://localhost:4200/
'''

'''

Running the following command will create 2 new records

'''
db_drop_and_create_all()


'''
    GET /groups (Public endpoint)
    for getting the groups names only
'''


@app.route('/Groups')
def Display_Groups():

    groups_list = []
    groups = Group.query.all()
    for d in groups:
        groups_list.append(d.short())

    if len(groups_list) == 0:
        abort(404)

    else:
        return jsonify({
            "success": True,
            "drinks": groups_list}), 200


'''
    GET /groups-information (Private endpoint)
        for getting the groups information
        teachers & students able to access this endpoint

'''


@app.route('/Groups-Details')
@requires_auth('get:groups-details')
def Display_Groups_Info(payload):

    groups = []
    group = Group.query.all()
    for d in group:
        groups.append(d.long())

    return jsonify({
            "success": True,
            "drinks": groups}), 200


'''
    POST /groups
        (Exclusive endpoint for the Managers only )
            Used to Add new groups

'''


@app.route('/Post-Group', methods=['POST'])
@requires_auth('post:group')
def Create_Group(payload):

    body = request.get_json()

    Group_teacher = body['title']
    Students = body['recipe']
    Group_students = json.dumps(Students)

    group = Group(Teacher_name=Group_teacher,
                  Teacher_Contact_Info=Group_students,
                  Student_Contact_Info=Group_students)

    group.insert()

    return jsonify({
        "success": True,
        "drinks": [group.long()]}), 200


'''
    PATCH /groups/<id>
        (Exclusive endpoint for the supervisors & Managers)
            Used to update teachers & students information list
'''


@app.route('/Edit-Group/<int:id>', methods=['patch'])
@requires_auth('patch:groups')
def Update_Group_Info(payload, id):

    group = Group.query.filter(Group.id == id).one_or_none()

    body = request.get_json()

    if 'title' in body:
        group.Teacher_name = body['title']

    if 'recipe' in body:
        group.Student_Contact_Info = json.dumps(body['recipe'])

    group.update()

    return jsonify({
        "success": True,
        "drinks": [group.long()]}), 200


'''
    DELETE /groups/<id>
        (Exclusive endpoint for the managers only)
                Used to delete existing groups
                returns error if the group id doesn't exist in the database
'''


@app.route('/Delete-Group/<int:id>', methods=['Delete'])
@requires_auth('delete:group')
def Delete_Group(payload, id):

    try:
        group = Group.query.filter(Group.id == id).one_or_none()

        if group is None:
            abort(404)
        else:
            group.delete()

        return jsonify({
            "status": 200,
            "success": True,
            "delete": id})

    except AuthError:
        return jsonify({
            "status": 400,
            "success": False})


'''
The following are Error handlers for unprocessable entities
'''


@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "the token is invalid. unprocessable"
    }), 422


@app.errorhandler(404)
def not_found(error):  # Usualy when there is a problem in the url
    return jsonify({
        "success": False,
        "error": 404,
        "message": "resource not found"
        }), 404


@app.errorhandler(400)
def AuthError(error):
    return jsonify({
        'code': 'No credintials provided',
        'description': 'the claims are invalid'
    }, 403)


@app.errorhandler(400)
def AuthError(error):
    return jsonify({
        'code': 'invalid_access_attempt',
        'description': 'the JWT doesn’t contain \
            the proper action. Unable to find the appropriate permission.'
    }, 400)


class AuthError(Exception):
    """
    An AuthError is raised whenever the authentication failed.
    """
    def __init__(self, error: Dict[str, str], status_code: int):
        super().__init__()
        self.error = error
        self.status_code = status_code


@app.errorhandler(AuthError)
def handle_auth_error(ex: AuthError) -> Response:
    '''
    This error handler capture the error
    so it don't give 500 server error
    '''
    response = jsonify(ex.error)
    response.status_code = ex.status_code
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
