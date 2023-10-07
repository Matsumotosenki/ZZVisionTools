"""
Author:Qychui
DATE:2023/9/14 17:09
File:pyqtflowchart.py
"""

import sys
import pyqtgraph as pg
from PyQt6.QtWidgets import QApplication, QGridLayout, QGroupBox, QWidget
from pyqtgraph.flowchart import Flowchart

pg.setConfigOptions(background='w')
pg.setConfigOptions(crashWarning=True)
pg.setConfigOptions(exitCleanup=True)


class DemoUI(QWidget):

    def __init__(self):
        super(DemoUI, self).__init__()
        self.setUI()
        self.show()

    def setUI(self):
        self.setWindowTitle("DemoUI")

        self.layout = QGridLayout(self)
        self.flowChartBox = QGroupBox(self)
        self.fc = Flowchart()
        self.flowChartWidget = self.fc.widget().chartWidget
        self.flowChartLayout = QGridLayout(self.flowChartBox)
        self.flowChartLayout.setContentsMargins(1, 2, 1, 5)
        self.flowChartLayout.addWidget(self.flowChartWidget)

        self.fc.inputNode.close()
        self.fc.outputNode.close()

        rand_node = self.fc.createNode('Max', pos=(0, 0))
        plot_node = self.fc.createNode('GaussianFilter', pos=(200, 0))
        self.fc.createNode('PlotCurve', pos=(400, 0))

        # 将两个节点连接起来
        self.fc.connectTerminals(rand_node['Out'], plot_node['In'])

        self.layout.addWidget(self.flowChartBox, 0, 0, 1, 1)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = DemoUI()
    app.exit(app.exec())
