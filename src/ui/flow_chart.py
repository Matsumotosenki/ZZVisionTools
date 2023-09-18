"""
Author:Qychui
DATE:2023/9/14 17:29
File:flow_chart.py
"""
import sys

from PyQt6.QtWidgets import QWidget, QApplication, QGridLayout, QGroupBox, QTabWidget, QFormLayout, QRadioButton, \
    QLineEdit, QHBoxLayout, QPushButton, QCheckBox
from pyqtgraph.flowchart import Flowchart


class FlowChart(QTabWidget):

    def __init__(self):
        super().__init__()

    def initUI(self):
        print('111')
        # 设置选项卡的位置、大小、标题和标签位置（上： North）
        self.setTabPosition(QTabWidget.TabPosition.North)
        # 创建用于显示控件的2个QWidget窗口对象tabW1、tabW2
        self.tabW1 = QWidget()
        self.tabW2 = QWidget()
        # tabW1、tabW2窗口分别加入选项卡1和选项卡2
        self.addTab(self.tabW1, '选项卡1')
        self.addTab(self.tabW2, '选项卡2')
        self.tabW1_UI()
        self.tabW2_UI()

        # 定义窗口对象tabW1界面控件

    def tabW1_UI(self):
        fLayout = QFormLayout()
        self.xm = QLineEdit()
        self.xb1 = QRadioButton('男')
        self.xb2 = QRadioButton('女')
        self.xb1.setChecked(True)
        self.csny = QLineEdit()
        btn = QPushButton("确定")
        # btn.clicked.connect(self.clickedFunc)

        hLay = QHBoxLayout()
        hLay.addWidget(self.xb1)
        hLay.addWidget(self.xb2)
        fLayout.addRow('姓名: ', self.xm)
        fLayout.addRow('性别: ', hLay)
        fLayout.addRow('出生年月: ', self.csny)
        fLayout.addRow(' ', btn)
        self.setTabText(0, '基本信息')  # 修改第1个选项卡标题
        self.tabW1.setLayout(fLayout)

        # 定义窗口对象tabW2界面控件

    def tabW2_UI(self):
        hLay = QHBoxLayout()
        self.cb1 = QCheckBox('C++')
        self.cb2 = QCheckBox('Java')
        self.cb3 = QCheckBox('C#')
        self.cb1.setChecked(True)
        hLay.addWidget(self.cb1)
        hLay.addWidget(self.cb2)
        hLay.addWidget(self.cb3)
        self.setTabText(1, '编程语言')  # 修改第2个选项卡标题
        self.tabW2.setLayout(hLay)

    def FlowChart(self):
        pass
        """流程图设置"""
        # pg.setConfigOptions(background='w')
        # pg.setConfigOptions(crashWarning=True)
        # pg.setConfigOptions(exitCleanup=True)

        # self.FlowChatlayout = QGridLayout(self)
        # self.flowChartBox = QGroupBox(self)
        # self.fc = Flowchart(
        #     terminals={
        #         'InputTerminal': {'io': 'in'},
        #         'OutputTerminal': {'io': 'out'},
        #         'Terminal': {'io': 'in'},
        #         'OutTerminal': {'io': ''}
        #     }
        # )
        # self.fc.inputNode.close()
        # self.fc.outputNode.close()
        #
        # self.flowChartWidget = self.fc.widget().chartWidget
        # self.flowChartLayout = QGridLayout(self.flowChartBox)
        # self.flowChartLayout.setContentsMargins(0, 0, 0, 0)
        # self.flowChartLayout.addWidget(self.flowChartWidget)
        # self.FlowChatlayout.addWidget(self.flowChartBox, 0, 0, 1, 1)

# class FlowTabWidget(QTabWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()