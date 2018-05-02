from Controller.Config import *
from Model.MainModel import *

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QLabel
from PyQt5.QtCore import pyqtSignal
from View.LoginWindowView import *


class TableList(QWidget, ConfigApplication):
    update_window = pyqtSignal(str)

    def __init__(self, root_window, connection_to_db):
        super().__init__(root_window)
        ConfigApplication.__init__(self)
        self.root_window = root_window
        #v_layout = QVBoxLayout(root_window)
        #v_layout.addWidget(self)
        #self.view = LoginWindowView(self)
        self.model = MainModel()

        self.root_window.setWindowTitle(self.windowTitle + " - Lista tabel")

    def run(self):
        '''
        Start drowing window
        :return:
        '''
        self.view.initDraw(self.getMinimalWidth(), self.getMinimalHeight())
        self.show()
        print("Jestem w TableList")
        self.root_window.update()