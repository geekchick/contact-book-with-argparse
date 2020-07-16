
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
        parser.add_argument('--listcontact', help="This will grab a contact you specify by first and last name and print it to the console", action="store_true")
        parser.add_argument('--listsort', help="This will list contacts by last name in alphabetical order and print it to the console", action="store_true")
        parser.add_argument('--all', help="Will list all of your contacts", action="store_true")
        parser.add_argument('--deleteall', help="Will delete all your contacts", action="store_true")
        parser.add_argument('--delete', help="This will delete a particular contact you specify", action="store_true")
        args = parser.parse_args()
       

        #print(f"this is args: {args}")
        return args

    def insert_contact(self):
        """
        inserts a contact into the database if it doesn't exist in the contacts table
        """
        contact_args = contact.get_args()
        #print(f"this is contact_args: {contact_args}")
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

    # TODO: this function does not loop thorugh and prompt to delete when more than one contact
    def delete_contact(self): 
        """
        Deletes a contact you specify
        """
        
        firstname_delete = input("What is the first name of the contact you want to delete? ")
        lastname_delete = input("What is the last name of the contact you want to delete? ")

        contacts_to_delete = self.c.execute("SELECT * FROM contacts WHERE firstname=? AND lastname=?",
                            (firstname_delete, lastname_delete) )
     
        row = self.c.fetchone()
        if row is None:
            print(f"The contact {firstname_delete} {lastname_delete} does not exist.")

        for contact in contacts_to_delete:
            first, last, email, phone = contact

            is_delete = input("Do you want to delete contact {} {} {} {} ? Type 'Yes' or 'No' > ".format(first, last, email, phone))
            if is_delete == 'Yes' or 'yes':
                self.c.execute("DELETE FROM contacts WHERE firstname=? AND lastname=? AND email=? AND phone=?",
                                    (first, last, email, phone))

                print("Your contact has been deleted.")

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
    

    def list_contact(self):
        """ 
        Selects a contact that's specified and prints it to the console
        """
        firstname_contact = input("What is the first name of your contact? ")
        lastname_contact = input("What is the last name of your contact? ") 

        select_contact = self.c.execute("SELECT * FROM contacts WHERE firstname=?" \
                                        "AND lastname=?", (firstname_contact, lastname_contact))

        row = self.c.fetchone() # gets the first row
            
        if row is None: # if there are no results in the first row then the contact doesn't exist
             print(f"There is no contact by the name of {firstname_contact} {lastname_contact}")

        for contact in select_contact:
            first, last, email, phone = contact
            if first == firstname_contact and last == lastname_contact:
                print(f"Here is your contact: {contact}")



    def list_sort_by_last_name(self):
        """
        Sorts the contacts by last name in ascending order and prints to the console
        """

        sorted_contacts = self.c.execute("SELECT * FROM contacts ORDER BY lastname")
        
        for contact in sorted_contacts:
            print(contact)


    def main(self):

        args = contact.get_args()

        if args.all:
            contact.list_contacts()
        elif args.deleteall:
            contact.delete_all_contacts()
        elif args.delete:
            contact.delete_contact()
        elif args.firstname:
            contact.insert_contact()
        elif args.update:
            contact.update_contact()
        elif args.listcontact:
            contact.list_contact()
        elif args.listsort:
            contact.list_sort_by_last_name()



contact = ContactBook()
contact.main()

  
            