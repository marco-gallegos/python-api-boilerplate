# traductor-python 2020B

api para un traductor ciclo 2020b

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