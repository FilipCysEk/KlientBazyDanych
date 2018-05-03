from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QScrollArea, QGridLayout, QLineEdit, QPushButton, QButtonGroup, QMessageBox
from PyQt5.QtWidgets import QHBoxLayout, QDialog, QDialogButtonBox

class TableListView:
    def __init__(self, window, root_window):
        self.main_widget = window
        self.root_window = root_window

        self.drawToolBar()

    def __del__(self):
        self.main_widget_draw_area.deleteLater()
        self.scrollable.deleteLater()
        self.scrollable_v_lay.deleteLater()
        self.main_widget.deleteLater()
        self.button_group_toolbar.deleteLater()

    def initDraw(self, width, height):
        self.main_widget.setMinimumWidth(width)
        self.main_widget.setMinimumHeight(height)

        self.scrollable = QScrollArea(self.main_widget)
        self.scrollable.move(0, 70)
        self.scrollable_v_lay = QVBoxLayout()
        self.scrollable.setLayout(self.scrollable_v_lay)
        self.main_widget_draw_area = QWidget(self.main_widget)
        self.scrollable_v_lay.addWidget(self.main_widget_draw_area)

        self.main_widget.show()
        pass

    def drawToolBar(self):
        self.button_group_toolbar = QButtonGroup(self.main_widget)

        self.search_b_g_tb = QPushButton(self.main_widget)
        self.search_b_g_tb.setText("Konsola SQL")

        self.button_group_toolbar.addButton(self.search_b_g_tb)

