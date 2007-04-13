#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import sys
import os

from PyQt4 import QtGui, QtCore

from Ui_mainwindow import Ui_MainWindow
import rst2rst,pprint,codecs
import docutils.core
import sourcecode
from pprint import pprint

def titleFromNode(node):
    title=''
    for n in node.children:
        if isinstance(n,docutils.nodes.title):
            title=rst2rst.gather_rst(n,0)
            node.children.remove(n)
            break
    return title

class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        # Set up the UI from designer
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
                
        QtCore.QObject.connect(self.ui.action_Open,
            QtCore.SIGNAL("triggered()"),
            self.openFile)

        QtCore.QObject.connect(self.ui.action_Save,
            QtCore.SIGNAL("triggered()"),
            self.saveFile)
        QtCore.QObject.connect(self.ui.slide_list,
            QtCore.SIGNAL("currentRowChanged(int)"),
            self.openSlide)
        
        self.data=None
        self.tree=None
        self.nodes={}
        self.slides=[]
        
    def saveFile(self):
    
        data=''
    
        t=[]
        tit=str(self.ui.pres_title.text())
        t.append('='*len(tit))
        t.append(tit)
        t.append('='*len(tit))
        t.append('')
        
        tit=str(self.ui.pres_subtitle.text())
        t.append('-'*len(tit))
        t.append(tit)
        t.append('-'*len(tit))
        t.append('')
        
        data=data+'\n'.join(t)
    
        for slide in self.slides:
            data=data+'\n'+self.slideToText(slide)
            
        codecs.open('salida','w','utf-8').write(data)
        
    def slideToText(self,slide):
        t=[]
        t.append(slide[0])
        t.append('-'*len(slide[0]))
        t.append('')
        t.append('')
        return '\n'.join(t)+slide[1]
        
        
    def openSlide(self,n):
        self.ui.slide_title.setText(self.slides[n][0])
        self.ui.slide_text.setText(self.slides[n][1])
        
    def processDocument(self):    
        for node in self.tree.children:
            if isinstance(node,docutils.nodes.title):
                # Presentation title
                self.nodes['pres_title']=node
                self.ui.pres_title.setText(rst2rst.gather_rst(node,0))
            elif isinstance(node,docutils.nodes.subtitle):
                # Presentation title
                self.nodes['pres_subtitle']=node
                self.ui.pres_subtitle.setText(rst2rst.gather_rst(node,0))
            elif isinstance(node,docutils.nodes.decoration):
                for subnode in node.children:
                    if isinstance(subnode,docutils.nodes.header):
                        self.nodes['header']=subnode
                        self.ui.pres_header.setPlainText(rst2rst.gather_rst(subnode,0))
                    elif isinstance(subnode,docutils.nodes.footer):
                        self.nodes['footer']=subnode
                        self.ui.pres_footer.setPlainText(rst2rst.gather_rst(subnode,0))
                    else:
                        print "1: Unknown node",pprint(subnode)
                        
            elif isinstance(node,docutils.nodes.section):
                self.slides.append([titleFromNode(node),rst2rst.gather_rst(node,0)])
            elif isinstance(node,docutils.nodes.docinfo):
                self.addDocInfo(node)
            else:
                print "2: Unknown node",pprint(node)
                print rst2rst.gather_rst(node,0)
            self.updateSlideList()

    def updateSlideList(self):
        self.ui.slide_list.clear()
        for slide in self.slides:
            self.ui.slide_list.addItem(slide[0])
            
            
    def addDocInfo(self,node):
        pass

    def openFile(self):
        fn=str(QtGui.QFileDialog.getOpenFileName (self))
        if not fn:
            return
        self.data=codecs.open(fn,"r","utf-8").read()
        self.tree=docutils.core.publish_doctree(self.data)
        
        self.processDocument()

def main():
    app=QtGui.QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
