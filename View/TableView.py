from Controller.Config import *
from View.RootWindow import RootWindow


import sys
import hashlib
import csv
from PyQt5.QtGui import QColor, QResizeEvent
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QBoxLayout, QLayout, QHBoxLayout, QVBoxLayout, QPushButton


class TableView(RootWindow, ConfigApplication):
    def __init__(self):
        super().__init__()
        ConfigApplication.__init__(self)
        print(self.windowTitle,"             ------ :D")


        self.app = None
    def run(self):
        '''
        After initialize class, you must run this, to start running application
        :return: nothing
        '''
        self.setWindowTitle(self.windowTitle + " - Tabele")
        label = QLabel(self)
        label.setText("Inne okno!!?")


        self.render()

    def resizeEvent(self, QResizeEvent):
        print("Success")

    def render(self):
        '''
        Refresh window
        :return: nothing
        '''

        self.show()

