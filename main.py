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
db.drop_tables([Contact])
db.create_tables([Contact])

def welcome_page():
    print("Welcome to your contact book. What would you like do:" )
    print('show contact: 1 create contact: 2 delete contact: 3 update contact: 4 exit: 5)
    answer = input('')
    if answer == '1':
        show_contact()
    elif answer == '2':
        create_contact()    

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

def delete_contact():
    first_name = input("first name ")
    contact = Contact.get(Contact.first_name == first_name)
    contact.delete_instace()
    delete_contact()

# GO  BACK TO UPDATE LATER
# def update_contact():
#     update_first_name = input("first name ")  
#     update_last_name = input("last name ")
#     update_phone_number = input("phone number ")   

#     edit_contact = Contact(
#        first_name = update_first_name,
#        last_name = update_last_name,
#        phone_numbert = update_phone_number 
#     )



# john = Contact(
#     first_name="John", 
#     last_name="Doe", 
#     phone_number="1234567890")

# john.save()

# chad = Contact (
#  first_name = "Chad",
#  last_name = "Smith",
#  phone_number = "7576890342")

   
welcome_page()