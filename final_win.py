from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout
from instr import *
from PyQt5.QtCore import Qt


class FinalWin(QWidget):
    def __init__(self, res, age):
        super().__init__()
        self.res = res
        self.age = int(age)
        self.set_appear()
        self.initUI()
        self.heart()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.index_text = QLabel(index + str(self.res))
        self.res_txt = QLabel(result + self.heart())
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.index_text, alignment=Qt.AlignCenter)
        self.layout.addWidget(self.res_txt, alignment= Qt.AlignCenter)
        self.setLayout(self.layout)
    def heart(self):
        if self.age > 15:
            self.age = 15
        self.age = (self.age + 1) // 2 - 4
        a = self.res + 1.5*self.age
        if a > 21:
            return low
        elif a > 17:
            return notlow
        elif a>12:
            return average
        elif a>6.5:
            return high
        else:
            return highest