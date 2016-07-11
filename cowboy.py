# _*_ coding: utf-8 _*_

from PyQt4 import QtCore, QtGui
import sys

app = QtGui.Application(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("First program on PyQt")
window.resize(300,100)
label = QtGui.QLabel("<center>Hello World!!</center>")
btnQuit = QGui.PushButton("&Close Window")
vbox = QtGui.QVBoxLayout()
vbox.addWidget(label)
vbox.addWidget(btnQuite)
window.addLayout(vbox)
QtCore.QObject.connect(btnQuit,QtCore.SIGNAL("clicked()"), QtGui.qApp,QtCore.SLOT("quit()"))

window.show()
sys.exit(app.exec_())