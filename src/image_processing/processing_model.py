"""
Author:Qychui
DATE:2023/9/15 17:36
File:processing_model.py
"""
import cv2
import numpy as np
import pyqtgraph.flowchart.library as fclib
from pyqtgraph.flowchart.library.common import CtrlNode
from pyqtgraph.flowchart import Node


class ImageViewNode(Node):

    nodeName = 'ImageView'

    def __init__(self, name):
        self.view = None
        Node.__init__(self, name, terminals={'data': {'io': 'in'}})

    def setView(self, view):
        self.view = view

    def process(self, data, display=True):

        if display and self.view is not None:
            if data is None:
                self.view.setImage(np.zeros((1, 1)))
            else:
                self.view.setImage(data)


class ImageGray(CtrlNode):
    nodeName = 'ImageGray'
    uiTemplate = [
        ('启用灰度化', 'check', {'checked': True}),
    ]

    def __init__(self, name):
        # 定义输入输出终端
        terminals = {
            'dataIn': dict(io='in'),  # 图像的输入
            'dataOut': dict(io='out'),  # 定义输出
        }  # 可以自己定义加入多种输入输出节点信息和名称

        CtrlNode.__init__(self, name, terminals=terminals)

    '''这是程序的逻辑层'''

    def process(self, dataIn, display=True):
        output = cv2.cvtColor(dataIn, cv2.COLOR_GRAY2BGR)
        return {'dataOut': output}


class ImageBinary(CtrlNode):
    nodeName = 'ImageBinary'
    uiTemplate = [
        ('thresh', 'spin', {'value': 1.0, 'step': 1.0, 'bounds': [0.0, None]}),
        ('maxvalue', 'spin', {'value': 1.0, 'step': 0.5, 'bounds': [0.0, None]}),
    ]

    def __init__(self, name):
        terminals = {
            'dataIn': dict(io='in'),  # 图像的输入
            'dataOut': dict(io='out'),  # 定义输出
        }  # 可以自己定义加入多种输入输出节点信息和名称

        CtrlNode.__init__(self, name, terminals=terminals)

    def process(self, dataIn, display=True):
        thresh = self.ctrls['thresh'].value()
        max_value = self.ctrls['maxvalue'].value()
        ret, thresh1 = cv2.threshold(dataIn, thresh, max_value, cv2.THRESH_BINARY)
        return {'dataOut': thresh1}

'''图像输入功能'''
class ImageInputLocal(CtrlNode):
    nodeName = 'ImageInputLocal'
    uiTemplate = [
        ('选择路径未完成', 'spin', {'value': 1.0, 'step': 1.0, 'bounds': [0.0, None]}),
    ]

    def __init__(self, name):
        terminals = {
            'dataOut': dict(io='out'),
        }

        CtrlNode.__init__(self, name, terminals=terminals)

    def process(self, dataOut, display=True):
        pass

'''图像数据输出功能'''
class ImageOutput(CtrlNode):
    nodeName = 'ImageOutput'
    uiTemplate = [
        ('勾选路径和其他参数', 'spin', {'value': 1.0, 'step': 1.0, 'bounds': [0.0, None]}),
    ]

    def __init__(self, name):
        terminals = {
            'dataIn': dict(io='in'),
        }
        CtrlNode.__init__(self, name, terminals=terminals)

    def process(self, dataIn, display=True):
        return {'dataOut': dataIn}

'''这里创建了两个自定义的方法'''
fclib.registerNodeType(ImageViewNode, [('Display',)])
fclib.registerNodeType(ImageGray, [('Process',)])
fclib.registerNodeType(ImageBinary, [('Process',)])
fclib.registerNodeType(ImageInputLocal, [('ProcessData',)])
fclib.registerNodeType(ImageOutput, [('ProcessData',)])