"""
Author:Qychui
DATE:2023/9/20 11:20
File:CustomNode2.py
"""
import cv2
from PIL import Image
import numpy as np
import os
import pyqtgraph as pg
import pyqtgraph.flowchart.library as fclib
from pyqtgraph.flowchart import Flowchart, Node
from pyqtgraph.flowchart.library.common import CtrlNode
from pyqtgraph.Qt import QtWidgets
from matplotlib import pyplot as plt

app = pg.mkQApp("Flowchart Custom Node Example")
print('123')
## Create main window with a grid layout inside
win = QtWidgets.QMainWindow()
win.setWindowTitle('pyqtgraph example: FlowchartCustomNode')
cw = QtWidgets.QWidget()
win.setCentralWidget(cw)
layout = QtWidgets.QGridLayout()
cw.setLayout(layout)

## Create an empty flowchart with a single input and output
fc = Flowchart(terminals={
    'dataIn': {'io': 'in'},
    'dataOut': {'io': 'out'}
})
w = fc.widget()

layout.addWidget(fc.widget(), 0, 0, 2, 1)

## Create two ImageView widgets to display the raw and processed data with contrast
## and color control.
v1 = pg.ImageView()
layout.addWidget(v1, 0, 1)

win.show()
win.showMaximized()  # 打开时默认全屏显示

## generate random input data
data = np.random.normal(size=(100, 100))
data = 25 * pg.gaussianFilter(data, (5, 5))
data += np.random.normal(size=(100, 100))
data[40:60, 40:60] += 15.0
data[30:50, 30:50] += 15.0
# data += np.sin(np.linspace(0, 100, 1000))
# data = metaarray.MetaArray(data, info=[{'name': 'Time', 'values': np.linspace(0, 1.0, len(data))}, {}])

output = cv2.imread('../images/OIP-C.jpg')
# default_out = cv2.cvtColor(output,cv2.COLOR_RGB2GRAY)

## Set the raw data as the input value to the flowchart
fc.setInput(dataIn=output)
fc.outputNode.close()


## At this point, we need some custom Node classes since those provided in the library
## are not sufficient. Each node will define a set of input/output terminals, a
## processing function, and optionally a control widget (to be displayed in the
## flowchart control panel)

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


## We will define an unsharp masking filter node as a subclass of CtrlNode.
## CtrlNode is just a convenience class that automatically creates its
## control widget based on a simple data structure.

# 反锐化掩模
class UnsharpMaskNode(CtrlNode):
    """Return the input data passed through an unsharp mask."""
    nodeName = "UnsharpMask"
    uiTemplate = [
        ('sigma', 'spin', {'value': 1.0, 'step': 1.0, 'bounds': [0.0, None]}),
        ('strength', 'spin', {'value': 1.0, 'dec': True, 'step': 0.5, 'minStep': 0.01, 'bounds': [0.0, None]}),
        ('main', 'spin', {'value': 1.0, 'step': 2.0, 'bounds': [0.0, None]}),
    ]

    def __init__(self, name):
        ## Define the input / output terminals available on this node
        terminals = {
            'dataIn': dict(io='in'),  # each terminal needs at least a name and
            'dataOut': dict(io='out'),  # to specify whether it is input or output
        }  # other more advanced options are available
        # as well..

        CtrlNode.__init__(self, name, terminals=terminals)

    def process(self, dataIn, display=True):
        # CtrlNode has created self.ctrls, which is a dict containing {ctrlName: widget}
        sigma = self.ctrls['sigma'].value()
        strength = self.ctrls['strength'].value()
        output = dataIn - (strength * pg.gaussianFilter(dataIn, (sigma, sigma)))

        return {'dataOut': output}


class ImageGray(CtrlNode):
    nodeName = 'ImageGray'
    uiTemplate = [
        ('checkGray', 'check', {'checked': True}),
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
        dataout = cv2.cvtColor(dataIn, cv2.COLOR_RGB2GRAY)
        return {'dataOut': dataout}


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
        try:
            minVal = float(self.ctrls['minVal'].value())
            maxVal = float(self.ctrls['maxVal'].value())
            aperture_size = int(self.ctrls['aperture_size'].value())
            L2gradient = bool(self.ctrls['L2gradient'].value())
            dataout = cv2.Canny(dataIn, minVal, maxVal, None, aperture_size, L2gradient)
            return {'dataOut': dataout}
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            print(f"minVal: {minVal}, maxVal: {maxVal}, aperture_size: {aperture_size}, L2gradient: {L2gradient}")

            return {'dataOut': None}


## To make our custom node classes available in the flowchart context menu,
## we can either register them with the default node library or make a
## new library.


## Method 1: Register to global default library:
'''方法一、设置类似全局变量的方法实现自定义节点'''
# fclib.registerNodeType(ImageViewNode, [('Display',)])
# fclib.registerNodeType(UnsharpMaskNode, [('Image',)])

## Method 2: If we want to make our custom node available only to this flowchart,
## then instead of registering the node type globally, we can create a new
## NodeLibrary:
'''方法二、设置单个窗口实现自定义的节点方法'''
library = fclib.LIBRARY.copy()  # start with the default node set
library.addNodeType(ImageViewNode, [('Display',)])
# Add the unsharp mask node to two locations in the menu to demonstrate
# that we can create arbitrary menu structures
library.addNodeType(UnsharpMaskNode, [('Vision',)])
library.addNodeType(ImageGray, [('Vision',)])

library.addNodeType(ImageDenoising, [('Vision',)])
library.addNodeType(ImageCanny, [('Vision',)])

fc.setLibrary(library)

## Now we will programmatically add nodes to define the function of the flowchart.
## Normally, the user will do this manually or by loading a pre-generated
## flowchart file.

v1Node = fc.createNode('ImageView', pos=(330, 0))
v1Node.setView(v1)

fNode = fc.createNode('UnsharpMask', pos=(110, 0))

cNode = fc.createNode('ImageGray', pos=(0, 0))

dNode = fc.createNode('ImageDenoising', pos=(220, 0))

eNode = fc.createNode('ImageCanny', pos=(0, 45))

fc.connectTerminals(fc['dataIn'], cNode['dataIn'])
fc.connectTerminals(fNode['dataOut'], v1Node['data'])
fc.connectTerminals(cNode['dataOut'], fNode['dataIn'])

fc.connectTerminals(dNode['dataIn'], fc['dataIn'])
fc.connectTerminals(eNode['dataIn'], fc['dataIn'])

if __name__ == '__main__':
    pg.exec()
