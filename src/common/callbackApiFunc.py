#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : callbackApiFun.py
# @Author: yangshuai
# @Date  : 2021/11/13
# @Desc  :


from PyQt5.QtCore import  *

class callbackApiFunc(QObject):

    @pyqtSlot()
    def getTerminalInfo(self):
        self.test = '这是一个测试'
        return self.test

    @pyqtSlot()
    def getConfigVal(self):
        self.val = 'getConfigVal测试'
        return self.val;