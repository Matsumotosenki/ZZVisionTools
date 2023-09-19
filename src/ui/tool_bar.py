"""
Author:Qychui
DATE:2023/9/13 14:26
File:tool_bar.py
"""
import random

from PyQt6 import QtCore

from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from pyqtgraph.flowchart import Flowchart


class ToolWindows(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

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
        self.topMiddle.setLayout(self.flow_chart_layout)

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
        self.img_process_list = ZZListWidget()
        self.img_process_layout = QVBoxLayout(self)
        self.img_process_layout.addWidget(self.img_process_list)

    def FlowChart(self):
        self.flowChart = FlowChart()
        self.flow_chart_layout = QVBoxLayout(self)
        self.flow_chart_layout.addWidget(self.flowChart)


class ZZListWidget(QListWidget):
    def __init__(self):
        super().__init__()
        process_name = [
            {"name": "灰度化", "icon_path": "icon/Edit.png"},
            {"name": "二值化", "icon_path": "icon/Quit.png"},
            {"name": "霍夫圆检测", "icon_path": "icon/Quit.png"},
            {"name": "截取ROI区域", "icon_path": "icon/Quit.png"},
            {"name": "图像输入", "icon_path": "icon/Open.png"},
            {"name": "图像保存", "icon_path": "icon/Save.png"}
        ]

        for data in process_name:
            item = QListWidgetItem(data["name"])
            icon = QIcon(data["icon_path"])

            # 设置图标的显示大小
            pixmap = icon.pixmap(QSize(40, 40))
            item.setIcon(QIcon(pixmap))

            item.setSizeHint(QSize(60, 50))
            self.addItem(item)
            self.setDefaultDropAction(Qt.DropAction.CopyAction)  # 设置拖拽模式为复制
            self.setDragDropMode(QAbstractItemView.DragDropMode.InternalMove)  # 拖拽模式为内部拖放

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


# TODO(gongzi): 把FlowChart单独拎出一个类
class FlowChart(QTabWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        '''添加一个初始选项窗口'''
        self.new_tab = QWidget()
        self.insertTab(self.count(), self.new_tab, f'选项卡{self.count() + 1}')
        self.tab_UI()

        '''加号键的事件'''
        self.addTab(QWidget(), "+")
        self.tabBarClicked.connect(self.addTabAction)
        self.tabBarDoubleClicked.connect(self.closeTab)

        # 设置初始选项卡为活动状态
        self.setCurrentIndex(0)

    def addTabAction(self, index):
        # 当点击“+”按钮选项卡时
        if index == self.count() - 1:
            # 创建一个新选项卡
            # TODO():选项卡需要设置关闭按钮和双击自定义名称的功能
            self.new_tab = QWidget()

            #     self.insertTab(self.count() - 1, self.new_tab, "")  # 空标题
            #     self.setTabText(self.count() - 2, f'选项卡{self.count()}')
            #     close_button = QPushButton("X")
            #     close_button.clicked.connect(lambda _, i=self.count() - 1: self.closeTab(i))
            #     self.tab_UI()
            #     self.tabBar().setTabButton(self.count() - 2, QTabBar.ButtonPosition.RightSide, close_button)
            #     self.setCurrentIndex(self.count() - 2)
            # else:
            #     self.setCurrentIndex(index)

            self.insertTab(self.count() - 1, self.new_tab, f'选项卡{self.count()}')
            self.tab_UI()
            self.setCurrentIndex(self.count() - 2)  # 设置新选项卡为活动状态

    def closeTab(self, index):
        self.removeTab(index)

    def FlowChart(self):
        self.tab_UI()

    # def tabW1_UI(self):
    #     fLayout = QFormLayout()
    #     self.xm = QLineEdit()
    #     self.xb1 = QRadioButton('男')
    #     self.xb2 = QRadioButton('女')
    #     self.xb1.setChecked(True)
    #     self.csny = QLineEdit()
    #     btn = QPushButton("确定")
    #     # btn.clicked.connect(self.clickedFunc)
    #
    #     hLay = QHBoxLayout()
    #     hLay.addWidget(self.xb1)
    #     hLay.addWidget(self.xb2)
    #     fLayout.addRow('姓名: ', self.xm)
    #     fLayout.addRow('性别: ', hLay)
    #     fLayout.addRow('出生年月: ', self.csny)
    #     fLayout.addRow(' ', btn)
    #     self.setTabText(0, '基本信息')  # 修改第1个选项卡标题
    #     self.tabW1.setLayout(fLayout)
    #
    #     # 定义窗口对象tabW2界面控件
    #
    # def tabW2_UI(self):
    #     hLay = QHBoxLayout()
    #     self.cb1 = QCheckBox('C++')
    #     self.cb2 = QCheckBox('Java')
    #     self.cb3 = QCheckBox('C#')
    #     self.cb1.setChecked(True)
    #     hLay.addWidget(self.cb1)
    #     hLay.addWidget(self.cb2)
    #     hLay.addWidget(self.cb3)
    #     self.setTabText(1, '编程语言')  # 修改第2个选项卡标题
    #     self.tabW2.setLayout(hLay)

    def tab_UI(self, default_sel=0):
        """流程图设置"""
        # pg.setConfigOptions(background='w')
        # pg.setConfigOptions(crashWarning=True)
        # pg.setConfigOptions(exitCleanup=True)

        flowLayout = QHBoxLayout()

        self.FlowChatlayout = QGridLayout(self)
        self.flowChartBox = QGroupBox(self)

        self.fc = Flowchart()

        '''默认节点隐藏'''
        self.fc.inputNode.close()
        self.fc.outputNode.close()



        self.flowChartWidget = self.fc.widget().chartWidget
        self.flowChartLayout = QGridLayout(self.flowChartBox)
        self.flowChartLayout.setContentsMargins(0, 0, 0, 0)
        self.flowChartLayout.addWidget(self.flowChartWidget)

        random_val = random.randint(0,2)
        if random_val == 0:
            rand_node = self.fc.createNode('Max', pos=(0, 0))

            plot_node = self.fc.createNode('GaussianFilter', pos=(200, 0))

            # 将两个节点连接起来
            self.fc.connectTerminals(rand_node['Out'], plot_node['In'])
        elif random_val == 1:
            rand_node = self.fc.createNode('Min', pos=(0, 0))

            plot_node = self.fc.createNode('GaussianFilter', pos=(200, 0))

            # 将两个节点连接起来
            self.fc.connectTerminals(rand_node['Out'], plot_node['In'])
        elif random_val == 2:
            pass



        flowLayout.addWidget(self.flowChartBox, 0)
        if default_sel == 1:
            # self.new_tab.setLayout(flowLayout)
            print(1)
        else:
            self.new_tab.setLayout(flowLayout)
