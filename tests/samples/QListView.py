"""
Author:Qychui
DATE:2023/9/15 10:14
File:QListView.py
"""
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import QMainWindow, QWidget, QListView, QVBoxLayout, QApplication
from PyQt6.QtGui import QStandardItemModel, QStandardItem, QIcon
import sys


class ToolWindows(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QListView Example')
        self.setGeometry(100, 100, 400, 300)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        list_view = QListView(self)
        layout.addWidget(list_view)

        list_view.setFixedWidth(128)

        # 创建一个QStandardItemModel
        model = QStandardItemModel()

        # 添加6个可点击、可拖拽并带有图标的项目W
        for i in range(6):
            item = QStandardItem(QIcon('../../src/ui/icon/Edit.png'), f'Item {i + 1}')
            item.setDragEnabled(True)  # 允许拖拽
            # item.setSizeHint(QSize(50, 50))
            model.appendRow(item)

        # 将模型设置给QListView
        list_view.setModel(model)


def main():
    app = QApplication(sys.argv)
    ex = ToolWindows()
    ex.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
