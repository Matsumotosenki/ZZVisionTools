# 对位模块
import numpy as np
import math
import time


# 单点对位
class Counterpoint:
    def __init__(self, teaching_x, teaching_y, teaching_r, run_x, run_y, run_r):
        # t0 = time.time()
        # 偏移值
        self.offset = None
        # 矩阵
        self.teachingT = None
        self.run_T = None
        # 弧度
        self.radian = None
        # 示教的X、Y、R
        self.teachingX = teaching_x
        self.teachingY = teaching_y
        self.teachingR = teaching_r
        # 运行的X、Y、R
        self.run_x = run_x
        self.run_y = run_y
        self.run_r = run_r

        # t1 = time.time()
        # print(t1 - t0)

    # 齐次变换矩阵
    def homogeneous(self):
        try:
            # 角度转换弧度，再计算偏移数据
            # 示教角度 减 运行角度
            self.radian = (self.teachingR - self.run_r) / 180 * math.pi
            # 旋转矩阵 给运行位做旋转
            rotation_matrix = np.mat(np.array([
                [np.cos(self.radian), -np.sin(self.radian), 0],
                [np.sin(self.radian), np.cos(self.radian), 0],
                [0, 0, 1]

            ]))
            # 生成运行位矩阵
            self.run_T = np.mat(np.array([[self.run_x],
                                          [self.run_y],
                                          [1]
                                          ]))
            # 生成示教位矩阵
            self.teachingT = np.mat(np.array([[self.teachingX],
                                              [self.teachingY],
                                              [1]
                                              ]))
            # 计算平移的点位偏移 X、Y
            self.offset = self.teachingT - rotation_matrix * self.run_T
            self.offset[2] = float(self.teachingR - self.run_r)
            return self.offset
            # print(self.radian)
            # print(self.offset)
        except Exception as r:
            if ((not self.teachingX) or (not self.teachingY) or (not self.teachingR)
                    or (not self.run_x) or (not self.run_y) or (not self.run_r)):
                print('参数错误 %s' % r)
                return "参数错误"
            else:
                print('未知错误 %s' % r)
                return "未知错误"


    def x(self):
        return self.offset[0]

    def y(self):
        return self.offset[1]

    def r(self):
        return self.offset[2]



