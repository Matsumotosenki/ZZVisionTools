"""
Author:Qychui
DATE:2023/9/13 14:26
File:tool_bar.py
"""
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtWidgets import QMainWindow


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
        self.toolbar.addActions((self.save_act, self.open_act,self.edit_act,self.quit_act))
