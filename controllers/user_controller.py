"""
@Author Marco A. Gallegos
@Date 2020/10/09
@Description
    user controller
"""
from flask_restful import Resource, reqparse
from model.user import User
import pendulum


class UserController(Resource):
    parser = reqparse.RequestParser()
    #TODO investigar el parametro type
    parser.add_argument('name', help='the name field is required', required=True)
    parser.add_argument('lastname', help='the name field is required', required=True)
    parser.add_argument('email', help='the name field is required', required=True)
    parser.add_argument('password', help='the name field is required', required=True)

    def get(self):
        users_query = User.select().dicts()
        users = list()
        for user in users_query:
            if user['created_at']:
                user['created_at'] = pendulum.instance(user['created_at']).to_datetime_string()
            users.append(user)
        #print(users)
        return users
    
    def post(self):
        data = self.parser.parse_args()

        new_user = User.create(
            name = data['name'],
            lastname = data['lastname'],
            email = data['email'],
            password = User.generate_hash(data['password'])
        )

        return new_user
