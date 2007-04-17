# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/mnt/centos/home/ralsina/Desktop/proyectos/tobogan/tobogan/mainwindow.ui'
#
# Created: Tue Apr 17 14:59:16 2007
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

        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")

        self.presentation = QtGui.QWidget()
        self.presentation.setObjectName("presentation")

        self.vboxlayout1 = QtGui.QVBoxLayout(self.presentation)
        self.vboxlayout1.setMargin(9)
        self.vboxlayout1.setSpacing(6)
        self.vboxlayout1.setObjectName("vboxlayout1")

        self.gridlayout = QtGui.QGridLayout()
        self.gridlayout.setMargin(0)
        self.gridlayout.setSpacing(6)
        self.gridlayout.setObjectName("gridlayout")

        self.pres_subtitle = QtGui.QLineEdit(self.presentation)
        self.pres_subtitle.setObjectName("pres_subtitle")
        self.gridlayout.addWidget(self.pres_subtitle,1,1,1,1)

        self.pres_title = QtGui.QLineEdit(self.presentation)
        self.pres_title.setObjectName("pres_title")
        self.gridlayout.addWidget(self.pres_title,0,1,1,1)

        self.header = QtGui.QLineEdit(self.presentation)
        self.header.setObjectName("header")
        self.gridlayout.addWidget(self.header,2,1,1,1)

        self.label_5 = QtGui.QLabel(self.presentation)
        self.label_5.setObjectName("label_5")
        self.gridlayout.addWidget(self.label_5,4,0,1,1)

        self.footer = QtGui.QLineEdit(self.presentation)
        self.footer.setObjectName("footer")
        self.gridlayout.addWidget(self.footer,3,1,2,1)

        self.label_4 = QtGui.QLabel(self.presentation)
        self.label_4.setObjectName("label_4")
        self.gridlayout.addWidget(self.label_4,2,0,2,1)

        self.label_2 = QtGui.QLabel(self.presentation)
        self.label_2.setObjectName("label_2")
        self.gridlayout.addWidget(self.label_2,0,0,1,1)

        self.label_3 = QtGui.QLabel(self.presentation)
        self.label_3.setObjectName("label_3")
        self.gridlayout.addWidget(self.label_3,1,0,1,1)
        self.vboxlayout1.addLayout(self.gridlayout)

        self.label_8 = QtGui.QLabel(self.presentation)
        self.label_8.setObjectName("label_8")
        self.vboxlayout1.addWidget(self.label_8)

        self.docinfo = QtGui.QTextEdit(self.presentation)
        self.docinfo.setObjectName("docinfo")
        self.vboxlayout1.addWidget(self.docinfo)
        self.tabWidget.addTab(self.presentation,"")

        self.slides = QtGui.QWidget()
        self.slides.setObjectName("slides")

        self.vboxlayout2 = QtGui.QVBoxLayout(self.slides)
        self.vboxlayout2.setMargin(9)
        self.vboxlayout2.setSpacing(6)
        self.vboxlayout2.setObjectName("vboxlayout2")

        self.splitter = QtGui.QSplitter(self.slides)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")

        self.slide_list = QtGui.QListWidget(self.splitter)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(1),QtGui.QSizePolicy.Policy(7))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.slide_list.sizePolicy().hasHeightForWidth())
        self.slide_list.setSizePolicy(sizePolicy)
        self.slide_list.setBaseSize(QtCore.QSize(150,0))
        self.slide_list.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.slide_list.setAutoFillBackground(False)
        self.slide_list.setUniformItemSizes(True)
        self.slide_list.setObjectName("slide_list")

        self.layoutWidget = QtGui.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")

        self.vboxlayout3 = QtGui.QVBoxLayout(self.layoutWidget)
        self.vboxlayout3.setMargin(0)
        self.vboxlayout3.setSpacing(6)
        self.vboxlayout3.setObjectName("vboxlayout3")

        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setMargin(0)
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setObjectName("hboxlayout")

        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.hboxlayout.addWidget(self.label)

        self.slide_title = QtGui.QLineEdit(self.layoutWidget)
        self.slide_title.setObjectName("slide_title")
        self.hboxlayout.addWidget(self.slide_title)
        self.vboxlayout3.addLayout(self.hboxlayout)

        self.hboxlayout1 = QtGui.QHBoxLayout()
        self.hboxlayout1.setMargin(0)
        self.hboxlayout1.setSpacing(6)
        self.hboxlayout1.setObjectName("hboxlayout1")

        self.label_6 = QtGui.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.hboxlayout1.addWidget(self.label_6)

        self.intrans = QtGui.QComboBox(self.layoutWidget)
        self.intrans.setObjectName("intrans")
        self.hboxlayout1.addWidget(self.intrans)

        self.label_7 = QtGui.QLabel(self.layoutWidget)
        self.label_7.setObjectName("label_7")
        self.hboxlayout1.addWidget(self.label_7)

        self.outtrans = QtGui.QComboBox(self.layoutWidget)
        self.outtrans.setObjectName("outtrans")
        self.hboxlayout1.addWidget(self.outtrans)
        self.vboxlayout3.addLayout(self.hboxlayout1)

        self.slide_text = QtGui.QTextEdit(self.layoutWidget)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(7),QtGui.QSizePolicy.Policy(7))
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.slide_text.sizePolicy().hasHeightForWidth())
        self.slide_text.setSizePolicy(sizePolicy)
        self.slide_text.setBaseSize(QtCore.QSize(450,0))

        font = QtGui.QFont(self.slide_text.font())
        font.setFamily("Bitstream Vera Sans Mono")
        self.slide_text.setFont(font)
        self.slide_text.setObjectName("slide_text")
        self.vboxlayout3.addWidget(self.slide_text)
        self.vboxlayout2.addWidget(self.splitter)
        self.tabWidget.addTab(self.slides,"")
        self.vboxlayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0,0,694,31))
        self.menubar.setObjectName("menubar")

        self.menuSlide = QtGui.QMenu(self.menubar)
        self.menuSlide.setObjectName("menuSlide")

        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")

        self.menu_Edit = QtGui.QMenu(self.menubar)
        self.menu_Edit.setObjectName("menu_Edit")

        self.menu_File = QtGui.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
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
        self.actionExport_HTML.setIcon(QtGui.QIcon(":/icons/icons/webexport.png"))
        self.actionExport_HTML.setObjectName("actionExport_HTML")

        self.actionNewSlide = QtGui.QAction(MainWindow)
        self.actionNewSlide.setIcon(QtGui.QIcon(":/icons/icons/newslide.png"))
        self.actionNewSlide.setObjectName("actionNewSlide")

        self.actionDelete_Slide = QtGui.QAction(MainWindow)
        self.actionDelete_Slide.setIcon(QtGui.QIcon(":/icons/icons/delslide.png"))
        self.actionDelete_Slide.setObjectName("actionDelete_Slide")

        self.actionMove_Up = QtGui.QAction(MainWindow)
        self.actionMove_Up.setEnabled(False)
        self.actionMove_Up.setIcon(QtGui.QIcon(":/icons/icons/1uparrow.png"))
        self.actionMove_Up.setObjectName("actionMove_Up")

        self.actionMove_Down = QtGui.QAction(MainWindow)
        self.actionMove_Down.setEnabled(False)
        self.actionMove_Down.setIcon(QtGui.QIcon(":/icons/icons/1downarrow.png"))
        self.actionMove_Down.setObjectName("actionMove_Down")
        self.menuSlide.addAction(self.actionNewSlide)
        self.menuSlide.addAction(self.actionDelete_Slide)
        self.menuSlide.addSeparator()
        self.menuSlide.addAction(self.actionMove_Up)
        self.menuSlide.addAction(self.actionMove_Down)
        self.menuHelp.addAction(self.action_Contents)
        self.menuHelp.addAction(self.actionAbout_Tobogan)
        self.menu_Edit.addAction(self.actionUndo)
        self.menu_Edit.addAction(self.actionRedo)
        self.menu_Edit.addSeparator()
        self.menu_Edit.addAction(self.actionCut)
        self.menu_Edit.addAction(self.actionCopy)
        self.menu_Edit.addAction(self.actionPaste)
        self.menu_Edit.addAction(self.actionDelete)
        self.menu_Edit.addAction(self.actionSelect_All)
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
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Edit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuSlide.menuAction())
        self.toolBar.addAction(self.action_Open)
        self.toolBar.addAction(self.action_Save)
        self.toolBar.addAction(self.actionExport_HTML)
        self.toolBar.addAction(self.actionPreview)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionUndo)
        self.toolBar.addAction(self.actionRedo)
        self.toolBar.addAction(self.actionCut)
        self.toolBar.addAction(self.actionCopy)
        self.toolBar.addAction(self.actionPaste)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionNewSlide)
        self.toolBar.addAction(self.actionDelete_Slide)
        self.toolBar.addAction(self.actionMove_Up)
        self.toolBar.addAction(self.actionMove_Down)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Footer:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Header:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Presentation Title:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Presentation Subtitle:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("MainWindow", "Extra Info:", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.presentation), QtGui.QApplication.translate("MainWindow", "Presentation", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Slide Title:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "In:", None, QtGui.QApplication.UnicodeUTF8))
        self.intrans.addItem(QtGui.QApplication.translate("MainWindow", "From Bottom", None, QtGui.QApplication.UnicodeUTF8))
        self.intrans.addItem(QtGui.QApplication.translate("MainWindow", "From Left", None, QtGui.QApplication.UnicodeUTF8))
        self.intrans.addItem(QtGui.QApplication.translate("MainWindow", "From Right", None, QtGui.QApplication.UnicodeUTF8))
        self.intrans.addItem(QtGui.QApplication.translate("MainWindow", "From Top", None, QtGui.QApplication.UnicodeUTF8))
        self.intrans.addItem(QtGui.QApplication.translate("MainWindow", "Fade In", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "Out:", None, QtGui.QApplication.UnicodeUTF8))
        self.outtrans.addItem(QtGui.QApplication.translate("MainWindow", "To Bottom", None, QtGui.QApplication.UnicodeUTF8))
        self.outtrans.addItem(QtGui.QApplication.translate("MainWindow", "To Left", None, QtGui.QApplication.UnicodeUTF8))
        self.outtrans.addItem(QtGui.QApplication.translate("MainWindow", "To Right", None, QtGui.QApplication.UnicodeUTF8))
        self.outtrans.addItem(QtGui.QApplication.translate("MainWindow", "To Top", None, QtGui.QApplication.UnicodeUTF8))
        self.outtrans.addItem(QtGui.QApplication.translate("MainWindow", "Fade out", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.slides), QtGui.QApplication.translate("MainWindow", "Slides", None, QtGui.QApplication.UnicodeUTF8))
        self.menuSlide.setTitle(QtGui.QApplication.translate("MainWindow", "Slide", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Edit.setTitle(QtGui.QApplication.translate("MainWindow", "&Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_File.setTitle(QtGui.QApplication.translate("MainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Open.setText(QtGui.QApplication.translate("MainWindow", "&Open", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Open.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Save.setText(QtGui.QApplication.translate("MainWindow", "&Save", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_as.setText(QtGui.QApplication.translate("MainWindow", "Save &as", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Quit.setText(QtGui.QApplication.translate("MainWindow", "&Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUndo.setText(QtGui.QApplication.translate("MainWindow", "Undo", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUndo.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Z", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRedo.setText(QtGui.QApplication.translate("MainWindow", "Redo", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRedo.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Shift+Z", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCut.setText(QtGui.QApplication.translate("MainWindow", "Cut", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCut.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+X", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCopy.setText(QtGui.QApplication.translate("MainWindow", "Copy", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCopy.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+C", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPaste.setText(QtGui.QApplication.translate("MainWindow", "Paste", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPaste.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+P", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDelete.setText(QtGui.QApplication.translate("MainWindow", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSelect_All.setText(QtGui.QApplication.translate("MainWindow", "Select All", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Contents.setText(QtGui.QApplication.translate("MainWindow", "&Contents", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Contents.setShortcut(QtGui.QApplication.translate("MainWindow", "F1", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout_Tobogan.setText(QtGui.QApplication.translate("MainWindow", "About Tobogan", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew.setText(QtGui.QApplication.translate("MainWindow", "New", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPreview.setText(QtGui.QApplication.translate("MainWindow", "Preview", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExport_HTML.setText(QtGui.QApplication.translate("MainWindow", "Export HTML", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNewSlide.setText(QtGui.QApplication.translate("MainWindow", "New Slide", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDelete_Slide.setText(QtGui.QApplication.translate("MainWindow", "Delete Slide", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMove_Up.setText(QtGui.QApplication.translate("MainWindow", "Move Up", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMove_Down.setText(QtGui.QApplication.translate("MainWindow", "Move Down", None, QtGui.QApplication.UnicodeUTF8))

import icons_rc


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
