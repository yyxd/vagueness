# _*_ coding: utf-8 _*_
# @Author: Diane
# @Time  : 2018/12/4 17:02
# @File  : temp.py
# @Goal  : test numpy

import numpy as np
import matplotlib.pyplot as plt
if __name__ == '__main__':
    x = np.linspace(-3,3,50)
    y1 = 2*x+1
    y2 = x**2
    plt.figure()
    plt.plot(x,y1)
    plt.plot(x,y2)