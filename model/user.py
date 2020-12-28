
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


class User(Model):
    id = AutoField(primary_key=True)
    name = CharField()
    lastname = CharField()
    email = CharField(unique=True, index=True)
    password = CharField()
    created_at = DateTimeField()
    updated_at = DateTimeField(null=True)
    deleted_at = DateTimeField(null=True)

    class Meta:
        database = db
        table_name="users"

    def get_as_dict(self)->dict:
        return {
            "id":self.id
        }
