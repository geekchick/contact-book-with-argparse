
The main objective of this project is to save contact details. You can use commands to enter the contact details. This project uses the argparse library. 

Some features that are implemented include the ability to add new contacts as well as commands to delete contacts, update contact information, and list saved contacts. You can also allow users to list contacts using different parameters, such as alphabetical order.

Since it’s a command-line project, the contacts will save to a sqlite3 database, named contact.db, on your local computer which will be created when you run:

 $ python3 contact_book.py

 from your command line terminal.

 Then you can pass in the following flags:
 

 `python3 contact_book.py --firstname "John" --lastname "Doe" --email "johndoe@foo.bar" --phone "2222222222"`<br/>  
 `python3 contact_book.py --update`<br/> 
 `python3 contact_book.py --listcontact`<br/> 
 `python3 contact_book.py --listsort` 
 `python3 contact_book.py --all` 
 `python3 contact_book.py --deleteall` 
 `python3 contact_book.py --delete` 
 
