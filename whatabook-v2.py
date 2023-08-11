# author: Tzvi Kaplan
# data: august 11 2023
# whatabook program
# description: program that allows user to view list of books, view store locations,
# add books to wishlist and view wishlist


import sys
import mysql.connector
from mysql.connector import errorcode
# connection information for the database
whatabook = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "localhost",
    "database": "whatabook",
    "raise_on_warnings": True
}
# shows the main menu
#if invalid option is entered, user tries again
def show_menu():
    print("\nWelcome to WhatABook program \n")
    print("\nMain Menu\n")
    print("[1.] View Books")
    print("[2.] View Store Locations")
    print("[3.] My Account")
    print("[4.] Exit program")
    try:
        option = int(input("Select option [1-4]: "))

        return option
    
    except ValueError:
        print("\nInvalid number, program terminated...\n")


# shows the list of books 
def show_books(_cursor):
    _cursor.execute("SELECT book_id, book_name, author FROM book")

    # get the results from the cursor
    books = _cursor.fetchall()

    print("\n       displaying book details ")

    # prints out the results for the books
    for book in books:
        print("  Book ID: {}\n  Book Name: {}\n  Author: {}\n".format(book[0], book[1], book[2]))

def show_locations(_cursor):
    _cursor.execute("SELECT store_id, locale FROM store")

    locations = _cursor.fetchall()
    # these lines of code print out the location information
    print("\n  displaying store locations ")

    for location in locations:
        print("  locale: {}\n".format(location[1]))

def verify_user():
    try:
        user_id = int(input('\n     Enter a customer id <Example 1 for user_id 1>: '))
# if a user choooses a number less than 1 or more than 3 the program will print this message and exit
        if user_id < 1 or user_id > 3:
            print("\n  invalid customer ID, program ended \n")
            sys.exit(0)

        return user_id
    except ValueError:
        print("\n  Invalid number, program terminated   \n")
        sys.exit(0)
# shows displays the main menu
def show_account_menu():
    try: # user acounts options menu
        print("\n       Customer Menu")
        print("        1. Wishlist\n        2. Add Book\n        3. Main Menu")
        account_option = int(input('        <example enter: 1 for wishlist>: '))

        return account_option
    except ValueError:
        print("\n  invalid number, program ended \n")
        sys.exit(0)
# user wishlist method
def show_wishlist(cursor, _user_id):
    # inner join
    cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author " + 
                    "FROM wishlist " + 
                    "INNER JOIN user ON wishlist.user_id = user.user_id " + 
                    "INNER JOIN book ON wishlist.book_id = book.book_id " + 
                    "WHERE user.user_id = {}".format(_user_id))
    
    wishlist = cursor.fetchall()

    print("\n         displaying your wishlist")
    # displays user wishlist list of books
    for book in wishlist:
        print("     Book ID: {}\n     Book Name: {}\n     Author: {}\n".format(book[3], book[4], book[5]))
# method that adds books to wishlist
def show_books_to_add(_cursor, _user_id):
    query = ("SELECT book_id, book_name, author, details "
            "FROM book "
            "WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(_user_id))
# these two lines of code actually add the books to the wishlist
    _cursor.execute(query)
    books_to_add = _cursor.fetchall()

    print("\n        displaying books that are not available at the moment")
# prints out the list of available books in books table

    for book in books_to_add:
        print("        Book ID: {}\n        Book Name: {}\n".format(book[0], book[1]))

def add_book_to_wishlist(_cursor, _user_id, _book_id):
    _cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES({}, {})".format(_user_id, _book_id))
# try and except block for catching database connection errors
try:
    db = mysql.connector.connect(**whatabook)
    cursor = db.cursor()

   # print("\n  Welcome to the WhatABook application! ")

    user_selection = show_menu()
# if the user chooses option 1 it will display the list of books
    while user_selection != 4:
        
        if user_selection == 1:
            # this line executes showing the books
            show_books(cursor)
      
       # if a user chooses option 2 then the program will show the locations
        if user_selection == 2:
            show_locations(cursor)
       
        # my accounr options menu
        # the user can view wishlist, add books, or go to main menu
        if user_selection == 3:
            my_user_id = verify_user()
            account_option = show_account_menu()
        
        # if a user does choose option 3
            while account_option != 3:
               
               
               
            # if option 1 is chosen then the user will view the wishlist 
                if account_option == 1:
                    show_wishlist(cursor, my_user_id)
                
            # if option 2 is chosen then the user will be shown a list of books to add from the books table    
                if account_option == 2:
                    show_books_to_add(cursor, my_user_id)
                   
                   # the user is given the list of books from the books table and is prompted to enter the ID of the book
                    book_id = int(input("\n        Enter the ID of the book you want to add: "))
                    add_book_to_wishlist(cursor, my_user_id, book_id)
                    
                    # commits the changes to the database
                    db.commit()
                    print("\n       Book ID: {} was added to your wishlist".format(book_id))
                
               # if the user chooses a numner less than 1 or greater than 3 in the account options menu then this message will be printed out
                if account_option < 1 or account_option > 3:
                    print("\n       Invalid option, please retry ")
                account_option = show_account_menu()

         
               # if the user chooses a numner less than 1 or greater than 4 in the account options menu then this message will be printed out
        if user_selection < 1 or user_selection > 4:
            print("\n       Invalid option, please retry")

        user_selection = show_menu()

    print("\n\n  program ended")

# database error catching except blocks
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password is invalid")
    
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")
   
    else:
        print(err)
# closes the connction to the whatabook database
finally:
    cursor.close()
    db.close()