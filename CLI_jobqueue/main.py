import psycopg2
from pprint import pprint
from database import *

if __name__ == '__main__':

	#to acquire connection to the database, call the class
	database_connection = DatabaseConnection() 
	"""database_connection.procedure()"""
	"""database_connection.trigger()
	table_name = raw_input("Enter the table name:")
	database_connection.create_table(table_name)
	
	table_name = raw_input("Enter the table name:")
	database_connection.drop_table()

	table_name = raw_input("Enter the table name:")
	database_connection.display_table()

	table_name = raw_input("Enter the table name:")
	column = raw_input("Enter the column name: ")
	typec = raw_input("Enter the type: ")
	database_connection.alter_table()"""

	table_name = raw_input("Enter table name to insert data to: ")
	a = input("Enter id: ")
	b = raw_input("Enter name: ")
	c = raw_input("Enter status: ")
	database_connection.insert_table(table_name, a, b, c)