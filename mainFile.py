#This is MainFile
#This file inicjalize all program

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import pyqtSlot

from Controller.Config import *
#from View.RootWindow import RootWindow
from View.TableView import TableView
from Controller.LoginWindow import LoginWindow
from Controller.TableList import TableList
from Model.MainModel import MainModel


class MainClass:
    def __init__(self):
        #self.main_window = RootWindow()
        self.main_window = QWidget()
        self.main_window.closeEvent = self.closeEvent
        self.connection_to_db = None

    def run(self):
        self.main_window_content = LoginWindow(self.main_window)
        self.connect_update_window(self.main_window_content)
        self.main_window_content.run()

    def connect_update_window(self, window):
        window.update_window.connect(self.slot_update_window)

    #@pyqtSlot(int)
    def slot_update_window(self, name):
        #print("Dobre sygnały")
        if name == "table_list":
            #self.main_window.destroy()
            #del self.main_window
            #self.main_window.deleteLater()
            self.connection_to_db = self.main_window_content.connection_to_db
            self.main_window_content = TableList(self.main_window)
            self.main_window_content.run()

    def closeEvent(self, event):
        if self.connection_to_db != None:
            model = MainModel()
            model.connection = self.connection_to_db
            model.closeConnection()


app = QApplication(sys.argv)
main = MainClass()
main.run()
sys.exit(app.exec_())
