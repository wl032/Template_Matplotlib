'''
本程序的目的是定义
  ——图像的布局
  ——并且指定非数据层面的信息

1. 非数据层面的信息指的是线型、颜色等
2. 整个ax的信息需在外部定义
'''

import matplotlib.pyplot as plt
import numpy as np
import my_ax


class Fig1:

    color_list = ['#FF0000',
                  '#FF7D00',
                  '#FFFF00',
                  '#00FF00',
                  '#00FFFF',
                  '#0000FF',
                  '#FF00FF']

    def __init__(self):
        fig, ax = plt.subplots()
        self.fig = fig
        self.ax = my_ax.Axis(ax)

    def fig_ax1(self, data):
        n = len(data)
        for i in range(n):
            parameters = {'x': data[i][0],
                          'y': data[i][1],
                          'linestyle': '',
                          'color': self.color_list[i],
                          'linewidth': '',
                          'marker': '',
                          'markercolor': '',
                          'markersize': '',
                          'label': ''
                          }
            self.ax.object1(parameters)

    def fig_ax1_pre(self, parameters):
        self.ax.ax_pre(parameters)

    def show(self):
        plt.show()



class Fig2:

    def __init__(self):
        fig, axs = plt.subplots(nrows=2, ncols=2)
        self.fig = fig
        self.ax00 = my_ax.Axis(axs[0, 0])
        self.ax01 = my_ax.Axis(axs[0, 1])
        self.ax10 = my_ax.Axis(axs[1, 0])
        self.ax11 = my_ax.Axis(axs[1, 1])

    def fig_ax00(self, data):
        parameters = {'x': data[0],
                      'y': data[1],
                      'linestyle': '',
                      'color': '',
                      'linewidth': '',
                      'marker': '',
                      'markercolor': '',
                      'markersize': '',
                      'label': ''
                      }
        self.ax00.object1(parameters)

    def fig_ax00_pre(self, parameters):
        self.ax00.ax_pre(parameters)

    def fig_ax01(self, data):
        parameters = {'x': data[0],
                      'y': data[1],
                      'linestyle': '',
                      'color': '',
                      'linewidth': '',
                      'marker': '',
                      'markercolor': '',
                      'markersize': '',
                      'label': ''
                      }
        self.ax01.object1(parameters)

    def fig_ax01_pre(self, parameters):
        self.ax01.ax_pre(parameters)

    def fig_ax10(self, data):
        parameters = {'x': data[0],
                      'y': data[1],
                      'linestyle': '',
                      'color': '',
                      'linewidth': '',
                      'marker': '',
                      'markercolor': '',
                      'markersize': '',
                      'label': ''
                      }
        self.ax10.object1(parameters)

    def fig_ax10_pre(self, parameters):
        self.ax10.ax_pre(parameters)

    def fig_ax11(self, data):
        parameters = {'x': data[0],
                      'y': data[1],
                      'linestyle': '',
                      'color': '',
                      'linewidth': '',
                      'marker': '',
                      'markercolor': '',
                      'markersize': '',
                      'label': ''
                      }
        self.ax11.object1(parameters)

    def fig_ax11_pre(self, parameters):
        self.ax11.ax_pre(parameters)

    def show(self):
        plt.show()
