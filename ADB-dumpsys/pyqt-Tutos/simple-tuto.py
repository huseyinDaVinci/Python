__author__ = 'barin.huseyin'
import time
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *


def main():
    # sys.argv we are getting the input from the command line.
    app = QApplication(
        sys.argv)  # every PyQt gui application must have QApplication object. this to be used access global like information such as the application directory.
    # QApplication  also provides the event loop.


    print dir(QApplication)
    try:
        due = QTime.currentTime()
        message = "Wake up body"
        if len(sys.argv) < 2:
            raise ValueError
        hours, mins = sys.argv[1].split(":")
        due = QTime(int(hours), int(mins))
        if not due.isValid():
            raise ValueError
        if len(sys.argv) > 2:
            message = " ".join(sys.argv[2:])

        label = QLabel("<font color=red size=72><b>" + message + "</b></font>")
        label.setWindowFlags(Qt.SplashScreen)

        label.show()
        QTimer.singleShot(60000, app.quit) # 1 minute
        app.exec_()

        while QTime.currentTime() < due:
            time.sleep(20)  # 20 seconds


    except ValueError:
        message = "Usage: alert.pyw HH:MM [optional message]"  # 24hr clock


if __name__ == "__main__": main();