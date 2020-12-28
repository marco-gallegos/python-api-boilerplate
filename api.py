"""
@Author Marco A. Gallegos
@Date   2020/10/09
@Update 2020/10/09
@Description
    Main Api file
"""
from flask import Flask
from flask_restful import Api
import os

#controladores
import controllers

#TODO use app_name from .env
app = Flask(__name__)
api = Api(app)

# rutas resource de flask restful
api.add_resource(controllers.HelloWorld, '/')
api.add_resource(controllers.UserController, '/user')

#se pueden agregar rutas nativas de flask que regresen json


if __name__ == '__main__':
    host = os.getenv('APP_HOST') if os.getenv('APP_HOST') else  '0.0.0.0'
    port = os.getenv('APP_PORT') if os.getenv('APP_PORT') else  5000
    app.run(debug=True, host=host, port=port)