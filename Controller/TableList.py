from Controller.Config import *
from Model.MainModel import *

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QLabel, QButtonGroup, QSizePolicy
from PyQt5.QtCore import pyqtSignal
from View.TableListView import *


class TableList(QWidget, ConfigApplication):
    update_window = pyqtSignal(str)

    def __init__(self, root_window, connection_to_db):
        super().__init__(root_window)
        ConfigApplication.__init__(self)
        self.root_window = root_window
        self.v_layout = root_window.layout()
        self.v_layout.addWidget(self)
        #self.v_layout = QVBoxLayout()
        print(self.v_layout.sizeHint())

        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.setStyleSheet("background-color:#00F")

        print(self.geometry())
        print(self.v_layout.geometry())

        self.view = TableListView(self, self.root_window)
        self.model = MainModel()

        self.root_window.setWindowTitle(self.windowTitle + " - Lista tabel")

    def __del__(self):
        self.button_group.deleteLater()

    def run(self):
        '''
        Start drowing window
        :return:
        '''
        self.view.initDraw(self.getMinimalWidth(), self.getMinimalHeight())
        self.show()
        print("Jestem w TableList")
        self.root_window.update()
        self.root_window.show()

    def resizeEvent(self, QResizeEvent):
        #self.setFixedWidth(self.root_window.width())
        #self.setFixedHeight(self.root_window.height())
        print(self.geometry())