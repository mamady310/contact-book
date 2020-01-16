from peewee import *

db = PostgresqlDatabase('contacts', user='postgres', password='', host='localhost', port=5432)

class BaseModel(Model):
   
    class Meta:
        database = db

class Contact(BaseModel):
    first_name = CharField()
    last_name = CharField()
    phone_number = CharField()


db.connect()