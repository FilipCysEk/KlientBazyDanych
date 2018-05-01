from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QObject, pyqtSignal

from Controller.Config import *

class RootWindow(QWidget):
    #Add signal
    #Dodanie sygnału
    update_window = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.configuration = ConfigApplication()
        self.setMinimumWidth(self.configuration.getMinimalWidth())
        self.setMinimumHeight(self.configuration.getMinimalHeight())
        self.resize(self.configuration.getMinimalWidth(), self.configuration.getMinimalHeight())

    def resizeEvent(self, QResizeEvent):
        pass

    def moveEvent(self, QMoveEvent):
        #print("SIalalalal")
        pass