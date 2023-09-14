"""
Author:Qychui
DATE:2023/9/13 14:26
File:tool_bar.py
"""
from PyQt6 import QtCore
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtWidgets import QMainWindow, QFrame, QSplitter


class ToolWindows(QMainWindow):

    def __init__(self):
        super().__init__()

    def initUI(self):


        # 自定义添加状态栏
        self.save_act = QAction(QIcon('icon/Save.png'), 'Save', self)
        self.save_act.setStatusTip('保存程序')

        self.open_act = QAction(QIcon('icon/Open.png'), 'Open', self)
        self.open_act.setStatusTip('打开程序')

        self.edit_act = QAction(QIcon('icon/Edit.png'), 'Edit', self)
        self.edit_act.setStatusTip('编辑程序')

        self.quit_act = QAction(QIcon('icon/Quit.png'), 'Quit', self)
        # 设置快捷键
        self.quit_act.setShortcut('Ctrl+Shift+Q')
        self.quit_act.setStatusTip('退出程序')
        self.quit_act.triggered.connect(self.close)

        self.toolbar = self.addToolBar('工具栏')

        # 每次写完后需要往toolbar中添加实例
        self.toolbar.addActions((self.save_act, self.open_act, self.edit_act, self.quit_act))

        self.topLeft = QFrame(self)
        self.topLeft.setFrameShape(QFrame.Shape.StyledPanel)
        self.topLeft.setBaseSize(200, 300)
        self.topLeft.setMinimumWidth(50)

        self.topMiddle = QFrame(self)
        self.topMiddle.setFrameShape(QFrame.Shape.StyledPanel)
        self.topMiddle.setBaseSize(600, 300)
        self.topMiddle.setMinimumWidth(300)

        self.topRight = QFrame(self)
        self.topRight.setFrameShape(QFrame.Shape.StyledPanel)
        self.topRight.setBaseSize(600, 300)
        self.topRight.setMinimumWidth(300)

        self.botRight = QFrame(self)
        self.botRight.setFrameShape(QFrame.Shape.StyledPanel)
        self.botRight.setBaseSize(600, 150)
        self.botRight.setMinimumHeight(50)

        # 实例化QSplitter并将初始方向设置为水平
        self.topSplitter = QSplitter(self)

        # 向topSplitter中添加控件并设置大小
        self.topSplitter.addWidget(self.topLeft)
        self.topSplitter.addWidget(self.topMiddle)
        self.topSplitter.addWidget(self.topRight)
        self.topSplitter.setMinimumHeight(400)
        self.topSplitter.setFixedHeight(600)

        self.botSplitter = QSplitter(self)
        self.botSplitter.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.botSplitter.addWidget(self.topSplitter)
        self.botSplitter.addWidget(self.botRight)

        self.setCentralWidget(self.botSplitter)
