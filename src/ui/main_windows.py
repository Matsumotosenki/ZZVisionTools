"""
Author:Qychui
DATE:2023/9/12 14:44
File:main_windows.py
"""
import sys


from tool_bar import ToolWindows
from ui_event import UIEvent
from PyQt6.QtWidgets import QApplication, QWidget


class MainWindows(ToolWindows, QWidget):

    # 初始显示文件
    def __init__(self):
        super().__init__()
        # self.initUI()

    # 窗口初始化函数，可自行添加运行
    def initUI(self):
        super().initUI()

        self.setWindowTitle('洲洲视觉')  # 窗口标题显示
        self.showMaximized()  # 打开时默认全屏显示
        self.show()


def main():
    app = QApplication(sys.argv)
    ex = MainWindows()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
