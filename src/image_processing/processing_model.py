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
        output = cv2.cvtColor(dataIn, cv2.COLOR_RGB2GRAY)
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


'''图像去噪功能'''


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


'''图像边缘检测功能'''


class ImageCanny(CtrlNode):
    nodeName = 'ImageCanny'
    uiTemplate = [
        ('minVal', 'spin', {'value': 100.0, 'step': 0.1, 'bounds': [0, None]}),
        ('maxVal', 'spin', {'value': 200.0, 'step': 0.1, 'bounds': [0, None]}),
        ('aperture_size', 'spin', {'value': 3, 'step': 2, 'bounds': [3, 7]}),
        ('L2gradient', 'check', {'value': False}),
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
            s = self.stateGroup.state()
            dataout = cv2.Canny(dataIn, minVal, maxVal, None, aperture_size, L2gradient=s['L2gradient'])
            return {'dataOut': dataout}


'''图像轮廓'''


class Imagerough(CtrlNode):
    nodeName = 'Imagerough'
    uiTemplate = [
        ('mode', 'combo', {'values': ['cv2.RETR_EXTERNAL', 'cv2.RETR_LIST', 'cv2.RETR_CCOMP',
         'cv2.RETR_TREE'], 'index': 3}),
        ('method', 'combo', {'values': ['cv2.CHAIN_APPROX_SIMPLE', 'cv2.CHAIN_APPROX_NONE'], 'index': 1}),
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
            datagray = cv2.cvtColor(dataIn, cv2.COLOR_BGR2GRAY)
            ret, thresh = cv2.threshold(datagray, 127, 255, 0)
            s = self.stateGroup.state()
            if s['mode'] == 'cv2.RETR_EXTERNAL':
                mode = 0
            elif s['mode'] == 'cv2.RETR_LIST':
                mode = 1
            elif s['mode'] == 'cv2.RETR_CCOMP':
                mode = 2
            else:
                mode = 3

            if s['method'] == 'cv2.CHAIN_APPROX_SIMPLE':
                method = 1
            else:
                method = 2
            contours, hierarchy = cv2.findContours(thresh, mode=mode, method=method)
            # contours, hierarchy = cv2.findContours(dataIn, 1, 2)

            #复制图像，用于绘制轮廓
            # draw_img=dataIn.copy()
            # 创建一个空白图像，与原图大小相同，用于绘制轮廓
            contour_img = np.zeros_like(dataIn)

            # 在空白图像上绘制轮廓，绘制所有轮廓，白色，线宽1
            res = cv2.drawContours(contour_img, contours, -1, (255, 255, 255), 1)
            # 在复制图像上绘制轮廓，绘制所有轮廓，红色，线宽1
            # res = cv2.drawContours(draw_img, contours, -1, (255, 0, 0), 1)
            return {'dataOut': res}



'''这里创建了两个自定义的方法'''
fclib.registerNodeType(ImageViewNode, [('Display',)])
fclib.registerNodeType(ImageGray, [('Process',)])
fclib.registerNodeType(ImageBinary, [('Process',)])
fclib.registerNodeType(ImageInputLocal, [('ProcessData',)])
fclib.registerNodeType(ImageOutput, [('ProcessData',)])
fclib.registerNodeType(ImageDenoising, [('ProcessData',)])
fclib.registerNodeType(ImageCanny, [('ProcessData',)])
fclib.registerNodeType(Imagerough, [('ProcessData',)])
