
"""
@Author Marco A. Gallegos
@Date   2020/12/26
@Update 2020/12/26
@Description
    Model for users
"""
from config.ORM import db
from peewee import Model
from peewee import CharField, DateTimeField, AutoField
from passlib.hash import pbkdf2_sha256 as sha256
import datetime


class User(Model):
    id = AutoField(primary_key=True)
    name = CharField()
    lastname = CharField()
    email = CharField(unique=True, index=True)
    password = CharField()
    created_at = DateTimeField(default=datetime.datetime.now)
    updated_at = DateTimeField(null=True)
    deleted_at = DateTimeField(null=True)

    class Meta:
        database = db
        table_name="users"

    def get_as_dict(self)->dict:
        return {
            "id":self.id,
            "name":self.name,
            "lastname":self.lastname,
            "email":self.email,
            "password":self.password,
        }
    
    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)
    
    @staticmethod
    def verify_hash(password, hash):
        return sha256.verify(password, hash)
