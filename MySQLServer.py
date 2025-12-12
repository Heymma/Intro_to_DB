import mysql.connector
from mysql.connector import Error


def create_database():
    connection = None
    cursor = None

    try:
        # Update user / password if needed
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Heymma080648"   # <-- replace with your MySQL password
        )

        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

    except Error as err:
        print(f"Error while connecting to MySQL or creating database: {err}")

    finally:
        # Properly close cursor and connection
        if cursor is not None:
            cursor.close()
        if connection is not None and connection.is_connected():
            connection.close()


if __name__ == "__main__":
    create_database()