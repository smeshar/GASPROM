import mysql.connector
from mysql.connector import Error
import functions

class Conn():
	def __init__(self):
		hostname = functions.hostname
		database = functions.database
		password = functions.password
		port = functions.port
		username = functions.username

		try:
			self.connection = mysql.connector.connect(host=hostname, database=database, user=username, password=password, port=port)
			if self.connection.is_connected():
				db_Info = self.connection.get_server_info()
				print("Connected to MySQL Server version ", db_Info)
				self.cursor = self.connection.cursor()
				self.cursor.execute("select database();")
				record = self.cursor.fetchone()
				print("You're connected to database: ", record)
				self.connection.commit()
		except Error as e:
			print("Error while connecting to MySQL" + str(e))

	def update_stocks(self, player_stocks):
		query = f"UPDATE config set stocks_price = {player_stocks}"
        self.cursor.execute(query)
        self.connection.commit()

    def func(self):
        query = f"SELECT * from queue"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()

        print(rows)

	def close(self):
		self.cursor.close()
		self.connection.close()

# c = Conn()