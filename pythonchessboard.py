# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 17:53:45 2022

@author: valentine
"""
# chessboard
import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout
from PyQt5.QtGui import QColor, QPalette
from PyQt5.QtCore import QCoreApplication

class Color(QWidget):
    def __init__(self, color):
        super().__init__()
        self.setAutoFillBackground(True)
        self.myPalette = self.palette()
        self.myPalette.setColor(QPalette.Window, QColor(color))
        self.setPalette(self.myPalette)

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Grid Layouts")
        self.layout = QGridLayout()
        for i in range(4):
            if i%2 ==0:
                for k in range(4):
                    if k%2 == 0:
                         self.layout.addWidget(Color('black'),i,k)
                    else:
                        self.layout.addWidget(Color('white'),i,k)
            else:
                for k in range(4):
                    if k%2 == 0:
                         self.layout.addWidget(Color('white'),i,k)
                    else:
                        self.layout.addWidget(Color('black'),i,k)
                    
        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)

app = QCoreApplication.instance()
if app is None:
    app = QApplication(sys.argv)
window = Window()
window.show()
app.exec_()