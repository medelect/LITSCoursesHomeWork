#!/home/axe/projects/homeWork/virtPyQt5/pyqt5/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider, QVBoxLayout, QApplication, QPushButton, QTextEdit)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()
        
    def initUI(self):

        lcd = QLCDNumber(self)
        sld = QSlider(Qt.Horizontal, self)
        btn = QPushButton("hi", self)
        txt = QTextEdit(self)

    #    print (dir(QSlider))

        txt.setText("aaa")
        

        btn.clicked.connect(self.moveObj)
        #btn.connect(self.btn, QtCore.SIGNAL("clicked()"), self.moveObj)

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)
        vbox.addWidget(btn)
        vbox.addWidget(txt)


        self.setLayout(vbox)
        sld.valueChanged.connect(lcd.display)
        #btn.clicked.connect(self.quit)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Signal & slot')
        self.show()

    def moveObj(self):
        txt.setText("bbb")

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())