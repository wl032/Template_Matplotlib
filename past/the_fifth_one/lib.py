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


# def operation(ax):
#     x = [1, 2, 1.5, 1.5]
#     y = [1, 1, 0.5, 1.5]
#     line = lines.Line2D(x, y)
#     ax.add_line(line)
#     ax.axis([0, 3, 0, 3])
#
#
# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
# plt.axis([0, 6, 0, 20])
# plt.show()
