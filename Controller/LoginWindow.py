from Controller.Config import *
from Model.MainModel import *


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
        self.model = MainModel()


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

        for i in range(0, len(self.view.label_user_list)):
            self.view.label_user_list[i].clicked.connect(self.connectToDb)

        self.root_window.show()

        self.view.new_user_label.mousePressEvent = self.addNewUser

    def updateUserList(self):
        user_data = DataFileService()
        user_list = user_data.get_usernames_and_adress()
        self.view.drawUserList(user_list)
        for i in range(0, len(self.view.label_user_list)):
            self.view.label_user_list[i].clicked.connect(self.connectToDb)
        self.update()

    def addNewUser(self, event):
        self.view.newUserWindow()
        self.view.buttonTest.clicked.connect(self.testConnection)
        self.view.buttonOK.clicked.connect(self.acceptAddNewUser)

    def testConnection(self):
        self.view.passwordWindow(self.view.dialog)
        self.view.passWindow_buttons.button(QDialogButtonBox.Ok).clicked.connect(self.testConnection2)

    def testConnection2(self):
        res = self.model.testConnection(self.view.line1_username.text(), self.view.line2_host.text(), self.view.line_pass.text(),
                                        self.view.line3_db.text())
        #print(str(res))
        if res == True:
            self.view.messageOK("Wszystko w porządku!!", "", self.view.passWindow)
        else:
            self.view.messageBad("Mamy tu jakiś problem!!", str(res), self.view.passWindow)

        self.view.passWindow.close()
        self.view.passWindow.destroy()

    def acceptAddNewUser(self):
        user_data = DataFileService()
        #print("Sprawdzam txt")

        if len(self.view.line1_username.text()) > 3 and len(self.view.line2_host.text()) > 3 and len(self.view.line3_db.text()) > 3:
            if user_data.addNewUser(self.view.line1_username.text(), self.view.line2_host.text(), self.view.line3_db.text()):

                self.updateUserList()
                #print(self.view.line1_username.text(), self.view.line2_host.text(), self.view.line3_db.text())

            self.view.dialog.close()
            self.view.dialog.destroy()

    def connectToDb(self):
        clicked_label = self.view.user_list_widget.sender()
        for i in range(0, len(self.view.label_user_list)):
            if clicked_label == self.view.label_user_list[i]:
                user_data = DataFileService()
                user_list = user_data.get_usernames_and_adress()
                #print(user_list[i])
                self.view.loginWindow(user_list[i][0], user_list[i][1], user_list[i][2])

                #self.view.button_delete_login_window.clicked.connect(self.deleteAccount(user_list[i]))
                self.view.button_delete_login_window.clicked.connect(self.deleteAccount)

                break

    #def deleteAccount(self, data_user):
    def deleteAccount(self):
        data_user = self.view.login_window.sender()
        #print(self.view.data_login_window)
        if QMessageBox.question(self.view.login_window, "Potwierdzenie", "Czy na pewno chcesz usunąć to konto?",
                                QMessageBox.Yes | QMessageBox.No) == QMessageBox.Yes:
            data_file = DataFileService()
            if data_file.deleteUser(self.view.data_login_window[0], self.view.data_login_window[1], self.view.data_login_window[2]):
                pass

            self.view.login_window.close()
            self.updateUserList()
        #self.view.confirmWindow("Czy na pewno chcesz usunąć to konto?")

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
                temp_array.append((row[0], row[1], row[2]))

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

    def deleteUser(self, username, host, db):
        data_users = self.get_usernames_and_adress()

        try:
            file = open('.users.csv', 'w', newline = '', encoding = 'utf-8')
            with file as userDataFile:

                for row in data_users:
                    if row[0] == username and row[1] == host and row[2] == db:
                        continue
                    else:
                        writ = csv.writer(userDataFile)
                        writ.writerow([row[0], row[1], row[2]])
                return True

        except csv.Error as err:
            print(err)
            exit(1)
        except OSError as err:
            self.userDataEmpty = True
            if err.errno != 2:
                QMessageBox.information(None, "Błąd!", "Błąd pliku!!\n" + err, QMessageBox.Ok)
                print(err)
                exit(1)