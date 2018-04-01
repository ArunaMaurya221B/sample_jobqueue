import __init__

if __name__ == '__main__':

	#to acquire connection to the database, call the class
	database_connection = DatabaseConnection() 

	table_name = raw_input("Enter the table name:")
	database_connection.create_table()

	table_name = raw_input("Enter the table name:")
	database_connection.drop_table()

	table_name = raw_input("Enter the table name:")
	database_connection.alter_table()
	data = raw_input("Enter the column and the type: ")

	table_name = raw_input("Enter table name to insert data to: ")
	data = raw_input("Enter the data to be updated separated by comma: ")
	database_connection.insert_table()