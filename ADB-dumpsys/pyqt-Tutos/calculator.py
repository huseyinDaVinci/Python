from PyQt4 import QtGui
import time
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()


    def initUI(self):

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QtGui.QIcon('C:\\Users\\barin.huseyin\\Pictures\\phone1.png'))

        self.show()

class Form(QDialog):
    def __init__(self, parent=None):

        super(Form, self).__init__(parent)
        self.browser = QTextBrowser()
        self.lineedit = QLineEdit("Type an expression and press Enter")
        self.lineedit.selectAll()
        layout = QVBoxLayout()
        layout.addWidget(self.browser)
        layout.addWidget(self.lineedit)
        self.setLayout(layout)
        self.lineedit.setFocus()

       #self.connect(self.lineedit, SIGNAL("returnPressed()"),self.updateUi)
        self.setWindowTitle("Calculate")


def main():

    app = QtGui.QApplication(sys.argv)
    main_window =Form()
    main_window.show()
    sys.exit(app.exec_())


def test():
    app = QtGui.QApplication(sys.argv)

    w = QtGui.QWidget()
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('Simple')
    w.show()

    sys.exit(app.exec_())
if __name__ == "__main__": main();


