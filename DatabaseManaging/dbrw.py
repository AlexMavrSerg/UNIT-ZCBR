from mysql.connector import connect, Error
from .info import *

class DatabaseReader(object):
#    def __new__(cls):
#        if not hasattr(cls, 'instance'):
#            cls.instance = super(DatabaseReader, cls).__new__(cls)
#        return cls.instance

    def __init__(self, *, host=None, user=None, database=None, password=None, table=None, exceptions=True, log = False):
        self.host = info.hosts if host is None else host
        self.user = info.users if user is None else user
        self.database = info.databases if database is None else database
        self.password = info.passwords if password is None else password
        self.table = info.table if table is None else table
        self.exceptions = exceptions

        self.log = log

        self.__plog("connecting to database '{}'".format(self.database))
        self.connection = connect(host=self.host, user=self.user, database=self.database, password=self.password)
        self.__plog("connected to database '{}'".format(self.database))

    def setTable(self, table):
        self.table = table

    def read(self, name: str): # Возвращает одну строку или список строк (если как имя было указано __ALLPOSTS__)
        if not isinstance(name, str):
            if self.exceptions:
                raise DatabaseException("name should be a string but it's " + str(type(name)) + "!\n")
            else:
                return None
        result = None
        if name == "__ALLPOSTS__":
            query = """SELECT * FROM {};""".format(self.table)
            with self.connection.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchall()
            return result
        else:
            result = self.__read(name)
            return result


    def __read(self, name: str) -> str:
        result = None
        query = "SELECT * FROM {} WHERE name = %s".format(self.table)
        with self.connection.cursor() as cursor:
            cursor.execute(query, (name,))
            result = cursor.fetchone()
        return result

    def fieldExists(self, name: str) -> bool:
        result = self.__read(name)
        if not result: return False
        return True

    def __plog(self, *args, **kwargs):
        if self.log:
            print("\033[33mDatabaseReader:{}:{}: ".format(self, self.database), end="")
            print(*args, **kwargs)
            print("\033[0m")


class DatabaseWriter(object):
#    def __new__(cls):
#        if not hasattr(cls, 'instance'):
#            cls.instance = super(DatabaseReader, cls).__new__(cls)
#        return cls.instance
    
    def __init__(self, *, host=None, user=None, database=None, password=None, table=None, exceptions=True, log = False):
        self.host = info.hosts if host is None else host
        self.user = info.users if user is None else user
        self.database = info.databases if database is None else database
        self.password = info.passwords if password is None else password
        self.table = info.table if table is None else table

        self.exceptions = exceptions
        self.log = log

        self.__plog("connecting to database '{}'".format(self.database))
        self.connection = connect(host=self.host, user=self.user, database=self.database, password=self.password)
        self.connection.autocommit = True
        self.__plog("onnected to database '{}'".format(self.database))
    
    def setTable(self, table):
        self.table = table
    
    def __fieldExists(self, name: str) -> bool:
        result = None
        with self.connection.cursor() as cursor:
            query = "SELECT * FROM {} WHERE name = %s".format(self.table)
            cursor.execute(query, (name,))
            result = cursor.fetchone()
        if not result: return False
        return True            

    def addField(self, name: str, content: str, rewrite=True) -> bool: # 0 если запись была добавлена, 1 если она уже существует и записи добавлено не было (поиск по имени)
        if self.__fieldExists(name):
            if not rewrite:
                raise DatabaseException("There is already exists the '{}' field".format(name))
            else:
                self.deleteField(name)
        
        with self.connection.cursor() as cursor:
            query = "INSERT INTO {} (name, data) VALUES (%s, %s)".format(self.table)
            cursor.execute(query, (name, content))
            self.__plog("inserted {} into {}".format(content, self.table))

    def deleteField(self, name: str) -> bool: # 0 в случае удаления, 1 в случае, если записи не существовало, и удалить её невозможно
        with self.connection.cursor() as cursor:
            query = "DELETE FROM {} WHERE name = %s".format(self.table)
            cursor.execute(query, (name,))
            self.__plog("deleted '{}' from {}".format(name, self.table))

    def __plog(self, *args, **kwargs):
        if self.log:
            print("\033[33mDatabaseWriter:{}:{}: ".format(self, self.database), end="")
            print(*args, **kwargs)
            print("\033[0m")

class DatabaseException(Exception):
    def __init__(self, message):
        self.txt = message