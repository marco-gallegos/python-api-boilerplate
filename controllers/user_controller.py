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
    parser.add_argument('name')

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
        args = self.parser.parse_args()
        return {}
