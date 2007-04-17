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
import rst2sl

transition_names=['from_bottom','from_left','from_right','from_top','fade_in','to_bottom','to_left','to_right','to_top','fade_out']
num_trans=len(transition_names)/2


def titleFromNode(node):
    title=''
    for n in node.children:
        if isinstance(n,docutils.nodes.title):
            title=rst2rst.gather_rst(n,0)
            node.children.remove(n)
            break
    return title

class MainWindow(QtGui.QMainWindow):
    def __init__(self,fname=None):
        QtGui.QMainWindow.__init__(self)

        # Set up the UI from designer
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
                
        QtCore.QObject.connect(self.ui.action_Open,
            QtCore.SIGNAL("triggered()"),
            self.openFile)

        QtCore.QObject.connect(self.ui.actionExport_HTML,
            QtCore.SIGNAL("triggered()"),
            self.exportHTML)

        QtCore.QObject.connect(self.ui.action_Save,
            QtCore.SIGNAL("triggered()"),
            self.saveFile)

        QtCore.QObject.connect(self.ui.slide_list,
            QtCore.SIGNAL("currentItemChanged ( QListWidgetItem *, QListWidgetItem *)"),
            self.switchSlide)
        
        self.data=None
        self.tree=None
        self.nodes={}
        self.slides=[]
        self.transitions=[]
        if fname:
            self.openFile(fname)
            
        
    def switchSlide(self,current,previous):
        pos_prev=self.ui.slide_list.row(previous)
        pos_cur=self.ui.slide_list.row(current)
        
        self.saveSlide(pos_prev)
        self.openSlide(pos_cur)
    
    def saveSlide(self,n):        
        self.slides[n][0]=unicode(self.ui.slide_title.text())
        self.slides[n][1]=unicode(self.ui.slide_text.toPlainText())
        self.transitions[2+n*2]=transition_names[self.ui.intrans.currentIndex()]
        self.transitions[3+n*2]=transition_names[self.ui.outtrans.currentIndex()+num_trans]
    
    def openSlide(self,n):
        self.ui.slide_title.setText(self.slides[n][0])
        self.ui.slide_text.setText(self.slides[n][1])
        
        self.ui.intrans.setCurrentIndex(transition_names.index(self.transitions[2+n*2]))
        self.ui.outtrans.setCurrentIndex(transition_names.index(self.transitions[3+n*2])-num_trans)
        
    def exportHTML(self):
        self.htmlfn='.'.join(self.fn.split('.')[:-1])+'.html'
        self.generateData()            
        html,code=rst2sl.rst2sl(self.data)
        codecs.open(self.htmlfn,'w','utf-8').write(html)
        
    def generateData(self):
        # FIXME these should actually be just modifications to the
        # docutils nodes and then a call to gen_rst but that's
        # for later ;-)
    
        self.data=''
    
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
        
        self.data=self.data+'\n'.join(t)

        #Docinfo
        self.data+='\n:transitions: '+','.join(self.transitions)+'\n'
        
    
        for slide in self.slides:
            self.data=self.data+'\n'+self.slideToText(slide)
            
        # FIXME handle header and footer
        
        
    def saveFile(self):
        self.generateData()            
        codecs.open(self.fn,'w','utf-8').write(self.data)
        
    def slideToText(self,slide):
        t=[]
        t.append(slide[0])
        t.append('-'*len(slide[0]))
        t.append('')
        t.append('')
        return '\n'.join(t)+slide[1]
        
        
    def processDocument(self):    
        self.nodes={}
        self.slides=[]
        self.transitions=[]

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
                        self.ui.header.setText(rst2rst.gather_rst(subnode,0))
                    elif isinstance(subnode,docutils.nodes.footer):
                        self.nodes['footer']=subnode
                        self.ui.footer.setText(rst2rst.gather_rst(subnode,0))
                    else:
                        print "1: Unknown node",pprint(subnode)
                        
            elif isinstance(node,docutils.nodes.section):
                self.slides.append([titleFromNode(node),rst2rst.gather_rst(node,0)])
            elif isinstance(node,docutils.nodes.docinfo):
                self.addDocInfo(node)
            else:
                print "2: Unknown node",pprint(node)
                print rst2rst.gather_rst(node,0)
            #self.matchTransitions()
            self.updateSlideList()

    def matchTransitions(self):
        print "t1: ",self.transitions
        while len(self.transitions) < 2+2*len(self.slides):
            self.transitions+=['from_bottom','to_bottom']
        self.transitions=self.transitions[:2+2*len(self.slides)]
        print "t2: ",self.transitions
            
    def updateSlideList(self):
        self.ui.slide_list.clear()
        for slide in self.slides:
            self.ui.slide_list.addItem(slide[0])
            
    def addDocInfo(self,node):
        for n in node.children:
            text=rst2rst.gen_rst(n,0)
            if text.startswith(':transitions:'):
                self.transitions=text[13:].strip().split(',')
                print "trans: ",self.transitions

    def openFile(self,fn=None):
        if not fn:
            fn=str(QtGui.QFileDialog.getOpenFileName (self))
        if not fn:
            return
        self.fn=fn
        self.data=codecs.open(fn,"r","utf-8").read()
        self.tree=docutils.core.publish_doctree(self.data)
        
        self.processDocument()

def main():
    app=QtGui.QApplication(sys.argv)
    window=MainWindow(sys.argv[1])
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
