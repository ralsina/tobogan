# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/mnt/centos/home/ralsina/Desktop/proyectos/tobogan/tobogan/mainwindow.ui'
#
# Created: Fri Apr 13 11:08:49 2007
#      by: PyQt4 UI code generator 4.1.1
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(QtCore.QSize(QtCore.QRect(0,0,694,507).size()).expandedTo(MainWindow.minimumSizeHint()))

        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.vboxlayout = QtGui.QVBoxLayout(self.centralwidget)
        self.vboxlayout.setMargin(9)
        self.vboxlayout.setSpacing(6)
        self.vboxlayout.setObjectName("vboxlayout")

        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")

        self.slides = QtGui.QListWidget(self.splitter)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(1),QtGui.QSizePolicy.Policy(7))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.slides.sizePolicy().hasHeightForWidth())
        self.slides.setSizePolicy(sizePolicy)
        self.slides.setObjectName("slides")

        self.widget = QtGui.QWidget(self.splitter)
        self.widget.setObjectName("widget")

        self.vboxlayout1 = QtGui.QVBoxLayout(self.widget)
        self.vboxlayout1.setMargin(0)
        self.vboxlayout1.setSpacing(6)
        self.vboxlayout1.setObjectName("vboxlayout1")

        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setMargin(0)
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setObjectName("hboxlayout")

        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName("label")
        self.hboxlayout.addWidget(self.label)

        self.title = QtGui.QLineEdit(self.widget)
        self.title.setObjectName("title")
        self.hboxlayout.addWidget(self.title)
        self.vboxlayout1.addLayout(self.hboxlayout)

        self.text = QtGui.QTextEdit(self.widget)
        self.text.setObjectName("text")
        self.vboxlayout1.addWidget(self.text)
        self.vboxlayout.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0,0,694,31))
        self.menubar.setObjectName("menubar")

        self.menu_File = QtGui.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")

        self.menu_Edit = QtGui.QMenu(self.menubar)
        self.menu_Edit.setObjectName("menu_Edit")

        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setOrientation(QtCore.Qt.Horizontal)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(self.toolBar)

        self.action_Open = QtGui.QAction(MainWindow)
        self.action_Open.setIcon(QtGui.QIcon(":/icons/icons/fileopen.png"))
        self.action_Open.setObjectName("action_Open")

        self.action_Save = QtGui.QAction(MainWindow)
        self.action_Save.setIcon(QtGui.QIcon(":/icons/icons/filesave.png"))
        self.action_Save.setObjectName("action_Save")

        self.actionSave_as = QtGui.QAction(MainWindow)
        self.actionSave_as.setIcon(QtGui.QIcon(":/icons/icons/filesaveas.png"))
        self.actionSave_as.setObjectName("actionSave_as")

        self.action_Quit = QtGui.QAction(MainWindow)
        self.action_Quit.setIcon(QtGui.QIcon(":/icons/icons/fileclose.png"))
        self.action_Quit.setObjectName("action_Quit")

        self.actionUndo = QtGui.QAction(MainWindow)
        self.actionUndo.setIcon(QtGui.QIcon(":/icons/icons/undo.png"))
        self.actionUndo.setObjectName("actionUndo")

        self.actionRedo = QtGui.QAction(MainWindow)
        self.actionRedo.setIcon(QtGui.QIcon(":/icons/icons/redo.png"))
        self.actionRedo.setObjectName("actionRedo")

        self.actionCut = QtGui.QAction(MainWindow)
        self.actionCut.setIcon(QtGui.QIcon(":/icons/icons/editcut.png"))
        self.actionCut.setObjectName("actionCut")

        self.actionCopy = QtGui.QAction(MainWindow)
        self.actionCopy.setIcon(QtGui.QIcon(":/icons/icons/editcopy.png"))
        self.actionCopy.setObjectName("actionCopy")

        self.actionPaste = QtGui.QAction(MainWindow)
        self.actionPaste.setIcon(QtGui.QIcon(":/icons/icons/editpaste.png"))
        self.actionPaste.setObjectName("actionPaste")

        self.actionDelete = QtGui.QAction(MainWindow)
        self.actionDelete.setObjectName("actionDelete")

        self.actionSelect_All = QtGui.QAction(MainWindow)
        self.actionSelect_All.setObjectName("actionSelect_All")

        self.action_Contents = QtGui.QAction(MainWindow)
        self.action_Contents.setObjectName("action_Contents")

        self.actionAbout_Tobogan = QtGui.QAction(MainWindow)
        self.actionAbout_Tobogan.setObjectName("actionAbout_Tobogan")

        self.actionNew = QtGui.QAction(MainWindow)
        self.actionNew.setIcon(QtGui.QIcon(":/icons/icons/filenew.png"))
        self.actionNew.setObjectName("actionNew")

        self.actionPreview = QtGui.QAction(MainWindow)
        self.actionPreview.setIcon(QtGui.QIcon(":/icons/icons/xeyes.png"))
        self.actionPreview.setObjectName("actionPreview")

        self.actionExport_HTML = QtGui.QAction(MainWindow)
        self.actionExport_HTML.setObjectName("actionExport_HTML")
        self.menu_File.addAction(self.actionNew)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Open)
        self.menu_File.addAction(self.action_Save)
        self.menu_File.addAction(self.actionSave_as)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.actionExport_HTML)
        self.menu_File.addAction(self.actionPreview)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Quit)
        self.menu_Edit.addAction(self.actionUndo)
        self.menu_Edit.addAction(self.actionRedo)
        self.menu_Edit.addSeparator()
        self.menu_Edit.addAction(self.actionCut)
        self.menu_Edit.addAction(self.actionCopy)
        self.menu_Edit.addAction(self.actionPaste)
        self.menu_Edit.addAction(self.actionDelete)
        self.menu_Edit.addAction(self.actionSelect_All)
        self.menuHelp.addAction(self.action_Contents)
        self.menuHelp.addAction(self.actionAbout_Tobogan)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Edit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.actionNew)
        self.toolBar.addAction(self.action_Save)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionUndo)
        self.toolBar.addAction(self.actionRedo)
        self.toolBar.addAction(self.actionCut)
        self.toolBar.addAction(self.actionCopy)
        self.toolBar.addAction(self.actionPaste)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionPreview)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Slide Title:", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_File.setTitle(QtGui.QApplication.translate("MainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Edit.setTitle(QtGui.QApplication.translate("MainWindow", "&Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Open.setText(QtGui.QApplication.translate("MainWindow", "&Open", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Save.setText(QtGui.QApplication.translate("MainWindow", "&Save", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_as.setText(QtGui.QApplication.translate("MainWindow", "Save &as", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Quit.setText(QtGui.QApplication.translate("MainWindow", "&Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUndo.setText(QtGui.QApplication.translate("MainWindow", "Undo", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRedo.setText(QtGui.QApplication.translate("MainWindow", "Redo", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCut.setText(QtGui.QApplication.translate("MainWindow", "Cut", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCopy.setText(QtGui.QApplication.translate("MainWindow", "Copy", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPaste.setText(QtGui.QApplication.translate("MainWindow", "Paste", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDelete.setText(QtGui.QApplication.translate("MainWindow", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSelect_All.setText(QtGui.QApplication.translate("MainWindow", "Select All", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Contents.setText(QtGui.QApplication.translate("MainWindow", "&Contents", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Contents.setShortcut(QtGui.QApplication.translate("MainWindow", "F1", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout_Tobogan.setText(QtGui.QApplication.translate("MainWindow", "About Tobogan", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew.setText(QtGui.QApplication.translate("MainWindow", "New", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPreview.setText(QtGui.QApplication.translate("MainWindow", "Preview", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExport_HTML.setText(QtGui.QApplication.translate("MainWindow", "Export HTML", None, QtGui.QApplication.UnicodeUTF8))

import icons_rc


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
