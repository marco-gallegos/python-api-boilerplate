"""
@Author Marco A. Gallegos
@Date   2020/10/09
@Update 2020/10/09
@Description
    Main Api file
"""
from config.config import APP_CONFIG
from flask import Flask
from flask_cors import CORS
from flask_restful import Api
#from flask_jwt_extended import (
#    JWTManager, jwt_required, create_access_token,
#    get_jwt_claims
#)
import os

# controladores
import controllers



#TODO use app_name from .env
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# Setup the Flask-JWT-Extended extension
#TODO use .env secret
app.config['JWT_SECRET_KEY'] = APP_CONFIG['APP_KEY']
#jwt = JWTManager(app)

#@jwt.user_claims_loader
#def add_claims_to_access_token(identity):
#    print("hola desde claim automatico de jwt")
#    return {
#        'hello': identity,
#    }

#se pueden agregar rutas nativas de flask que regresen json


# Setup the flask restful api
api = Api(app)

# rutas resource de flask restful
api.add_resource(controllers.HelloWorld, '/')
api.add_resource(controllers.UserController, '/user')
#api.add_resource(controllers.LoginController, '/login')



if __name__ == '__main__':
    host = os.getenv('APP_HOST') if os.getenv('APP_HOST') else '0.0.0.0'
    port = os.getenv('APP_PORT') if os.getenv('APP_PORT') else 5000
    app.run(debug=True, host=host, port=port)