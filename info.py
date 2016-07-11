#!/home/axe/projects/homeWork/virtPyQt5/pyqt5/bin/python3

from PyQt5.QtCore import QT_VERSION_STR
from PyQt5.Qt import PYQT_VERSION_STR
from PyQt5.QtWidgets import QWidget
from sip import SIP_VERSION_STR


print('Qt version: ',QT_VERSION_STR)
print('SIP version: ',SIP_VERSION_STR)
print('PyQt version: ',PYQT_VERSION_STR)
print(dir(QWidget))