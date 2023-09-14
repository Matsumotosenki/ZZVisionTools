"""
Author:Qychui
DATE:2023/9/14 17:29
File:flow_chart.py
"""
import sys

from PyQt6.QtWidgets import QWidget, QApplication, QGridLayout, QGroupBox
from pyqtgraph.flowchart import Flowchart


class FlowChart(QWidget):

    def __init__(self):
        super().__init__()

    def initUI(self):
        self.layout = QGridLayout(self)
        self.flowChartBox = QGroupBox(self)
        self.fc = Flowchart()
        self.flowChartWidget = self.fc.widget().chartWidget
        self.flowChartLayout = QGridLayout(self.flowChartBox)
        self.flowChartLayout.setContentsMargins(0, 0, 0, 0)
        self.flowChartLayout.addWidget(self.flowChartWidget)
        self.layout.addWidget(self.flowChartBox, 0, 0, 1, 1)

