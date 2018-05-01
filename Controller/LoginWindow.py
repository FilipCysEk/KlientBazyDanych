from Controller.Config import *


import csv
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QLabel
from View.LoginWindowView import *


class LoginWindow(QWidget, ConfigApplication):
    def __init__(self, root_window):
        super().__init__()
        ConfigApplication.__init__(self)
        self.root_window = root_window
        v_layout = QVBoxLayout(root_window)
        v_layout.addWidget(self)
        self.view = LoginWindowView(self)


        self.root_window.setWindowTitle(self.windowTitle + " - Logowanie")

    def run(self):
        '''
        Start drowing window
        :return:
        '''
        self.view.initDraw(self.getMinimalWidth(), self.getMinimalHeight())

        user_data = DataFileService()
        user_list = user_data.get_usernames_and_adress()

        self.view.drawUserList(user_list)

        self.root_window.show()

        self.view.new_user_label.mousePressEvent = self.addNewUser

    def updateUserList(self):
        user_data = DataFileService()
        user_list = user_data.get_usernames_and_adress()
        self.view.drawUserList(user_list)
        self.update()

    def addNewUser(self, event):
        print("Nowe Okienko")
        self.view.newUserWindow()
        self.view.buttonTest.clicked.connect(self.testConnection)
        self.view.buttonOK.clicked.connect(self.acceptAddNewUser)

    def testConnection(self):
        self.view.passwordWindow()


    def acceptAddNewUser(self):
        user_data = DataFileService()
        print("Sprawdzam txt")

        if len(self.view.line1_username.text()) > 3 and len(self.view.line2_host.text()) > 3 and len(self.view.line3_db.text()) > 3:
            if user_data.addNewUser(self.view.line1_username.text(), self.view.line2_host.text(), self.view.line3_db.text()):

                self.updateUserList()
                #print(self.view.line1_username.text(), self.view.line2_host.text(), self.view.line3_db.text())

            self.view.dialog.close()
            self.view.dialog.destroy()



    def resizeEvent(self, QResizeEvent):
        self.view.centeringUserListWidget()

class DataFileService:
    '''
        Class to read from file user date (name, password, database, etc)
        In file:
        - database username
        - database address
        - database password
        - database name
    '''

    def __init__(self):
        self.userDataFile = []
        self.userDataEmpty = False
        try:
            file = open('.users.csv', 'r', newline = '', encoding = 'utf-8')
            with file as userDataFile:
                reade = csv.reader(userDataFile)

                for row in reade:
                    self.userDataFile.append([row[0], row[1], row[2]])

        except csv.Error as err:
            print(err)
            exit(1)
        except OSError as err:
            self.userDataEmpty = True
            if err.errno != 2:
                print(err)
                exit(1)

    def get_usernames_and_adress(self):
        if self.userDataEmpty:
            return []
        else:
            temp_array = []
            for row in self.userDataFile:
                temp_array.append((row[0], row[1]))

            return temp_array

    def addNewUser(self, username, host, database):
        try:
            file = open('.users.csv', 'a', newline = '', encoding = 'utf-8')
            with file as userDataFile:
                writ = csv.writer(userDataFile)
                writ.writerow([username, host, database])
                return True

        except csv.Error as err:
            print(err)
            exit(1)
        except OSError as err:
            self.userDataEmpty = True
            if err.errno != 2:
                print(err)
                exit(1)