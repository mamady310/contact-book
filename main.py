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
# db.drop_tables([Contact])
db.create_tables([Contact])

def welcome_page():
    print("Welcome to your contact book. What would you like do?" )
    print('show contacts: 1 create contact: 2 delete contact: 3 update contact: 4 exit: 5')
    answer = input('')
    if answer == '1':
        print('answer')
        # show_contact()
    elif answer == '2':
       create_contact() 
    elif answer == '3':
       delete_contact()      
    elif answer == '4':
       update_contact()
    else:
       exit      

def show_contact():
    

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
    last_name = input("Find contact to delete by last name:  ")
    contact = Contact.get(Contact.last_name == last_name)
    delete_contact()

    contact.delete_instace()
    

def update_contact():
    last_name = input("Find Contact to update by last name: ")
    contact = Contact.get(Contact.last_name == last_name) 
    contact.first_name = input ("first name ")
    contact.last_name = input("last name ")
    contact.phone_number = input( "phone number")
  
    contact.save()


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