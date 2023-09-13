import sys

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
        topLeft.setBaseSize(400, 400)
        topLeft2 = QFrame(self)
        topLeft2.setFrameShape(QFrame.Shape.StyledPanel)
        topLeft2.setBaseSize(400, 400)
        bottom = QFrame(self)
        bottom.setFrameShape(QFrame.Shape.StyledPanel)
        bottom.setMinimumSize(300, 200)
        bottom.setBaseSize(400, 400)

        # 实例化QSplitter并将初始方向设置为水平
        splitter1 = QSplitter(self)

        # 向splitter1中添加控件并设置它们的初始大小
        splitter1.addWidget(topLeft)
        splitter1.addWidget(topLeft2)
        splitter1.addWidget(bottom)
        splitter1.setSizes([50, 100])

        # 实例化另一个QSplitter并设置其方向为垂直
        splitter2 = QSplitter(self)
        splitter2.addWidget(splitter1)
        # splitter2.addWidget(bottom)

        self.setCentralWidget(splitter2)

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
