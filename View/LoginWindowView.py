from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QScrollArea, QGridLayout, QLineEdit, QPushButton, QButtonGroup, QMessageBox
from PyQt5.QtWidgets import QHBoxLayout, QDialog, QDialogButtonBox

class LoginWindowView:
    def __init__(self, window):
        self.main_widget = window

    def __del__(self):
        #if self.main_widget in :
        self.user_list_widget.deleteLater()
        self.user_scroll.deleteLater()
        self.main_widget.deleteLater()
        '''
        self.user_list_widget.destroy()
        self.user_scroll.destroy()
        self.main_widget.destroy()
        print("Ds")
        
        if self.user_scroll in self:
            self.user_scroll.destroy()

        if self.v_lay_user_list_widget in self:
            self.v_lay_user_list_widget.deleteLater()

        if self.new_user_label in self:
            self.new_user_label.deleteLater()

        if self.label_user_list in self:
            for i in range(0, len(self.label_user_list)):
                self.label_user_list[i].deleteLater()

        if self.dialog in self:
            self.dialog.destroy()

        if self.line1_username in self:
            self.line1_username.deleteLater()

        if self.line2_host in self:
            self.line2_host.deleteLater()

        if self.line3_db in self:
            self.line3_db.deleteLater()

        if self.line2_host in self:
            self.line2_host.deleteLater()

        if self.buttonOK in self:
            self.buttonOK.deleteLater()

        if self.buttonTest in self:
            self.buttonTest.deleteLater()

        if self.dialog_layout in self:
            self.dialog_layout.deleteLater()

        if self.passWindow in self:
            self.passWindow.destroy()

        if self.line_pass in self:
            self.line_pass.deleteLater()

        if self.passWindow_buttons in self:
            self.passWindow_buttons.destroy()

        if self.login_window in self:
            self.login_window.destroy()

        if self.line1_login_window in self:
            self.line1_login_window.deleteLater()

        if self.button_delete_login_window in self:
            self.button_delete_login_window.deleteLater()

        if self.button_login_window in self:
            self.button_login_window.destroy()
        '''


    def initDraw(self, width, height):
        self.main_widget.setMinimumWidth(width)
        self.main_widget.setMinimumHeight(height)

        self.user_scroll = QScrollArea(self.main_widget)
        self.user_scroll.setWidgetResizable(True)
        self.user_list_widget = QWidget(self.user_scroll)

        self.user_list_size = [300,400]
        self.centeringUserListWidget()
        self.label_user_list = []

        #self.user_list_widget.setStyleSheet("background-color:#F00")
        self.user_list_widget.setStyleSheet("background-color: rgba(0, 0, 0, 0.1)")

        self.v_lay_user_list_widget = QVBoxLayout()
        self.user_list_widget.setLayout(self.v_lay_user_list_widget)

        #self.background_user_button = "background-color: rgba(0, 0, 0, 0.1)"
        self.background_user_button = "background-color: #EEE"

        self.new_user_label = QLabel(self.user_list_widget)
        self.new_user_label.setText("+ Dodaj nowego użytkownika")
        self.new_user_label.setFixedHeight(40)
        self.new_user_label.setFixedWidth(self.user_list_size[0] - 40)
        #self.new_user_label.move(10, 0)
        self.new_user_label.setStyleSheet(self.background_user_button)
        #self.new_user_label.mousePressEvent = self.clickedButton

        self.v_lay_user_list_widget.addWidget(self.new_user_label)
        #self.v_lay_user_list_widget.addStretch()


    def centeringUserListWidget(self):
        win = [self.main_widget.width(), self.main_widget.height()]
        self.user_scroll.setGeometry(int((win[0] - self.user_list_size[0]) / 2), int((win[1] - self.user_list_size[1]) / 2),
                                          self.user_list_size[0], self.user_list_size[1])

    def drawUserList(self, userList):
        if len(self.label_user_list) != 0:
            for i in range(0, len(self.label_user_list)):
                self.label_user_list[i].deleteLater()

        self.label_user_list  = []
        if len(userList) == 0:
            self.v_lay_user_list_widget.addStretch()
        else:
            for row in userList:
                temp = QPushButton(self.user_list_widget)
                temp.setText(row[0] + "@" + row[1])
                temp.setFixedHeight(40)
                temp.setFixedWidth(self.user_list_size[0] - 40)
                temp.setStyleSheet(self.background_user_button)
                #temp.setStyleSheet("background-color:rgba(255, 0, 0, 0)")

                self.label_user_list.append(temp)

            '''
            for row in self.label_user_list:
                self.v_lay_user_list_widget.addWidget(row)
                .clicked.connect(lambda: self.test(tempi))
                tempi += 1
            '''

            for i in range(0, len(self.label_user_list)):
                self.v_lay_user_list_widget.addWidget(self.label_user_list[i])

            self.v_lay_user_list_widget.addStretch()
            self.user_scroll.setWidget(self.user_list_widget)

    def clickedButton(self, event):
        print("ClicketButton")

    def test(self):
        temp = self.user_list_widget.sender()
        for i in range(0, len(self.label_user_list)):
            if self.label_user_list == temp:
                print()
        print(temp, " - ", temp.text())


    def newUserWindow(self):
        self.dialog = QWidget()
        self.dialog.setFixedWidth(400)
        self.dialog.setFixedHeight(250)
        self.dialog_layout = QGridLayout()
        self.dialog_layout.setSpacing(10)
        self.dialog.setWindowTitle("Dodawanie nowego użytkownika")

        lab1_username = QLabel(self.dialog)
        lab1_username.setText("Podaj nazwę użytkownika:")
        self.line1_username = QLineEdit(self.dialog)
        self.line1_username.setPlaceholderText("np. Mietek")

        lab2_host = QLabel(self.dialog)
        lab2_host.setText("Podaj adres serwera:")
        self.line2_host = QLineEdit(self.dialog)
        self.line2_host.setPlaceholderText("np. localhost")

        lab3_db = QLabel(self.dialog)
        lab3_db.setText("Podaj nazwę bazy:")
        self.line3_db = QLineEdit(self.dialog)
        self.line3_db.setPlaceholderText("np. Tajna baza NASA")

        self.buttonOK = QPushButton(self.dialog)
        self.buttonOK.setText("Dodaj")
        buttonCancel = QPushButton(self.dialog)
        buttonCancel.setText("Anuluj")
        self.buttonTest = QPushButton(self.dialog)
        self.buttonTest.setText("Testuj połączenie")

        buttonCancel.clicked.connect(self.newUserWindowCancelButton)

        self.dialog_layout.addWidget(lab1_username, 1, 0)
        self.dialog_layout.addWidget(self.line1_username, 1, 1, 1, 2)

        self.dialog_layout.addWidget(lab2_host, 2, 0)
        self.dialog_layout.addWidget(self.line2_host, 2, 1, 1, 2)

        self.dialog_layout.addWidget(lab3_db, 3, 0)
        self.dialog_layout.addWidget(self.line3_db, 3, 1, 1, 2)

        self.dialog_layout.addWidget(self.buttonTest, 4, 2)
        self.dialog_layout.addWidget(self.buttonOK,5, 1)
        self.dialog_layout.addWidget(buttonCancel, 5, 2)

        self.line1_username.text()
        self.dialog.setLayout(self.dialog_layout)
        self.dialog.show()

    def newUserWindowCancelButton(self):
        self.dialog.close()
        self.dialog.destroy()

    def passwordWindow(self, parent):
        self.passWindow = QDialog(parent)

        passWindow_label = QLabel(self.passWindow)
        passWindow_label.setText("Podaj Hasło")

        self.line_pass = QLineEdit(self.passWindow)
        self.line_pass.setEchoMode(QLineEdit.Password)

        self.passWindow.setFixedHeight(120)
        self.passWindow.setFixedWidth(300)

        passWindow_v_lay = QVBoxLayout(self.passWindow)
        self.passWindow.setLayout(passWindow_v_lay)

        passWindow_v_lay.addWidget(passWindow_label)
        passWindow_v_lay.addWidget(self.line_pass)

        self.passWindow_buttons = QDialogButtonBox(self.passWindow)
        self.passWindow_buttons.addButton(QDialogButtonBox.Ok)
        self.passWindow_buttons.addButton(QDialogButtonBox.Cancel)
        self.passWindow_buttons.button(QDialogButtonBox.Cancel).clicked.connect(self.passWindowCancelEvent)

        passWindow_v_lay.addWidget(self.passWindow_buttons)



        self.passWindow.show()

    def passWindowCancelEvent(self, event):
        self.passWindow.close()
        self.passWindow.destroy()

    def messageOK(self, text, text2 = None, parrent = None):
        message = QMessageBox(parrent)
        message.setText(text)
        message.setInformativeText(text2)
        message.setIcon(QMessageBox.Information)
        message.show()

    def messageBad(self, text, text2 = None, parrent = None):
        message = QMessageBox(parrent)
        message.setText(text)
        message.setInformativeText(text2)
        message.setIcon(QMessageBox.Critical)
        message.show()

    def messageNeutral(self, text, text2 = None, parrent = None):
        message = QMessageBox(parrent)
        message.setText(text)
        message.setInformativeText(text2)
        message.show()

    def loginWindow(self, username, host, db):
        self.login_window = QDialog()
        self.login_window.setWindowTitle("Logowanie do " + username + "@" + host)
        self.login_window.setFixedWidth(300)
        self.login_window.setFixedHeight(200)
        self.data_login_window = [username, host, db]

        label1_login_window = QLabel(self.login_window)
        label2_login_window = QLabel(self.login_window)
        label3_login_window = QLabel(self.login_window)
        label1_login_window.setText("<h2>Chcesz się zalogować do:</h2>")
        label2_login_window.setText("Nazwa użytkownika:\t" + username +
                                    "\nHost:\t\t\t" + host +"\nBaza:\t\t\t" + db)
        label3_login_window.setText("Podaj hasło:")

        self.line1_login_window = QLineEdit(self.login_window)
        self.line1_login_window.setEchoMode(QLineEdit.Password)

        self.button_delete_login_window = QPushButton(self.login_window)
        self.button_delete_login_window.setText("Usuń to konto")

        self.button_login_window = QDialogButtonBox(self.login_window)
        self.button_login_window.addButton(self.button_delete_login_window, QDialogButtonBox.AcceptRole)
        self.button_login_window.addButton(QDialogButtonBox.Ok)
        self.button_login_window.addButton(QDialogButtonBox.Cancel)

        self.button_login_window.button(QDialogButtonBox.Cancel).clicked.connect(self.loginWindowCancelEvent)

        #self.button_login_window.(QDialogButtonBox.MacLayout)

        v_lay_login_window = QVBoxLayout(self.login_window)
        self.login_window.setLayout(v_lay_login_window)

        v_lay_login_window.addWidget(label1_login_window)
        v_lay_login_window.addWidget(label2_login_window)
        v_lay_login_window.addWidget(label3_login_window)
        v_lay_login_window.addWidget(self.line1_login_window)
        v_lay_login_window.addStretch()
        v_lay_login_window.addWidget(self.button_login_window)

        self.login_window.show()

    def loginWindowCancelEvent(self, event):
        self.login_window.close()
        self.login_window.destroy()
