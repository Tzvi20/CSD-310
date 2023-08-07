# author: Tzvi kaplan
# date: august 7 2023
# whatabook application
# the user can add books to a wishlist, view store locations

whatabook = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "localhost",
    "database": "whatabook",
    "raise_on_warnings": True
}
def show_menu():
    print("\n     Main Menu   ")
    print("    1. View Books\n    2. View Store Locations\n    3. My Account\n    4. Exit Program")

    try:
        choice = int(input('      <example enter: 1 for book listing>: '))
        return choice
    except ValueError:
        print("\n  option is invalid, program terminated...\n")

        sys.exit(0)

def show_books(_cursor):

    _cursor.execute("SELECT book_id, book_name, author, details from book")

    # get the results from the cursor 
    books = _cursor.fetchall()

    print("\n       displaying book details ")
    
    # prints out the results for the books
    for book in books:
        print("  Book Name: {}\n  Author: {}\n  Details: {}\n".format(book[0], book[1], book[2]))

def show_locations(_cursor):
    cursor.execute("SELECT store_id, locale from store")

    locations = cursor.fetchall()
    # these lines of code print out the location information
    print("\n  displaying store locations ")

    for location in locations:
        print("  locale: {}\n".format(location[1]))

def verify_user():
    
    try:
        user_id = int(input('\n     Enter a customer id <Example 1 for user_id 1>: '))

        if user_id < 0 or user_id > 3:
            print("\n  invalid customer ID, program ended \n")
            sys.exit(0)

        return user_id
    except ValueError: # prints out this message if a incorrect user ID is entered
        print("\n  Invalid number, program terminated...\n")

        sys.exit(0)

def show_account_menu():
     # displays the users account options 

    try:
        print("\n       Customer Menu")
        print("        1. Wishlist\n        2. Add Book\n        3. Main Menu")
        account_option = int(input('        <example enter: 1 for wishlist>: '))

        return account_option
    except ValueError: # if a user tries to enter 5 it will print this message out and the program will end
        print("\n  invalid number, program ended \n")

        sys.exit(0)

def show_wishlist(cursor, _user_id):

# queries the database for the list of books added to the users wishlist 
    cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author " + 
                    "FROM wishlist " + 
                    "INNER JOIN user ON wishlist.user_id = user.user_id " + 
                    "INNER JOIN book ON wishlist.book_id = book.book_id " + 
                    "WHERE user.user_id = {}".format(_user_id))
    
    wishlist = cursor.fetchall()

    print("\n         displaying your wishlist")

    for book in wishlist:
        print("     Book Name: {}\n     Author: {}\n".format(book[4], book[5]))

def show_books_to_add(_cursor, _user_id):

# queries the database for the list of books that are not in the users wishlist
    query = ("SELECT book_id, book_name, author, details "
            "FROM book "
            "WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(_user_id))

    print(query)

    _cursor.execute(query)

    books_to_add = _cursor.fetchall()

    print("\n        displaying books that are not available at the moment")

    for book in books_to_add:
        print("        Book Id: {}\n        Book Name: {}\n".format(book[0], book[1]))

def add_book_to_wishlist(_cursor, _user_id, _book_id):
    _cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES({}, {})".format(_user_id, _book_id))

try:
    # try and catch block for handling potential MySQL database errors as always

    db = mysql.connector.connect(**whatabook) # connect to the WhatABook database 

    cursor = db.cursor() # cursor for MySQL queries

    print("\n  Welcome to the WhatABook application! ")

    user_selection = show_menu() # show the main menu 

    # while the user's selection isn't 4
    while user_selection != 4:

        # if the user chooses 1, call the show_books method and display the  list of books
        if user_selection == 1:
            show_books(cursor)

        # if the user chooses 2, call the show_locations method and display the available locations
        if user_selection == 2:
            show_locations(cursor)

        # if the user chooses 3, call the verify_user method to verify the entered user_id 
        # calls the show_account_menu() to show the account settings menu
        if user_selection == 3:
            my_user_id = verify_user()
            account_option = show_account_menu()

            # while account option does not equal 3
            while account_option != 3:

                # if the user chooses 1, call the show_wishlist() method to show the current users 
                # configured wishlist items 
                if account_option == 1:
                    show_wishlist(cursor, my_user_id)

                # if the user chooses 2, call the show_books_to_add function to show the user 
                # the books not currently configured in the users wishlist
                if account_option == 2:

                    # show the books not currently in the users wishlist
                    show_books_to_add(cursor, my_user_id)

                    # get the entered book_id 
                    book_id = int(input("\n        Enter the ID of the book you want to add: "))
                    
                    # add the selected book the users wishlist
                    add_book_to_wishlist(cursor, my_user_id, book_id)

                    db.commit() # makes the changes to the database 

                    print("\n       Book id: {} was added to your wishlist".format(book_id))

                # if the selected option is less than 0 or greater than 3, display an invalid user selection 
                if account_option < 0 or account_option > 3:
                    print("\n       Invalid option, please retry ")

                # shows the account menu 
                account_option = show_account_menu()
        
        # if the user selection is less than 0 or greater than 4, display an invalid user selection
        if user_selection < 0 or user_selection >3:
            print("\n       Invalid option, please retry")
            
        # show the main menu
        user_selection = show_menu()

    print("\n\n  program ended")

except mysql.connector.Error as err:
   # error handling

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password is invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
    # closes the connection to the whatabook database  
    db.close()
