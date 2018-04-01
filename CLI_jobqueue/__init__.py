import psycopg2
from pprint import pprint

class DatabaseConnection:
	def __init__(self):
		try:
			self.connection = psycopg2.connect(
				"dbname=sample user=icts")
			self.connection.autocommit = True
			self.cursor = self.connection.cursor()
		except:
			pprint("Cannot connect")

	# creating the table
	def create_table(self):
		create_table_command = "CREATE TABLE %s (id integer primary key, name VARCHAR(10), status VARCHAR(10))" %(table_name)
		self.cursor.execute (create_table_command)

	# drop/delete a table
	def drop_table(self):
		drop_command = "DROP TABLE %s" %(table_name)
		self.cursor.execute(drop_command)

	# alter table: can add new columns
	def alter_table(self):
		alter_command = "ALTER TABLE %s ADD %s %s" %(table_name, column, typec)
		self.cursor.execute(alter_command)

	# inserting values into the table
	def insert_table(self):
		insert_command = "INSERT INTO %s(id, name, status) VALUES (%s, '%s', '%s')" %(table_name, a, b, c)
		self.cursor.execute(insert_command)

	#print the table
	def display_table(self):
		display_command = "SELECT * FROM %s" %(table_name)
		self.cursor.execute(display_command)
		temps = self.cursor.fetchall()
		for temp in temps:
			pprint("Each row: {0}".format(temp))



if __name__ == '__main__':

	#to acquire connection to the database, call the class
	database_connection = DatabaseConnection() 

	"""table_name = raw_input("Enter the table name:")
	database_connection.create_table()

	table_name = raw_input("Enter the table name:")
	database_connection.drop_table()

	table_name = raw_input("Enter the table name:")
	database_connection.display_table()"""

	"""table_name = raw_input("Enter the table name:")
	column = raw_input("Enter the column name: ")
	typec = raw_input("Enter the type: ")
	database_connection.alter_table()"""

	"""table_name = raw_input("Enter table name to insert data to: ")
	a = input("Enter id: ")
	b = raw_input("Enter name: ")
	c = raw_input("Enter status: ")
	database_connection.insert_table()"""