#This is MainFile
#This file inicjalize all program

import sys
from PyQt5.QtWidgets import QApplication, QWidget

from Controller.Config import *
from View.LoginWindow import *


        #rootWindow.resize(configuration.getMinimalWidth(), configuration.getMinimalHeight())



app = QApplication(sys.argv)
'''
rootWindow = QWidget()
rootWindow.setMinimumWidth(configuration.getMinimalWidth())
rootWindow.setMinimumHeight(configuration.getMinimalHeight())
rootWindow.resize(configuration.getMinimalWidth(), configuration.getMinimalHeight())
'''
test = LoginWindow()
#rootWindow.resizeEvent(test.set_users_lsit_widget())
#rootWindow.resizeEvent()
test.run()



sys.exit(app.exec_())