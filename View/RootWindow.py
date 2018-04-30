from PyQt5.QtWidgets import QWidget
from Controller.Config import *

class RootWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.configuration = ConfigApplication()
        self.setMinimumWidth(self.configuration.getMinimalWidth())
        self.setMinimumHeight(self.configuration.getMinimalHeight())
        self.resize(self.configuration.getMinimalWidth(), self.configuration.getMinimalHeight())