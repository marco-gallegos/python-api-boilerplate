"""
@Author Marco A. Gallegos
@Date 2020/10/09
@Update 2020/10/09
@Description
    This file return the type of db configured in .env file
"""
from peewee import SqliteDatabase, MySQLDatabase, PostgresqlDatabase
from config.config import APP_CONFIG
import os

print(f"database {APP_CONFIG['DB_CONNECTION']}/{APP_CONFIG['DB_DATABASE']}")
print(f"{APP_CONFIG}")

if APP_CONFIG['DB_CONNECTION'] == 'sqlite':
    db = SqliteDatabase(APP_CONFIG['DB_DATABASE'])
elif APP_CONFIG['DB_CONNECTION'] == 'mysql':
    db = MySQLDatabase(database=APP_CONFIG['DB_DATABASE'], user=APP_CONFIG['DB_USERNAME'], password=APP_CONFIG['DB_PASSWORD'], host=APP_CONFIG['DB_HOST'], port=APP_CONFIG['DB_PORT'])
elif APP_CONFIG['DB_CONNECTION'] == 'postgres':
    db = PostgresqlDatabase(database=APP_CONFIG['DB_DATABASE'], user=APP_CONFIG['DB_USERNAME'], password=APP_CONFIG['DB_PASSWORD'], host=APP_CONFIG['DB_HOST'], port=APP_CONFIG['DB_PORT'])
else:
    raise Exception("please configure a valid SQL SGBD en .env file")