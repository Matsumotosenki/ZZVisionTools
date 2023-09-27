"""
Author:Qychui
DATE:2023/9/15 17:36
File:processing_model.py
"""
import cv2
import numpy as np
import pyqtgraph as pg
from pyqtgraph.flowchart.library.common import CtrlNode
from pyqtgraph.flowchart import Node


class ImageViewNode(Node):
    """Node that displays images data in an ImageView widget"""
    nodeName = 'ImageView'

    def __init__(self, name):
        self.view = None
        ## Initialize node with only a single input terminal
        Node.__init__(self, name, terminals={'data': {'io': 'in'}})

    def setView(self, view):  ## setView must be called by the program
        self.view = view

    def process(self, data, display=True):
        ## if process is called with display=False, then the flowchart is being operated
        ## in batch processing mode, so we should skip displaying to improve performance.

        if display and self.view is not None:
            ## the 'data' argument is the value given to the 'data' terminal
            if data is None:
                self.view.setImage(np.zeros((1, 1)))  # give a blank array to clear the view
            else:
                self.view.setImage(data)


class ImageGray(CtrlNode):
    nodeName = '图像灰度化'
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

        output = cv2.cvtColor(dataIn,cv2.COLOR_GRAY2BGR)
        return {'dataOut': output}

class ImageDenoising(CtrlNode):
    nodeName = 'ImageDenoising'
    uiTemplate = [
        ('h', 'spin', {'value': 10.0, 'step': 0.1, 'bounds': [0.1, 50]}),
        ('hForColorComponents', 'spin', {'value': 10.0, 'step': 0.1, 'bounds': [0.1, 50]}),
        ('templateWindowSize', 'spin', {'value': 7, 'step': 2, 'bounds': [1, None]}),
        ('searchWindowSize', 'spin', {'value': 21, 'step': 2, 'bounds': [1, None]}),
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
        dataout = cv2.fastNlMeansDenoisingColored(dataIn, None, float(self.ctrls['h'].value()),
                                                  float(self.ctrls['hForColorComponents'].value()),
                                                  int(self.ctrls['templateWindowSize'].value()),
                                                  int(self.ctrls['searchWindowSize'].value()))

        return {'dataOut': dataout}

class ImageCanny(CtrlNode):
    nodeName = 'ImageCanny'
    uiTemplate = [
        ('minVal', 'spin', {'value': 100.0, 'step': 0.1, 'bounds': [0, None]}),
        ('maxVal', 'spin', {'value': 200.0, 'step': 0.1, 'bounds': [0, None]}),
        ('aperture_size', 'spin', {'value': 3, 'step': 2, 'bounds': [3, 7]}),
        ('L2gradient', 'spin', {'value': 0, 'step': 1, 'bounds': [0, 1]}),
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
            minVal = float(self.ctrls['minVal'].value())
            maxVal = float(self.ctrls['maxVal'].value())
            aperture_size = int(self.ctrls['aperture_size'].value())
            L2gradient = bool(self.ctrls['L2gradient'].value())
            dataout = cv2.Canny(dataIn, minVal, maxVal, None, aperture_size, L2gradient)
            return {'dataOut': dataout}
