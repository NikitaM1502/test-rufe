from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import(
    QApplication, QtWidget,
    QHBoxLayout, QVBoxLayout,
    QGroupBox, QRadioButton,
    QPushButton, QLabel, QListWidget, QLineEdit
)

from instr import *
from final_win import*

class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.connects()
        self.set_appear()
        self.show()

    def next_click(self):
        self.tw = TestWin()
        self.hide()

    def connects(self):
        self.btn_next.clicked.connects(self.next_click)

    def set_appear(self):
        self.setWidgetTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def initUI(self):
        self.btn_next = QPushButton(txt_sendresalts, self)
        self.btn_test1 = QPushButton(txt_starttest1, self)
        self.btn_test2 = QPushButton(txt_starttest3, self)
        self.btn_test3 = QPushButton(txt_starttest3, self)

        self.text_name = QLable(txt_name)
        self.text_age = QLable(txt_age)
        self.text_test1 = QLable(txt_test1)
        self.text_test2 = QLable(txt_test2)
        self.text_test3 = QLable(txt_test3)
        self.text_timer = QLable(txt_timer)

        self.line_name = QLineEdit(txt_hintname)

        self.line_age = QLineEdit(txt_hintage)

        self.line_test1 = QLineEdit(txt_hinttest1)

        self.line_test2 = QLineEdit(txt_hinttest2)

        self.line_test3 = QLineEdit(txt_hinttest3)

        self.l_line = QVBoxLayout()
        self.r_line = QVBoxLayout()
        self.h_line = QHBoxLayout()
        self.r_line.addWidget(self.text_timer, alignmet = QtAlignCenter)
        self.l_line.addWidget(self.text_name, alignmet = QtAlignLeft)
        self.l_line.addWidget(self.line_name, alignmet = QtAlignLeft)
        self.l_line.addWidget(self.text_age, alignmet = QtAlignLeft)
        self.l_line.addWidget(self.line_age, alignmet = QtAlignLeft)
        self.l_line.addWidget(self.text_test1, alignmet = QtAlignLeft)
        self.l_line.addWidget(self.btn_test1, alignmet = QtAlignLeft)
        self.l_line.addWidget(self.line_test1, alignmet = QtAlignLeft)
        self.l_line.addWidget(self.text_test2, alignmet = QtAlignLeft)
        self.l_line.addWidget(self.btn_test2, alignmet = QtAlignLeft)
        self.l_line.addWidget(self.text_test3, alignmet = QtAlignLeft)
        self.l_line.addWidget(self.btn_test3, alignmet = QtAlignLeft)
        self.l_line.addWidget(self.line_test2, alignmet = QtAlignLeft)
        self.l_line.addWidget(self.line_test3, alignmet = QtAlignLeft)
        self.l_line.addWidget(self.btn_next, alignmet = QtAligncenter)
        self.h_line.addLoyout(self.l_line)
        self.h_line.addLoyout(self.r_line)
        self.setLayout(self.h_line)

    def next_click(self):
        self.hide()
        self.fw = FinalWin()

    def connects(self):
        self.btn_next.clicked.connect(self.next_click)

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
