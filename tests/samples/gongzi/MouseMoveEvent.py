"""
Author:Qychui
DATE:2023/9/20 16:20
File:MouseMoveEvent.py
"""
import sys
from PyQt5.QtWidgets import QPushButton, QWidget, QApplication
from PyQt5.QtCore import Qt, QMimeData, QPoint
from PyQt5.QtGui import QDrag
import time


class DraggableButton(QPushButton):
    def __init__(self, title, parent):
        super().__init__(title, parent)
        self.iniDragCor = [0, 0]

    def mousePressEvent(self, e):
        print("ppp", e.pos())
        self.iniDragCor[0] = e.x()
        self.iniDragCor[1] = e.y()

    def mouseMoveEvent(self, e):
        x = e.x() - self.iniDragCor[0]
        y = e.y() - self.iniDragCor[1]

        cor = QPoint(x, y)
        self.move(self.mapToParent(cor))  # 需要maptoparent一下才可以的,否则只是相对位置。

        print('drag button event,', time.time(), e.pos(), e.x(), e.y())


class DragWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.button1 = DraggableButton("mybutton", self)
        self.button1.move(50, 20)

        self.setWindowTitle("Click or Move")
        self.setGeometry(300, 300, 280, 150)

    def mouseMoveEvent(self, e):
        print('main', e.x(), e.y())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = DragWidget()
    ex.show()
    app.exec_()

