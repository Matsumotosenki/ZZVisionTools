'''
Author:Qychui
DATE:2023/9/13 14:26
File:tool_bar.py
'''
import pyqtgraph
from PyQt6 import QtCore
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from flow_chart import FlowChartView


class ToolWindows(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 最上方的菜单和最底下的状态栏显示
        self.MenuBar()
        # 最上边工具栏
        self.ToolBar()
        # 中心流程图
        self.FlowChart()
        # TODO():右上角属性栏需要重写一个点击实时同步
        # 右上角属性栏
        self.FlowChartValue()
        # 右下角图像预览
        self.ImagePreviewLayout()
        # 左边图像处理
        self.ImageProces()
        # 窗口布局层，放在最后
        self.LayoutWindows()

    '''窗口布局设定函数'''

    def LayoutWindows(self):
        '''视图层说明'''

        '''左侧工具栏窗口设置'''
        self.topLeft = QFrame(self)
        self.topLeft.setFrameShape(QFrame.Shape.StyledPanel)
        self.topLeft.setMaximumWidth(160)
        self.topLeft.setMinimumWidth(70)
        # self.topLeft.setFixedWidth(150)
        self.topLeft.setLayout(self.img_process_layout)

        '''中间的流程图窗口设置'''
        self.topMiddle = QFrame(self)
        self.topMiddle.setFrameShape(QFrame.Shape.StyledPanel)
        self.topMiddle.setBaseSize(400, 300)
        self.topMiddle.setMinimumWidth(300)
        self.topMiddle.setLayout(self.flow_chart_layout)

        # 实现窗口拖拽功能
        self.topMiddle.setAcceptDrops(True)
        self.topMiddle.dragEnterEvent = self.dragEnterEvent
        self.topMiddle.dropEvent = self.dropEvent

        '''右上角属性窗口'''
        self.topRight_t = QFrame(self)
        self.topRight_t.setFrameShape(QFrame.Shape.StyledPanel)
        self.topRight_t.setMinimumHeight(200)
        self.topRight_t.setLayout(self.flow_chart_value)

        '''右下角图像查看窗口'''
        self.topRight_b = QFrame(self)
        self.topRight_b.setFrameShape(QFrame.Shape.StyledPanel)
        self.topRight_b.setLayout(self.image_layout_view)
        self.topRight_b.setMaximumHeight(300)
        self.topRight_b.setMinimumHeight(100)

        '''右边上下窗口整合到topRight_splitter中'''
        self.topRight_splitter = QSplitter(QtCore.Qt.Orientation.Vertical)
        self.topRight_splitter.addWidget(self.topRight_t)
        self.topRight_splitter.addWidget(self.topRight_b)
        self.topRight_splitter.setMinimumWidth(400)

        '''底部窗口：显示控制台指令和参数等等'''
        # self.botSplitter = QFrame(self)
        # self.botSplitter.setFrameShape(QFrame.Shape.StyledPanel)
        # self.botSplitter.setBaseSize(600, 150)
        # self.botSplitter.setMinimumHeight(50)

        self.topSplitter = QSplitter(self)

        # 向topSplitter中添加控件并设置大小
        self.topSplitter.addWidget(self.topLeft)
        self.topSplitter.addWidget(self.topMiddle)
        self.topSplitter.addWidget(self.topRight_splitter)
        self.topSplitter.setMinimumHeight(400)
        self.topSplitter.setFixedHeight(600)

        # self.mainSplitter = QSplitter(self)
        # # 实例化botSplitter并将初始方向设置为水平
        # self.mainSplitter.setOrientation(QtCore.Qt.Orientation.Vertical)
        # self.mainSplitter.addWidget(self.topSplitter)

        '''底部添加窗口'''
        # self.mainSplitter.addWidget(self.botSplitter)

        self.setCentralWidget(self.topSplitter)

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

    '''流程图实例化窗口'''

    def FlowChart(self):
        self.flowChart = FlowChartView()
        self.flow_chart_layout = QVBoxLayout(self)
        self.flow_chart_layout.addWidget(self.flowChart)

    def dragEnterEvent(self, event):
        event.accept()

    '''当释放工具栏中的工具时触发此函数'''

    def dropEvent(self, event):
        # TODO():要加一个判断，判断当前窗口是否为流程图窗口，若是则在当前流程图窗口创建一个新的流程模块(也可以在之前限制模块允许拖拽的范围和窗口)
        selected_item = self.img_process_list.currentItem()
        current_tab = self.flowChart.currentIndex()
        if selected_item:
            item_name = selected_item.text()
            print(f'物体被拖拽: {item_name}')
            cursor_cos = self.flowChart.fc.viewBox.viewPos()
            # cursor_m_pos = self.flowChart.fc.viewBox.mouseDragEvent(event)
            print(cursor_cos)
            # print(cursor_m_pos)
            print(f'当前坐标为{cursor_cos.x()},{cursor_cos.y()}')
            cursor_pos = QCursor.pos()
            # 获取事件位置作为创建网格的标准
            print(f'鼠标当前位置：x={cursor_pos.x()}, y={cursor_pos.y()}')
            print(f'当前选项卡的index为:{current_tab}')
            self.flowChart.fc.createNode('ImageGray',
                                         pos=(cursor_cos.x() + cursor_pos.x(), cursor_cos.y() + cursor_pos.y()))
            self.flowChart.flowChartWidget.nodeMenuTriggered()

    def nodeAction(self, action):
        if action.pos is not None:
            pos = action.pos
        else:
            pos = self.menuPos

    '''创建右上角流程图的值显示窗口'''

    def FlowChartValue(self):
        self.flow_chart_value = QVBoxLayout(self)
        self.flow_chart_value.addWidget(self.flowChart.fc.widget())

    '''创建右下角图像预览窗口'''

    def ImagePreviewLayout(self):
        self.image_layout_view = QVBoxLayout(self)
        self.imagePreview = pyqtgraph.ImageView()
        self.image_layout_view.addWidget(self.imagePreview)

        # TODO():函数访问不到图像、图像初始显示不出来（需要重新连接才能显示），记得修bug
        self.flowChart.img_view.setView(self.imagePreview)


'''该类型用于生成左侧工具栏里的工具'''


class ZZListWidget(QListWidget):
    def __init__(self):
        super().__init__()
        process_name = [
            {'name': '图像输入', 'icon_path': 'icon/Open.png'},
            {'name': '图像保存', 'icon_path': 'icon/Save.png'},
            {'name': '灰度化', 'icon_path': 'icon/Edit.png'},
            {'name': '二值化', 'icon_path': 'icon/Quit.png'},
            {'name': '霍夫圆检测', 'icon_path': 'icon/Quit.png'},
            {'name': '截取ROI区域', 'icon_path': 'icon/Quit.png'},
        ]

        for data in process_name:
            item = QListWidgetItem(data['name'])
            icon = QIcon(data['icon_path'])

            # 设置图标的显示大小
            pixmap = icon.pixmap(QSize(40, 40))
            item.setIcon(QIcon(pixmap))

            item.setSizeHint(QSize(60, 50))
            self.addItem(item)
            # self.setDefaultDropAction(Qt.DropAction.CopyAction)  # 设置拖拽模式为复制
            self.setDragDropMode(QAbstractItemView.DragDropMode.InternalMove)  # 拖拽模式为内部拖放

        # 右键菜单操作
        self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.customContextMenuRequested.connect(self.showContextMenu)

    def showContextMenu(self, pos):
        menu = QMenu(self)
        delete_action = QAction('删除', self)
        delete_action.triggered.connect(self.deleteSelectedItem)
        menu.addAction(delete_action)
        menu.exec(self.mapToGlobal(pos))

    def deleteSelectedItem(self):
        selected_item = self.currentItem()
        if selected_item:
            row = self.row(selected_item)
            self.takeItem(row)
