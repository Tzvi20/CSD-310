#Author: Tzvi Kaplan
#date: July 21 2023
#pytest connection code
import mysql.connector

def connect_to_mysql(host, user, password, database):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Trump2024",
            database="pytest"
        )
        print("Connected to MySQL database!")
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def main():

    host = "localhost"
    user = "root"
    password = "Trump2024"
    database = "pytest"

    connection = connect_to_mysql(host, user, password, database)
    if not connection:
        return

    connection.close()
    print("Connection closed.")

if __name__ == "__main__":
    main()