
The main objective of this project is to save contact details. You can use commands to enter the contact details. This project uses the argparse library. 

Some features that are implemented include the ability to add new contacts as well as commands to delete contacts, update contact information, and list saved contacts. You can also allow users to list contacts using different parameters, such as alphabetical order.

Since it’s a command-line project, the contacts will save to a sqlite3 database, named contact.db, on your local computer which will be created when you run:

 $ python3 contact_book.py

 from your command line terminal.

 Then you can pass in the following flags:
 

 `python3 contact_book.py --firstname "John" --lastname "Doe" --email "johndoe@foo.bar" --phone "2222222222"`<br/>  **Note: Adds a contact to database**
 `python3 contact_book.py --update`<br/> **Note: Updates a contact**
 `python3 contact_book.py --listcontact`<br/> **Note: Lists a specific contact**
 `python3 contact_book.py --listsort`<br/> **Note: Sorts contacts in alphabetical order**
 `python3 contact_book.py --all`<br/> **Note: Lists all your contacts**
 `python3 contact_book.py --deleteall`<br/> **Note: Deletes all your contacts**
 `python3 contact_book.py --delete`<br/> **Note: Deletes a specific contact**
 
