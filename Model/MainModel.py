import mysql.connector
from mysql.connector import errorcode

class MainModel:
    def __init__(self):
        pass

    def testConnection(self, user, host, passw, database):
        try:
            connection = mysql.connector.connect(host=host, user=user, password=passw, database=database)
            connection.close()
            return True

        except mysql.connector.Error as err:
            return err
            print(err)

    def makeConnection(self, user, host, passw, database):
        try:
            self.connection = mysql.connector.connect(host=host, user=user, password=passw, database=database)
            return True

        except mysql.connector.Error as err:
            return err
            print(err)

    def closeConnection(self):
        self.connection.close()