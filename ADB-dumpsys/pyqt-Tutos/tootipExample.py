__author__ = 'barin.huseyin'

from PyQt4 import QtGui
import time
import sys
import os
from PyQt4.QtCore import *
from PyQt4.QtGui import *


class ExampleToolbar(QtGui.QMainWindow):
    def __init__(self):
        super(ExampleToolbar, self).__init__()

        self.initUI()


    def callFunctionDemo(self):
        print os.getcwd()

    def initUI(self):
        exitAction = QtGui.QAction(QtGui.QIcon('phone.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(self.callFunctionDemo)
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)
        self.resize(250, 150)
        self.center()
        self.setWindowTitle('Center')
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


    def closeEvent(self, event):

        reply = QtGui.QMessageBox.question(self, 'Message',
                                           "Are you sure to quit?", QtGui.QMessageBox.Yes |
                                           QtGui.QMessageBox.No, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


class ExampleStatusBar(QtGui.QMainWindow):
    def __init__(self):
        super(ExampleStatusBar, self).__init__()
        self.initUI()


    def initUI(self):
        self.statusBar().showMessage('Ready')

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Statusbar')
        self.show()


class ExampleCenter(QtGui.QWidget):
    def __init__(self):
        super(ExampleCenter, self).__init__()

        self.initUI()

    def initUI(self):
        self.resize(250, 150)
        self.center()

        self.setWindowTitle('Center')
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


class ExampleAlert(QtGui.QWidget):
    def __init__(self):
        super(ExampleAlert, self).__init__()

        self.initUI()


    def initUI(self):

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Message box')
        self.show()


    def closeEvent(self, event):

        reply = QtGui.QMessageBox.question(self, 'Message',
                                           "Are you sure to quit?", QtGui.QMessageBox.Yes |
                                           QtGui.QMessageBox.No, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):
        QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))

        self.setToolTip('This is a <b>QWidget</b> widget')

        btn = QtGui.QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.clicked.connect(QCoreApplication.instance().quit)
        btn.resize(btn.sizeHint())
        btn.move(50, 50)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Tooltips')
        self.show()


def main():
    app = QApplication(sys.argv)

    tooltip = ExampleToolbar()

    tooltip.show()

    app.exec_()


if __name__ == "__main__": main()