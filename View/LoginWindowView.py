from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QScrollArea, QGridLayout, QLineEdit, QPushButton, QButtonGroup

class LoginWindowView:
    def __init__(self, window):
        self.main_widget = window

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
        self.background_user_button = "background-color: rgba(0, 0, 0, 0)"

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
                temp = QLabel(self.user_list_widget)
                temp.setText(row[0] + "@" + row[1])
                temp.setFixedHeight(40)
                temp.setFixedWidth(self.user_list_size[0] - 40)
                temp.setStyleSheet(self.background_user_button)
                self.label_user_list.append(temp)

            for row in self.label_user_list:
                self.v_lay_user_list_widget.addWidget(row)

            self.v_lay_user_list_widget.addStretch()
            self.user_scroll.setWidget(self.user_list_widget)

    def clickedButton(self, event):
        print("ClicketButton")


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