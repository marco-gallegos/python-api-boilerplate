"""
@Author Marco A. Gallegos
@Date   2020/10/09
@Update 2020/10/09
@Description
    Main Api file
"""
from config.config import APP_CONFIG
from flask import Flask, jsonify
from flask_cors import CORS
from flask_restful import Api
from flask_jwt_extended import (get_jwt_identity, jwt_required, JWTManager)
import os

import controllers

print(APP_CONFIG)

app = Flask(APP_CONFIG['APP_NAME'])
CORS(app, resources={r"/*": {"origins": "*"}})

# Setup the Flask-JWT-Extended extension
app.config["JWT_SECRET_KEY"] = APP_CONFIG['APP_KEY']
jwt = JWTManager(app)


# se pueden agregar rutas nativas de flask que regresen json
@app.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    # Access the identity of the current user with get_jwt_identity
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200


# Setup the flask restful api
api = Api(app)

# rutas resource de flask restful
api.add_resource(controllers.HelloWorld, '/')
api.add_resource(controllers.UserController, '/user')
api.add_resource(controllers.LoginController, '/login')


if __name__ == '__main__':
    host = os.getenv('APP_HOST') if os.getenv('APP_HOST') else '0.0.0.0'
    port = os.getenv('APP_PORT') if os.getenv('APP_PORT') else 5000
    app.run(debug=True, host=host, port=port)
