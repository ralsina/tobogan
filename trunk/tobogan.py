#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import sys
import os

from PyQt4 import QtGui, QtCore

from Ui_mainwindow import Ui_MainWindow

class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        # Set up the UI from designer
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

def main():
    app=QtGui.QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
