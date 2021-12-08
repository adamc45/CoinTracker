from dotenv import load_dotenv
import os
import mysql.connector

load_dotenv()
db_password = os.getenv("DB_PASSWORD")
db = os.getenv("DB")
host = os.getenv("HOST")
user = os.getenv("USER")

class Connection:
	def get_conn(self):
		return mysql.connector.connect(
			database=db,
			host=host,
			password=db_password,
			user=user
		)
	def get_cursor(self, conn):
		return conn.cursor()
