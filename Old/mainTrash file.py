

        #rootWindow.resize(configuration.getMinimalWidth(), configuration.getMinimalHeight())

@pyqtSlot(str)
def slot_update_window(name):
    print("Dobre sygnały")
    if name == 2:
        main_window = TableView()
        main_window.run()


app = QApplication(sys.argv)
main_window = RootWindow()
main_window.update_window.connect(slot_update_window)
'''
rootWindow = QWidget()
rootWindow.setMinimumWidth(configuration.getMinimalWidth())
rootWindow.setMinimumHeight(configuration.getMinimalHeight())
rootWindow.resize(configuration.getMinimalWidth(), configuration.getMinimalHeight())
'''
main_window = LoginWindow()
main_window.update_window.connect(slot_update_window)
#rootWindow.resizeEvent(test.set_users_lsit_widget())
#rootWindow.resizeEvent()
main_window.run()



sys.exit(app.exec_())