"""
Author:Qychui
DATE:2023/9/23 10:28
File:pyqtDropAction.py
"""
import sys

from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon, QCursor
from PyQt6.QtWidgets import QListWidget, QListWidgetItem, QAbstractItemView, QMenu, QWidget, QVBoxLayout, QMainWindow, \
    QApplication, QSplitter


class ZZListWidget(QListWidget):
    def __init__(self):
        super().__init__()
        process_name = [
            {"name": "图像输入", "icon_path": "icon/Open.png"},
            {"name": "图像保存", "icon_path": "icon/Save.png"},
            {"name": "灰度化", "icon_path": "icon/Edit.png"},
            {"name": "二值化", "icon_path": "icon/Quit.png"},
            {"name": "霍夫圆检测", "icon_path": "icon/Quit.png"},
            {"name": "截取ROI区域", "icon_path": "icon/Quit.png"},
        ]

        for data in process_name:
            item = QListWidgetItem(data["name"])
            icon = QIcon(data["icon_path"])

            # 设置图标的显示大小
            pixmap = icon.pixmap(QSize(40, 40))
            item.setIcon(QIcon(pixmap))

            item.setSizeHint(QSize(60, 50))
            self.addItem(item)
            self.setDragDropMode(QAbstractItemView.DragDropMode.InternalMove)  # 拖拽模式为内部拖放

        # 右键菜单操作
        self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.customContextMenuRequested.connect(self.showContextMenu)

    def showContextMenu(self, pos):
        context_menu = QMenu(self)
        delete_action = context_menu.addAction("Delete Item")
        action = context_menu.exec_(self.mapToGlobal(pos))

        if action == delete_action:
            selected_item = self.currentItem()
            if selected_item:
                self.takeItem(self.row(selected_item))


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        central_widget = QWidget()
        layout = QVBoxLayout()

        self.list_widget = ZZListWidget()

        # Create a splitter to divide the space
        splitter = QSplitter(Qt.Orientation.Horizontal)
        splitter.addWidget(self.list_widget)

        # Add an empty widget (half of the window space)
        empty_widget = QWidget()
        splitter.addWidget(empty_widget)

        layout.addWidget(splitter)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Connect the custom function for handling drops
        empty_widget.setAcceptDrops(True)
        empty_widget.dragEnterEvent = self.dragEnterEvent
        empty_widget.dropEvent = self.dropEvent

    def dragEnterEvent(self, event):
        # This function handles the drag enter event
        event.accept()

    def dropEvent(self, event):
        # This function handles the drop event
        # You can perform any custom actions here
        selected_item = self.list_widget.currentItem()
        if selected_item:
            item_name = selected_item.text()
            print(f"Item dropped: {item_name}")
            cursor_pos = QCursor.pos()
            # 获取事件位置作为创建网格的标准
            print(f"鼠标当前位置：x={cursor_pos.x()}, y={cursor_pos.y()}")

if __name__ == "__main__":
    app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
