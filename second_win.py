from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QApplication, QHBoxLayout, QLineEdit
from instr import *
from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtGui import QFont
import time
from final_win import FinalWin
class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def set_appear(self):
        self.setWindowTitle('Тесты')
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.name_text = QLabel(txt_name)
        self.age_text = QLabel(txt_age)
        self.instr_text = QLabel(txt_instr)
        self.instr_text2 = QLabel(txt_instr2)
        self.instr_text3 = QLabel(txt_instr3)
        self.time_txt = QLabel('0:00:00')
        self.time_txt.setFont(QFont("Times", 36, QFont.Bold))

        self.txt_next = QPushButton(txt_next2)
        self.test1 = QPushButton(test1)
        self.test2 = QPushButton(test2)
        self.test3 = QPushButton(test3)

        self.name_line = QLineEdit('Ф.И.О')
        self.age_line = QLineEdit('0')
        self.test1_line = QLineEdit('0')
        self.test2_line = QLineEdit('0')
        self.test3_line = QLineEdit('0')
        
        self.h_line = QHBoxLayout()
        self.l_line = QVBoxLayout()
        self.r_line = QVBoxLayout()

        self.l_line.addWidget(self.name_text)
        self.l_line.addWidget(self.name_line)
        self.l_line.addWidget(self.age_text)
        self.l_line.addWidget(self.age_line)
        self.l_line.addWidget(self.instr_text)
        self.l_line.addWidget(self.test1)
        self.l_line.addWidget(self.test1_line)
        self.l_line.addWidget(self.instr_text2)
        self.l_line.addWidget(self.test2)
        self.l_line.addWidget(self.instr_text3)
        self.l_line.addWidget(self.test3)
        self.l_line.addWidget(self.test2_line)
        self.l_line.addWidget(self.test3_line)
        self.l_line.addWidget(self.txt_next, alignment=Qt.AlignCenter)

        self.r_line.addWidget(self.time_txt)

        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        
        self.setLayout(self.h_line)

    def connects(self):
        self.txt_next.clicked.connect(self.next_click)
        self.test1.clicked.connect(self.test1_timer)
        self.test2.clicked.connect(self.test2_timer)
        self.test3.clicked.connect(self.test3_timer)
    
    def test1_timer(self):
        global time
        time = QTime(0, 0, 15)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)
        
    def timer1Event(self):
        global time
        time = time.addSecs(-1)
        self.time_txt.setText(time.toString("hh:mm:ss"))
        if time.toString("hh:mm:ss")[6:8] == '00':
            self.timer.stop()
    
    def test2_timer(self):
        global time
        time = QTime(0, 0, 30)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer2Event)
        self.timer.start(1500)
        
    def timer2Event(self):
        global time
        time = time.addSecs(-1)
        self.time_txt.setText(time.toString("hh:mm:ss")[6:8])
        if time.toString("hh:mm:ss")[6:8] == '00':
            self.timer.stop()
    
    def test3_timer(self):
        global time
        time = QTime(0, 1, 0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer3Event)
        self.timer.start(1000)
        
    def timer3Event(self):
        global time
        time = time.addSecs(-1)
        self.time_txt.setText(time.toString("hh:mm:ss"))
        if int(time.toString("hh:mm:ss")[6:8]) in range(15, 45):
            self.time_txt.setStyleSheet("color:rgb(0,0,0)")
        else:
            self.time_txt.setStyleSheet("color:rgb(0,255,0)")

        if time.toString("hh:mm:ss")[6:8] == '00':
            self.timer.stop()

    def next_click(self):
        self.hide()
        self.res = (4*(int(self.test1_line.text())+int(self.test2_line.text())+int(self.test3_line.text()))-200)/10
        self.age = self.age_line.text()
        self.fw = FinalWin(self.res, self.age)

