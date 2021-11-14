
import sys
from PyQt5.QtWidgets import QDesktopWidget


# class formStyleClass():
#     def __init__(self):
#         super(formStyleClass,self).__init__()

#窗体居中显示
def formCenter(self):
        #获取屏幕坐标系
        screen = QDesktopWidget().screenGeometry()
        #获取窗口坐标系
        size = self.geometry()
        newLeft = (screen.width() - size.width()) / 2
        newTop = (screen.height() - size.heigh()) / 2
        self.move(newLeft,newTop)

