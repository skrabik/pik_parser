from config import  DB_HOST, DB_USER, DB_PASSWORD, DB_NAME, DB_ENGIN, DB_PORT
from sqlalchemy import create_engine, text

class DB:
    def __init__(self):
        self.db_name = DB_NAME
        self.db_host = DB_HOST
        self.db_port = DB_PORT
        self.db_user = DB_USER
        self.db_password = DB_PASSWORD
        self.db_engine = DB_ENGIN

    def get_connection_string(self):
        return self.db_engine + "://" + self.db_host + ":" + self.db_port + "/" + self.db_name + "?password=" + self.db_password + "&user=" + self.db_user

    def connect(self):
        engine = create_engine(self.get_connection_string(),
                                          pool_size=10,
                                          max_overflow=2,
                                          pool_recycle=300,
                                          pool_pre_ping=True,
                                          pool_use_lifo=True)
        self.connection = engine.connect()
        return self

    def select(self, query_string):
        return self.connection.execute(text(query_string))

    def insert(self, query_string):
        self.connection.execute(text(query_string))
        return self.connection.commit()

