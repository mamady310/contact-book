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
db.create_tables([Contact])

def create_contact(): 
    new_first_name = input("first name ")
    new_last_name = input("last name ")
    new_phone_number = input("phone number ")

    add_contact = Contact(
        first_name = new_first_name,
        last_name = new_last_name,
        phone_number = new_phone_number
    )
    add_contact.save()
   

   

john = Contact(
    first_name="John", 
    last_name="Doe", 
    phone_number="1234567890")

john.save()
# chad = Contact (
#  first_name = "Chad",
#  last_name = "Smith",
#  phone_number = "7576890342")

    
create_contact()
