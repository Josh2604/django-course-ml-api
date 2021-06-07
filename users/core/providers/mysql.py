import psycopg2


class Connector:
    def __init__(self, host: str, database: str, user: str, password: str, port: int):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = port
        self.__connection = None

    def connect(self):
        conn = None
        try:
            print("this is the credentials --", self.host)
            print("this is the credentials --", self.database)
            print("this is the credentials --", self.user)
            print("this is the credentials --", self.password)
            conn = psycopg2.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password,
                port=self.port,
            )
            print("The connection --", conn)
            self.__connection = conn
            return conn
        except(Exception, psycopg2.DatabaseError) as error:
            print("Error trying to connect to database: {} ".format(self.database), error)

    def close(self):
        if self.__connection is not None:
            print("connection closed")
            self.__connection.close()


class DBConnection:
    def __init__(self, connector: Connector):
        self.Connector = connector

    def create_connection(self):
        conn = self.Connector.connect()
        return conn

    def close_connection(self):
        self.Connector.close()
