#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : webEnginesControl.py
# @Author: Feng
# @Date  : 2021/11/13
# @Desc  :


from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
import sys


channel = QWebChannel()
class WebEngineView(QMainWindow):

    def __init__(self):
        super(WebEngineView, self).__init__()
        self.setWindowTitle("政务终端")
        self.setGeometry(5,30,1355,730)
        self.browser = QWebEngineView()
        self.browser.load(QUrl('https://720yun.com/t/49vktq27srl?scene_id=74265864'))
        self.setCentralWidget(self.browser)
        channel.registerObject("VUE_BOUND")
if __name__ =='__main__':
    app = QApplication(sys.argv)
    win = WebEngineView()
    win.show()
    sys.exit(app.exec_())