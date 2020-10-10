"""
@Author Marco A. Gallegos
@Date 2020/10/09
@Description
    Api para el compilador de tradutores de lenguajes 2, debe contener enpoints para el control
    de el analizador lexic, sintactico y ..
"""
from flask import Flask
from flask_restful import Api

#controladores no olvides agregar la clase en el init de el paquete
import controllers

app = Flask(__name__)
api = Api(app)

# rutas resource de flask restful
api.add_resource(controllers.HelloWorld, '/')

#se pueden agregar rutas nativas de flask que escupan json

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')