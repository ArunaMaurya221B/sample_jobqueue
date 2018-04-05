import psycopg2
from pprint import pprint
from log import *

class DatabaseConnection():
	def __init__(self):
		try:
			self.connection = psycopg2.connect(
				"dbname=sample user=icts")
			self.connection.autocommit = True
			self.cursor = self.connection.cursor()
		except:
			pprint("Cannot connect")


	def procedure(self):
		with open('create.sql', 'r') as f:
			sql = f.read()
		self.cursor.execute(sql);

	# creating the table
	def create_table(self, table_name):
		create_table_command = "CREATE TABLE %s (id integer primary key, name VARCHAR(10), status VARCHAR(10))" %(table_name)
		self.cursor.execute (create_table_command)
		logger.info("Table created")

	# drop/delete a table
	def drop_table(self, table_name):
		drop_command = "DROP TABLE %s" %(table_name)
		self.cursor.execute(drop_command)
		logger.info("Table deleted")

	# alter table: can add new columns
	def alter_table(self, table_name, column, typec):
		alter_command = "ALTER TABLE %s ADD %s %s" %(table_name, column, typec)
		self.cursor.execute(alter_command)
		logger.info("Table altered")

	# inserting values into the table
	def insert_table(self, table_name, a, b, c):
		insert_command = "INSERT INTO %s(id, name, status) VALUES (%s, '%s', '%s')" %(table_name, a, b, c)
		self.cursor.execute(insert_command)
		logger.info("Insert function executed")


	#print the table
	def display_table(self, table_name):
		display_command = "SELECT * FROM %s" %(table_name)
		self.cursor.execute(display_command)
		temps = self.cursor.fetchall()
		for temp in temps:
			pprint("Each row: {0}".format(temp))
		logger.info("Table printed")

	#creating a trigger
	def trigger(self):
		trigger_command = ("""CREATE TRIGGER trig2 BEFORE INSERT ON a FOR EACH 
							ROW EXECUTE PROCEDURE this()""")
		print "in trigger"
		self.cursor.execute(trigger_command)