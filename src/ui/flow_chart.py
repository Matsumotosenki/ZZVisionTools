"""
Author:Qychui
DATE:2023/9/14 17:29
File:flow_chart.py
"""
import sys
import random
from PyQt6.QtWidgets import QTabWidget, QWidget, QHBoxLayout, QGridLayout, QGroupBox
from pyqtgraph.flowchart import Flowchart

'''
这段代码用于实现访问image_processing中的类方法
有一些编译器由于规则配置的问题可能会报错，但是并不影响正常运行
'''
sys.path.append('..')
from image_processing import *


class FlowChartView(QTabWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        '''添加一个初始选项窗口'''
        self.new_tab = QWidget()
        self.insertTab(self.count(), self.new_tab, f'选项卡{self.count() + 1}')
        self.tab_UI(default_sel=1)

        '''加号键的事件'''
        self.addTab(QWidget(), '+')
        self.tabBarClicked.connect(self.addTabAction)
        self.tabBarDoubleClicked.connect(self.closeTab)

        # 设置初始选项卡为活动状态
        self.setCurrentIndex(0)


    def addTabAction(self, index):
        # 当点击“+”按钮选项卡时
        if index == self.count() - 1:
            # 创建新的选项卡
            # TODO():选项卡需要设置关闭按钮和双击自定义名称的功能
            self.new_tab = QWidget()

            #     用于实现添加关闭按钮的功能
            #     self.insertTab(self.count() - 1, self.new_tab, '')  # 空标题
            #     self.setTabText(self.count() - 2, f'选项卡{self.count()}')
            #     close_button = QPushButton('X')
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

    def tab_UI(self, default_sel=0):
        '''流程图设置'''
        # pg.setConfigOptions(background='w')
        # pg.setConfigOptions(crashWarning=True)
        # pg.setConfigOptions(exitCleanup=True)

        flowLayout = QHBoxLayout()

        # self.FlowChatlayout = QGridLayout(self)
        self.flowChartBox = QGroupBox(self)
        self.fc = Flowchart(
            terminals={
                'dataIn': {'io': 'in'},
                'dataOut': {'io': 'out'}
            }
        )

        '''默认节点隐藏'''
        # self.fc.inputNode.close()
        self.fc.outputNode.close()

        self.flowChartWidget = self.fc.widget().chartWidget
        self.flowChartLayout = QGridLayout(self.flowChartBox)
        self.flowChartLayout.setContentsMargins(0, 0, 0, 0)
        self.flowChartLayout.addWidget(self.flowChartWidget)

        random_val = random.randint(0, 2)

        ''' 默认第一创建的窗口执行下列第三个分支'''
        # TODO():后期要改回来
        if default_sel == 1:
            random_val = 2

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

            output = cv2.imread('../../tests/images/R-C.jpg')
            self.fc.setInput(dataIn=output)

            self.img_view = self.fc.createNode('ImageView', pos=(300, 0))

            # self.fc.connectTerminals(self.fc['dataIn'], self.img_view['data'])

        flowLayout.addWidget(self.flowChartBox, 0)
        if default_sel == 1:
            print('创建了第一个窗口栏')
            self.new_tab.setLayout(flowLayout)
        else:
            print('new tab created')
            self.new_tab.setLayout(flowLayout)
