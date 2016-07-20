#!/home/axe/projects/homeWork/virtPyQt5/pyqt5/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout)
from PyQt5.QtCore import *


import sys
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("First Project on PyQT")
window.resize(300,200)
btn = QPushButton("Hi")
btn.resize(200,100)

vbox = QVBoxLayout() 
vbox.addWidget(btn)

window.setLayout(vbox)

#QtCore.connect(btn, SIGNAL("clicked()")), app, SLOT("quit()")



window.show()
sys.exit(app.exec_())