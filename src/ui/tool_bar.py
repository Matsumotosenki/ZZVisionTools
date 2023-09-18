"""
Author:Qychui
DATE:2023/9/13 14:26
File:tool_bar.py
"""
from PyQt6 import QtCore
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QAction, QIcon, QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import QMainWindow, QFrame, QSplitter, QGridLayout, QLabel, QPushButton, QListView, QVBoxLayout
from flow_chart import FlowChart


class ToolWindows(QMainWindow, FlowChart):

    def __init__(self):
        super().__init__()

    def initUI(self):
        # 最上方的菜单和最底下的状态栏显示
        self.MenuBar()
        # 工具栏
        self.ToolBar()
        # 流程图
        self.FlowChart()
        # 图像处理
        self.ImageProces()
        # 窗口布局层，放在最后
        self.LayoutWindows()

    '''窗口布局设定函数'''

    def LayoutWindows(self):
        self.topLeft = QFrame(self)
        self.topLeft.setFrameShape(QFrame.Shape.StyledPanel)
        self.topLeft.setMaximumWidth(160)
        self.topLeft.setMinimumWidth(70)
        # self.topLeft.setFixedWidth(150)
        self.topLeft.setLayout(self.img_process_layout)

        self.topMiddle = QFrame(self)
        self.topMiddle.setFrameShape(QFrame.Shape.StyledPanel)
        self.topMiddle.setBaseSize(400, 300)
        self.topMiddle.setMinimumWidth(300)
        self.topMiddle.setLayout(self.FlowChatlayout)

        self.topRight_t = QFrame(self)
        self.topRight_t.setFrameShape(QFrame.Shape.StyledPanel)
        self.topRight_t.setMinimumHeight(200)
        self.topRight_b = QFrame(self)
        self.topRight_b.setFrameShape(QFrame.Shape.StyledPanel)
        self.topRight_b.setMaximumHeight(300)
        self.topRight_b.setMinimumHeight(100)

        self.topRight_splitter = QSplitter(QtCore.Qt.Orientation.Vertical)
        self.topRight_splitter.addWidget(self.topRight_t)
        self.topRight_splitter.addWidget(self.topRight_b)
        self.topRight_splitter.setMinimumWidth(400)

        self.botSplitter = QFrame(self)
        self.botSplitter.setFrameShape(QFrame.Shape.StyledPanel)
        self.botSplitter.setBaseSize(600, 150)
        self.botSplitter.setMinimumHeight(50)

        self.topSplitter = QSplitter(self)

        # 向topSplitter中添加控件并设置大小
        self.topSplitter.addWidget(self.topLeft)
        self.topSplitter.addWidget(self.topMiddle)
        self.topSplitter.addWidget(self.topRight_splitter)
        self.topSplitter.setMinimumHeight(400)
        self.topSplitter.setFixedHeight(600)

        self.mainSplitter = QSplitter(self)
        # 实例化botSplitter并将初始方向设置为水平
        self.mainSplitter.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.mainSplitter.addWidget(self.topSplitter)
        self.mainSplitter.addWidget(self.botSplitter)

        self.setCentralWidget(self.mainSplitter)

    '''工具栏布局函数'''

    def ToolBar(self):
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

    '''菜单函数'''

    def MenuBar(self):
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

    def ImageProces(self):
        self.img_process_layout = QVBoxLayout(self)
        self.list_view = QListView(self)
        self.img_process_layout.addWidget(self.list_view)

        # 创建一个QStandardItemModel
        model = QStandardItemModel()

        process_name = ['灰度化', '二值化', '霍夫圆检测', '截取ROI区域']
        # 添加带有图标的项目
        for i in process_name:
            icon = QIcon('icon/Edit.png')
            pixmap = icon.pixmap(QSize(55, 55))
            item = QStandardItem(QIcon(pixmap), f'{i}')
            # item.setDragEnabled(True)  # 允许拖拽
            item.setSizeHint(QSize(50, 50))
            model.appendRow(item)

        # 将模型设置给QListView
        self.list_view.setModel(model)
        # self.list_view.setFixedWidth(150)
