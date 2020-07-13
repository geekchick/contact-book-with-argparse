
import argparse
from datetime import date
import sqlite3
from sqlite3 import Error

class ContactBook:
    conn = sqlite3.connect('contact.db')
    c = conn.cursor()

    c.execute(""" CREATE TABLE IF NOT EXISTS contacts (
                            firstname text,
                            lastname text,
                            email text,
                            phone text
                ) """) 



    def __init__(self, first_name=None, last_name=None, email=None, phone=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.date_created = date.today()


    
    def get_args(self):
        parser = argparse.ArgumentParser(description="Creating a contact book.")
        parser.add_argument('--firstname', type=str, help='The first name of your contact')
        parser.add_argument('--lastname', type=str, help='The last name of your contact')
        parser.add_argument('--email', type=str, help="The email address of your contact")
        parser.add_argument('--phone', type=str, help="The phone number of your contact")
        parser.add_argument('--update', help="This will allow you to update a contact", action="store_true")
        parser.add_argument('--all', help="Will list all of your contacts", action="store_true")
        parser.add_argument('--deleteall', help="Will delete all your contacts", action="store_true")
        args = parser.parse_args()
       

        print(f"this is args: {args}")
        return args

    def insert_contact(self):
        """
        inserts a contact into the database if it doesn't exist in the contacts table
        """
        contact_args = contact.get_args()
        print(f"this is contact_args: {contact_args}")
        name_list = self.c.execute("SELECT * FROM contacts WHERE firstname=:firstname AND lastname=:lastname", {'firstname':contact_args.firstname, 'lastname':contact_args.lastname})

        if (contact_args.firstname, contact_args.lastname, contact_args.email, contact_args.phone) not in name_list and not contact_args.all: # check if tuple is in the list, if it's not then insert it into the table
            print("...Not in table so insert...")
            self.c.execute("INSERT INTO contacts VALUES (:firstname, :lastname, :email, :phone)", 
                            {'firstname': contact_args.firstname, 'lastname': contact_args.lastname, 'email':contact_args.email, 'phone':contact_args.phone})
            self.conn.commit()
            self.conn.close()
        else:
            print("...Contact is already in your contact book...")


    def update_contact(self):
        """
        Updates the information of the contact
        """
        field_changed = input("Which field do you want to update? Type 'firstname','lastname','email' or 'phone > ")
        field_changed_to = input("What do you want to change the field to? > ")
        firstname_value = input("What is the first name of the contact you want to change? > ")
        lastname_value = input("What is the last name of the contact you want to change? > ")

        self.c.execute("""UPDATE contacts SET """ + field_changed + """=?
                          WHERE firstname = ? and lastname = ? """,
                          (field_changed_to, firstname_value, lastname_value))
        
        self.conn.commit()
        self.conn.close()




        

    def delete_all_contacts(self):
        # deletes all contacts from your contact book
        confirmation = input("Are you sure you want to delete ALL your contacts? Type 'Yes' or 'No' > ")
        if confirmation == "Yes" or  confirmation == "yes":
            print("..You are deleting all your contacts...")
            self.c.execute("DELETE FROM contacts")
            self.conn.commit()
            self.conn.close()
        elif confirmation == "No" or confirmation == "no":
            print("Phew, your contacts will not be deleted.")
    

    def list_contacts(self):
        """
        Selects all the contacts in the contact book and prints them out to the console
        """

        self.c.execute("SELECT * FROM contacts")
        contacts = self.c.fetchall()
        for item in contacts:
            print(item)
    

    def list_contact_in_order(self):
        pass

    def list_contact_by_date(self):
        pass

    def main(self):

        args = contact.get_args()

        if args.all:
            contact.list_contacts()
        elif args.deleteall:
            contact.delete_all_contacts()
        elif args.firstname:
            contact.insert_contact()
        elif args.update:
            contact.update_contact()



contact = ContactBook()
contact.main()

  
            