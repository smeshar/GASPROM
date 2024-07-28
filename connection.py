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
                self.connection.commit()

        except Error as e:
            print("Error while connecting to MySQL" + str(e))

    def login(self, name: str, password: str):
        query = f"SELECT password, balance, player_stocks, elec, storymode FROM users WHERE name = '{name}'"
        self.cursor.execute(query)

        rows = self.cursor.fetchall()
        if len(rows) == 0:
            print(" Несуществующий пользователь")
            return []

        print(rows)

        passw = rows[0][0]
        if passw != password:
            print(" Неверный пароль")
            return []

        return rows[0]

    def register(self, name, password, balance, player_stocks, elec, storymode):
        query = f"SELECT * FROM users WHERE name = '{name}'"
        self.cursor.execute(query)
        if len(self.cursor.fetchall()) != 0:
            print(self.cursor.fetchall())
            print("Пользователь с таким никнеймом уже существует")
            return 0

        query = f"""INSERT INTO users (name, password, balance, player_stocks, elec, storymode)
                VALUES ('{name}', '{password}', {balance}, {player_stocks}, {elec}, {storymode})
                """
        self.cursor.execute(query)
        self.connection.commit()
        return 1

    def update(self):
        query = f"SELECT * FROM config"
        self.cursor.execute(query)

        rows = self.cursor.fetchone()
        if len(rows) == 0:
            print("Error update config database")

        return rows


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