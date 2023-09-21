"""
Author:Qychui
DATE:2023/9/20 14:22
File:processing.py
"""
import numpy as np
import pyqtgraph as pg
from pyqtgraph.flowchart.library.common import CtrlNode
from pyqtgraph.flowchart import Node

class MonaWin():
    def __init__(self):
        print('win')
    def started(self):
        print('winwin')

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

class UnsharpMaskNode(CtrlNode):
    """Return the input data passed through an unsharp mask."""
    nodeName = "UnsharpMask"
    uiTemplate = [
        ('sigma', 'spin', {'value': 1.0, 'step': 1.0, 'bounds': [0.0, None]}),
        ('strength', 'spin', {'value': 1.0, 'dec': True, 'step': 0.5, 'minStep': 0.01, 'bounds': [0.0, None]}),
        ('main','spin',{'value':1.0,'step':2.0,'bounds':[0.0,None]})
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

def Momo():
    print('Momo')
