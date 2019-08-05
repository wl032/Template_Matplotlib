'''
本程序的目的是定义
  ——轴坐标系中可能包含的对象

1. 程序提取了这些对象的关键参数
2. 对于这些对象具体的绘制，程序中不进行定义
'''


import matplotlib.pyplot as plt
import matplotlib.lines as lines

class Axis:
    def __init__(self, ax):
        self.ax = ax

    def object1(self, parameters):
        # parameters = {'x': '',
        #               'y': '',
        #               'linestyle': '',
        #               'color': '',
        #               'linewidth': '',
        #               'marker': '',
        #               'markercolor': '',
        #               'markersize': '',
        #               'label': ''
        #               }

        x = parameters['x']
        y = parameters['y']
        linestyle = parameters['linestyle']
        color = parameters['color']
        linewidth = parameters['linewidth']
        marker = parameters['marker']
        markercolor = parameters['markercolor']
        markersize = parameters['markersize']
        label = parameters['label']

        line = lines.Line2D(x, y)
        if not linestyle == '':
            line.set_linestyle(linestyle)
        if not color == '':
            line.set_color(color)
        if not linewidth == '':
            line.set_linewidth(linewidth)
        if not marker == '':
            line.set_marker(marker)
        if not markercolor == '':
            line.set_markeredgecolor(markercolor)
            line.set_markerfacecolor(markercolor)
        if not markersize == '':
            line.set_markersize(markersize)
        if not label == '':
            line.set_label(label)

        self.ax.add_line(line)

    def ax_pre(self, parameters):
        # parameters = {'xlabel': '',
        #               'ylabel': '',
        #               'xlim': '',
        #               'ylim': '',
        #               'title': '',
        #               'legend': ''
        #               }

        xlabel = parameters['xlabel']
        ylabel = parameters['ylabel']
        xlim = parameters['xlim']
        ylim = parameters['ylim']
        title = parameters['title']
        legend = parameters['legend']

        if not xlabel == '':
            self.ax.set_xlabel(xlabel)
        if not ylabel == '':
            self.ax.set_ylabel(ylabel)
        if not xlim == '':
            self.ax.set_xlim(xlim)
        if not ylim == '':
            self.ax.set_ylim(ylim)
        if not title == '':
            self.ax.set_title(title)
        if not legend == '':
            self.ax.set_legend(legend)
