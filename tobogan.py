#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import sys
import os
import tempfile

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

        QtCore.QObject.connect(self.ui.actionSave_as,
            QtCore.SIGNAL("triggered()"),
            self.saveFileAs)

        QtCore.QObject.connect(self.ui.actionPreview,
            QtCore.SIGNAL("triggered()"),
            self.preview)

        QtCore.QObject.connect(self.ui.actionMove_Up,
            QtCore.SIGNAL("triggered()"),
            self.moveSlideUp)

        QtCore.QObject.connect(self.ui.actionMove_Down,
            QtCore.SIGNAL("triggered()"),
            self.moveSlideDown)

        QtCore.QObject.connect(self.ui.actionNewSlide,
            QtCore.SIGNAL("triggered()"),
            self.newSlide)
            
        QtCore.QObject.connect(self.ui.actionDelete_Slide,
            QtCore.SIGNAL("triggered()"),
            self.delSlide)
        
        QtCore.QObject.connect(self.ui.slide_list,
            QtCore.SIGNAL("currentItemChanged ( QListWidgetItem *, QListWidgetItem *)"),
            self.switchSlide)
        
        self.data=None
        self.tree=None
        self.nodes={}
        self.slides=[]
        self.transitions=[]
        self.fn='untitled.rst'
        self.setTitle()
        if fname:
            self.openFile(fname)
        else:
            self.data='''\
==========
Title Here
==========

Subtitle Here
=============

:Author: Unknown
:transitions: from_bottom,to_bottom,from_bottom,to_bottom


Slide 1
-------

* Text of the slide

        '''
            self.tree=docutils.core.publish_doctree(self.data)
            self.processDocument()


    def newSlide(self):
        self.slides.append(['Slide %d'%(len(self.slides)),'Text of the slide'])
        self.transitions.append('from_bottom')
        self.transitions.append('to_bottom')
        self.updateSlideList()

    def delSlide(self):
        c=self.ui.slide_list.currentRow()
        if c>0:
            del self.slides[c]
            del self.transitions[c*2:c*2+1]
        self.updateSlideList()
        self.openSlide(c-1)
            
    def setTitle(self):
        self.setWindowTitle('Tobogan - %s'%self.fn)
        
    def preview(self):
        # Create a temporary folder
        dn=tempfile.mkdtemp()
        fn=os.path.join(dn,self.fn+'.html')
        self.exportAllFiles(dn)
        QtGui.QDesktopServices.openUrl(QtCore.QUrl(fn))

    def exportAllFiles(self,dname):
        fn=os.path.join(dname,self.fn+'.html')
        self.exportHTML(fn)
        for f in ['mootools.js','code.css','murphy.css','slides.css']:
            fn1=os.path.join('resources',f)
            fn2=os.path.join(dname,f)
            open(fn2,'w').write(open(fn1,'r').read())
        
    def moveSlideUp(self):
        r=self.ui.slide_list.currentRow()
        if r<2:
            return
        QtCore.QObject.disconnect(self.ui.slide_list,
            QtCore.SIGNAL("currentItemChanged ( QListWidgetItem *, QListWidgetItem *)"),
            self.switchSlide)
        r2=r-1
        t=self.slides[r2]        
        self.slides[r2]=self.slides[r]
        self.slides[r]=t
        self.updateSlideList()
        QtCore.QObject.connect(self.ui.slide_list,
            QtCore.SIGNAL("currentItemChanged ( QListWidgetItem *, QListWidgetItem *)"),
            self.switchSlide)
        self.ui.slide_list.setCurrentRow(r2)

    def moveSlideDown(self):
        r=self.ui.slide_list.currentRow()
        if r<1 or r>=len(self.slides)-1:
            return
        QtCore.QObject.disconnect(self.ui.slide_list,
            QtCore.SIGNAL("currentItemChanged ( QListWidgetItem *, QListWidgetItem *)"),
            self.switchSlide)
        r2=r+1
        t=self.slides[r2]        
        self.slides[r2]=self.slides[r]
        self.slides[r]=t
        self.updateSlideList()
        QtCore.QObject.connect(self.ui.slide_list,
            QtCore.SIGNAL("currentItemChanged ( QListWidgetItem *, QListWidgetItem *)"),
            self.switchSlide)
        self.ui.slide_list.setCurrentRow(r2)

        
    def switchSlide(self,current,previous):
            
        pos_prev=self.ui.slide_list.row(previous)
        pos_cur=self.ui.slide_list.row(current)

        self.ui.actionMove_Up.setEnabled(True)
        self.ui.actionMove_Down.setEnabled(True)
        print pos_cur,len(self.slides)
        if pos_cur in [-1,0,1]:
            self.ui.actionMove_Up.setEnabled(False)
        if pos_cur in [-1,0,len(self.slides)-1]:
            self.ui.actionMove_Down.setEnabled(False)
        
        
        self.saveSlide(pos_prev)
        self.openSlide(pos_cur)
    
    def saveSlide(self,n):    
        if n==-1 or n>len(self.slides)-1:
            return
        self.slides[n][0]=unicode(self.ui.slide_title.text())
        self.slides[n][1]=unicode(self.ui.slide_text.toPlainText())
        self.transitions[n*2]=transition_names[self.ui.intrans.currentIndex()]
        self.transitions[1+n*2]=transition_names[self.ui.outtrans.currentIndex()+num_trans]
    
    def openSlide(self,n):
        if n==-1:
            return
        self.ui.slide_title.setText(self.slides[n][0])
        self.ui.slide_text.setText(self.slides[n][1])
        
        self.ui.intrans.setCurrentIndex(transition_names.index(self.transitions[n*2]))
        self.ui.outtrans.setCurrentIndex(transition_names.index(self.transitions[1+n*2])-num_trans)
        
    def exportHTML(self,fname=None):
        if not fname:
            fname='.'.join(self.fn.split('.')[:-1])+'.html'
            
        self.generateData()            
        html,code=rst2sl.rst2sl(self.data)
        codecs.open(fname,'w','utf-8').write(html)
        
    def generateData(self):

        # Maybe the user modified current slide and never did anything
        # else so it didn't get saved
        self.saveSlide(self.ui.slide_list.currentRow())

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
        self.data+=unicode(self.ui.docinfo.toPlainText())
        
        for slide in self.slides[1:]:
            self.data=self.data+'\n'+self.slideToText(slide)+'\n'
            
        htext=unicode(self.ui.header.text())
        ftext=unicode(self.ui.footer.text())
        
        if htext:
            self.data+='\n\n.. header:: %s\n'%htext
        if ftext:
            self.data+='\n\n.. footer:: %s\n'%ftext
        
    def saveFileAs(self):
        fn=str(QtGui.QFileDialog.getSaveFileName (self))
        if fn:
            self.fn=fn
            self.setTitle()
            self.saveFile()
        
    def saveFile(self,fname=None):
        self.generateData()     
        if not fname:
            fname=self.fn
        codecs.open(fname,'w','utf-8').write(self.data)
        
    def slideToText(self,slide):
        t=[]
        t.append(slide[0])
        t.append('-'*len(slide[0]))
        t.append('')
        t.append('')
        return '\n'.join(t)+slide[1]
                
    def processDocument(self):    
        self.nodes={}
        self.slides=[['Cover Slide','You can\'t edit this in this version']]
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
        while len(self.transitions) < 2*len(self.slides):
            self.transitions+=['from_bottom','to_bottom']
        self.transitions=self.transitions[:2*len(self.slides)]
        print "t2: ",self.transitions
            
    def updateSlideList(self):
        self.ui.slide_list.clear()
        for slide in self.slides:
            self.ui.slide_list.addItem(slide[0])
            
    def addDocInfo(self,node):
        t=''
        for n in node.children:
            text=rst2rst.gen_rst(n,0)
            if text.startswith(':transitions:'):
                self.transitions=text[13:].strip().split(',')
            else:
                t+=text
        self.ui.docinfo.setText(t)
            

    def openFile(self,fn=None):
        if not fn:
            fn=str(QtGui.QFileDialog.getOpenFileName (self))
        if not fn:
            return
        self.fn=fn
        self.setTitle()
        self.data=codecs.open(fn,"r","utf-8").read()
        self.tree=docutils.core.publish_doctree(self.data)
        
        self.processDocument()
        
def main():
    app=QtGui.QApplication(sys.argv)
    if len(sys.argv)>1:
        window=MainWindow(sys.argv[1])
    else:
        window=MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
