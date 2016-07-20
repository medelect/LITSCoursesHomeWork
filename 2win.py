#!/home/axe/projects/homeWork/virtPyQt5/pyqt5/bin/python3

import sys
from PyQt5 import QtWidgets
from PyQt5 import QtCore

def window():
	app = QtWidgets.QApplication(sys.argv)
	w = QtWidgets.QWidget()
	w.resize(300,300)
	b= QtWidgets.QLabel(w)
	but=QtWidgets.QPushButton(w)
	but.setText("Hi")
	but.setGeometry(20,20,30,30) 
	b.setText("Hello World!")
	w.setGeometry(100,100,200,50)
	b.move(50,20)
	w.setWindowTitle("PyQt")

	QtCore.QObject.connect(but, QtCore.SIGNAL("clicked()")), QtWidgets.app, QtCore.SIGNAL("quit()")

	w.show()
	sys.exit(app.exec_())
if __name__ == '__main__':
 window()
