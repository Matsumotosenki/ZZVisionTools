import sys

from PyQt6 import QtCore
from PyQt6.QtGui import QIcon, QAction
from PyQt6.QtWidgets import QApplication, QWidget, QSplitter, QTextEdit, QVBoxLayout, QFrame, QMainWindow


class SplitterExample(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 实例化两个QFrame控件
        topLeft = QFrame(self)
        topLeft.setFrameShape(QFrame.Shape.StyledPanel)
        topMiddle = QFrame(self)
        topMiddle.setFrameShape(QFrame.Shape.StyledPanel)
        topRight = QFrame(self)
        topRight.setFrameShape(QFrame.Shape.StyledPanel)
        topRight.setMinimumSize(300, 200)


        # 实例化QSplitter并将初始方向设置为水平
        topSplitter = QSplitter(self)
        topSplitter.setOrientation(QtCore.Qt.Orientation.Vertical)

        # 向splitter1中添加控件并设置它们的初始大小
        topSplitter.addWidget(topLeft)
        topSplitter.addWidget(topMiddle)
        topSplitter.addWidget(topRight)
        topSplitter.setStretchFactor(0,1)
        topSplitter.setStretchFactor(1,1)
        topSplitter.setStretchFactor(2,1)

        # 实例化另一个QSplitter并设置其方向为垂直
        botSplitter = QSplitter(self)
        botSplitter.addWidget(topSplitter)


        self.setCentralWidget(botSplitter)

        exitAct = QAction(QIcon('../Icon/RandomUser.ico'), 'Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(self.close)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAct)

        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exitAct)

        self.setWindowTitle("QSplitter示例")
        self.showMaximized()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = SplitterExample()
    demo.show()
    sys.exit(app.exec())
