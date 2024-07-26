import mysql.connector
from mysql.connector import Error

class Conn():
    def __init__(self):
        hostname = "wn9.h.filess.io"
        database = "smeshar_evercryaid"
        port = "3307"
        username = "smeshar_evercryaid"
        password = "3f9bfbd77435c3f029a645427b5abc9292725f40"

        try:
            self.connection = mysql.connector.connect(host=hostname, database=database, user=username, password=password,
                                                 port=port)
            if self.connection.is_connected():
                db_Info = self.connection.get_server_info()
                print("Connected to MySQL Server version ", db_Info)
                self.cursor = self.connection.cursor()
                self.cursor.execute("select database();")
                record = self.cursor.fetchone()
                print("You're connected to database: ", record)

                self.cursor.execute("""
                CREATE TABLE users (
                    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
                    name VARCHAR(30),
                    password VARCHAR(30),
                    balance DOUBLE,
                    k DOUBLE,
                    elec DOUBLE,
                    storymode,
                    
                )
                """)
                self.connection.commit()

        except Error as e:
            print("Error while connecting to MySQL" + str(e))

    def login(self, name: str, password: str):
        query = f"SELECT password, crypto_bal, bal FROM users WHERE name = '{name}'"
        self.cursor.execute(query)

        rows = self.cursor.fetchall()
        if rows is None:
            print("Несуществующий пользователь")
            return []

        l = list()

        passw = rows[0][0]
        if passw != password:
            print("Неверный пароль")
            return []

        return rows[0]

    # def register(self, name, password, ):


    def fetch_all(self) -> [list]:
        query = "SELECT * FROM users"
        self.cursor.execute(query)

        rows = self.cursor.fetchall()
        l = list()

        for row in rows:
            l.append(row)

        return l

    def close(self):
        self.cursor.close()
        self.connection.close()

c = Conn()