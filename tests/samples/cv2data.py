"""
Author:Qychui
DATE:2023/9/20 16:43
File:cv2data.py
"""
import cv2
import numpy as np
import pyqtgraph as pg

data = np.random.normal(size=(100, 100))
data = 25 * pg.gaussianFilter(data, (5, 5))
data += np.random.normal(size=(100, 100))
data[40:60, 40:60] += 15.0
data[30:50, 30:50] += 15.0

output = cv2.imread('../images/A7R06362-1-e1603849094415.jpg')
# print(type(data))
# print(type(output))
f_output = cv2.cvtColor(output, cv2.COLOR_BGR2GRAY)
cv2.imshow('imgShow', f_output)
cv2.waitKey(0)

