# Rest Api Boilerplate

el objetivo de este repo es proveer un templete para microservicios o apis usando :

* flask (framework)
* peewee (ORM)
* jwt (auth)
* flask_restful (routes manager)

adicionalmente:

* pendulum (like moment in js or carbon in php)

## Requisitos

#### pip tools

utileria para la gestion de requerimientos se debe instalar para actualizar el archivo requirements.txt `pip install pip-tools`.

```shell
#se corre el comando para leer requirements.in y generar requirements.txt
pip-compile
pip install -r requirements.txt
```


## SetUp

#### maquina local

para levantar en tu maquina local debes

* instalar python
* instalar librerias `pip install -r requirements.txt`
* python api.py


#### docker

se puede levantar usando docker

* instala docker y docker-compose
* docker-compose up -d