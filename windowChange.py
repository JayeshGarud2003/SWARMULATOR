#file2
from PyQt5 import QtCore, QtWidgets
from nextWindow import NextPage
from SwarmUiTest import Dashboard
from compare import MyApp
# from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import * 
from fileMain import PageWindow
# from PyQt5.uic import loadUi
import pandas as pd
from PyQt5.QtCore import QSize, Qt, pyqtSlot, pyqtSignal
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QTableWidget, QTableWidgetItem,
                             QFileDialog, QVBoxLayout, QWidget, QDialog, QLabel, QLineEdit, QComboBox, QCheckBox, QHBoxLayout)

class Project(QtWidgets.QMainWindow):
    def __init__(self):
        super(Project,self).__init__()


        self.stacked_widget = QtWidgets.QStackedWidget()
        self.setCentralWidget(self.stacked_widget)


        self.pages = {}

        self.register_page(Dashboard(),"Dashboard")
        self.register_page(NextPage(),"next")
        self.register_page(MyApp(),"myapp")
        self.goto('Dashboard')

    def register_page(self,page,name):
        self.pages[name]  = page
        self.stacked_widget.addWidget(page)


        if isinstance(page,PageWindow):
            page.gotoSignal.connect(self.goto)
    


    @QtCore.pyqtSlot(str)
    def goto(self,name):
         if name in self.pages:
             self.stacked_widget.setCurrentWidget(self.pages[name])



if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    project = Project()
    project.show()
    sys.exit(app.exec_( ))