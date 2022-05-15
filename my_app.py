from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QApplication
from instr import *
from PyQt5.QtCore import Qt
from second_win import TestWin
class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.hello_text = QLabel(txt_hello)
        self.instr_text = QLabel(txt_instruction)
        self.txt_next = QPushButton(txt_next)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.hello_text)
        self.layout.addWidget(self.instr_text)
        self.layout.addWidget(self.txt_next, alignment=Qt.AlignCenter)
        self.setLayout(self.layout)

    def connects(self):
        self.txt_next.clicked.connect(self.next_click)

    def next_click(self):
        self.hide()
        self.tw = TestWin()
app = QApplication([])
mainwin = MainWin()
app.exec_()    




