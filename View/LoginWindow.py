from Controller.Config import *
from View.RootWindow import RootWindow


import sys
import hashlib
import csv
from PyQt5.QtGui import QColor, QResizeEvent
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QBoxLayout, QLayout, QHBoxLayout, QVBoxLayout, QPushButton
from PyQt5.QtCore import Qt, pyqtSignal


class LoginWindow(RootWindow, ConfigApplication):

    # Add signal
    # Dodanie sygnału
    update_window = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        ConfigApplication.__init__(self)
        print(self.windowTitle)


        self.app = None
        #self.root_window = root_window
        self.user_data = DataFileService()

        #self.root_window.resizeEvent(self.set_users_lsit_widget())

    #def self.root_window.resizeEvent(self):
     #   print("test")

    def run(self):
        '''
        After initialize class, you must run this, to start running application
        :return: nothing
        '''
        self.setWindowTitle(self.windowTitle + " - Logowanie")

        user_list = self.user_data.get_usernames_and_adress()

        #root_window_size = [self.root_window.width(), self.root_window.height()]
        self.user_list_widget_size = [200, 300]

        self.user_list_widget = QWidget(self)
        #user_list_widget.setGeometry(int((root_window_size[0]-user_list_widget_size[0])/2),int((root_window_size[1]-user_list_widget_size[1])/2),
         #                            user_list_widget_size[0], user_list_widget_size[1])

        self.set_users_lsit_widget()

        self.user_list_widget.setStyleSheet("background-color:#F00")
#        self.user_list_widget.resizeEvent(set_users_list_widget)

        if user_list == None:
            print("Empty list")
        else:
            pass

        button = QPushButton(self)
        button.setText("Inne Okno")
        button.clicked.connect(self.buttonNewLook)

        self.render()

    def set_users_lsit_widget(self):
        root_window_size = [self.width(), self.height()]
        self.user_list_widget.setGeometry(int((root_window_size[0] - self.user_list_widget_size[0]) / 2),
                                     int((root_window_size[1] - self.user_list_widget_size[1]) / 2),
                                     self.user_list_widget_size[0], self.user_list_widget_size[1])

    def resizeEvent(self, QResizeEvent):
        self.set_users_lsit_widget()
        #print("Success")

    def render(self):
        '''
        Refresh window
        :return: nothing
        '''

        self.show()

    def buttonNewLook(self):
        print("Nie wiem")
        self.update_window.emit(2)


class DataFileService:
    '''
        Class to read from file user date (name, password, database, etc)
        In file:
        - database username
        - database address
        - database password
    '''

    def __init__(self):
        self.userDataFile = None
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
            return None
        else:
            temp_array = None
            for row in self.userDataFile:
                temp_array.append((row[0], row[1]))

            return temp_array
