"""
@Author Marco A. Gallegos
@Date 2020/10/09
@Description
    login controller this controller make the login function
"""
from flask_restful import Resource, reqparse
from model.user import User

from flask_jwt_extended import (
    jwt_required, create_access_token,
    get_jwt_identity, create_refresh_token
)


class LoginController(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('email',help='the name field is required', required=True)
    parser.add_argument('password',help='the name field is required', required=True)

    @jwt_required
    def get(self):
        user = get_jwt_identity()
        return {
            "identity": user,
        }
    
    def post(self):
        data = self.parser.parse_args()
        user = User.select().where(User.email == data['email']).get()
        print(user)
        seriaized_user = user.get_as_dict()
        seriaized_user.pop('password')
        if user:
            coincide_password  = User.verify_hash( data['password'], user.password)
            if coincide_password:
                access_token = create_access_token(identity=seriaized_user)
                print(access_token)
                refresh_token = create_refresh_token(identity=seriaized_user)
                return {
                    'message': f"Logged in as {user.name}",
                    'access_token': access_token,
                    'refresh_token': refresh_token
                }
            else:
                return {'message': 'Wrong credentials'}
        return {'message': 'Wrong credentials'}
