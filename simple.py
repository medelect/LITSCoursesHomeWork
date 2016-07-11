#!/home/axe/projects/homeWork/virtPyQt5/pyqt5/bin/python3
# -*- coding: utf-8 -*-

import sys
import math

#sys.path.append(r"/home/axe/projects/homeWork/virtPyQt5/pyqt5/lib/python3.5/site-packages/")

from PyQt5.QtWidgets import QApplication, QWidget
#from PyQt5.QtCore import *

#print(sys.path)
if __name__ == '__main__':

    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('Simple')
    w.show()

    sys.exit(app.exec_())

