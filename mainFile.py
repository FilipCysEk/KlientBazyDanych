#This is MainFile
#This file inicjalize all program

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import pyqtSlot

from Controller.Config import *
from View.LoginWindow import *
from View.RootWindow import RootWindow
from View.TableView import TableView


class MainClass:
    def __init__(self):
        self.main_window = RootWindow()

    def run(self):
        self.main_window = LoginWindow()
        self.connect_update_window(self.main_window)
        self.main_window.run()

    def connect_update_window(self, window):
        window.update_window.connect(self.slot_update_window)

    #@pyqtSlot(int)
    def slot_update_window(self, name):
        print("Dobre sygnały")
        if name == 2:
            self.main_window = TableView()
            self.main_window.run()

app = QApplication(sys.argv)
main = MainClass()
main.run()
sys.exit(app.exec_())