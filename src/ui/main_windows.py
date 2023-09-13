"""
Author:Qychui
DATE:2023/9/12 14:44
File:main_windows.py
"""
import sys

from PyQt6 import QtWidgets

from tool_bar import ToolWindows

from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QFrame, QSplitter, QTextEdit


class MainWindows(ToolWindows, QWidget):

    # 初始显示文件
    def __init__(self):
        super().__init__()
        self.initUI()

    # 窗口初始化函数，可自行添加运行
    def initUI(self):
        super().initUI()




        self.statusbar = self.statusBar()
        self.statusbar.showMessage('程序初始化完成')

        self.menubar = self.menuBar()
        self.viewMenu = self.menubar.addMenu('文件')
        self.setMenu = self.menubar.addMenu('设置')
        self.aboutMenu = self.menubar.addMenu('关于')
        self.helpMenu = self.menubar.addMenu('帮助')

        self.viewStatAct = QAction('打开项目', self)
        self.viewStatAct.setStatusTip('选择文件打开')
        self.viewStatAct.setChecked(True)

        self.viewQuit = QAction('退出程序', self)
        self.viewQuit.setStatusTip('退出程序')

        self.viewImport = QAction('导入程序', self)

        self.viewSet = QAction('主题设置', self)
        self.viewSet.setStatusTip('打开设置窗口')

        self.viewHelp = QAction('获取帮助', self)
        self.viewAbout = QAction('关于洲洲', self)

        self.viewMenu.addAction(self.viewStatAct)
        self.viewMenu.addAction(self.viewImport)
        self.viewMenu.addAction(self.viewQuit)

        self.setMenu.addAction(self.viewSet)
        self.aboutMenu.addAction(self.viewAbout)
        self.helpMenu.addAction(self.viewHelp)

        self.statusBar()





        self.setWindowTitle('洲洲视觉')  # 窗口标题显示

        self.showMaximized()  # 打开时默认全屏显示
        self.show()


def main():
    app = QApplication(sys.argv)
    ex = MainWindows()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
