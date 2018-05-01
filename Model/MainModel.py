import mysql.connector
from mysql.connector import errorcode

class MainModel:
    def __init__(self):
        pass

    def testConnection(self, user, host, passw, database):
        try:
            connection = mysql.connector.connect(host=host, user=user, password=passw, database=database)
            return True

        except mysql.connector.Error as err:
            return err
            print(err)

