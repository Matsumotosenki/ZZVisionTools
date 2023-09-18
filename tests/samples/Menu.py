"""
Author:Qychui
DATE:2023/9/15 17:16
File:Menu.py
"""
import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QApplication, QListWidget, QMenu, QMainWindow, QVBoxLayout, QWidget

class MyListWidget(QListWidget):
    def __init__(self):
        super().__init__()

        # 创建一些初始项目
        self.addItem("Item 1")
        self.addItem("Item 2")
        self.addItem("Item 3")

        # 右键菜单操作
        self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.customContextMenuRequested.connect(self.showContextMenu)

    def showContextMenu(self, pos):
        menu = QMenu(self)
        delete_action = QAction("删除", self)
        delete_action.triggered.connect(self.deleteSelectedItem)
        menu.addAction(delete_action)
        menu.exec(self.mapToGlobal(pos))

    def deleteSelectedItem(self):
        selected_item = self.currentItem()
        if selected_item:
            row = self.row(selected_item)
            self.takeItem(row)

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)
        self.list_widget = MyListWidget()
        layout.addWidget(self.list_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec())
