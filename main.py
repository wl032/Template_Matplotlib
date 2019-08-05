import my_fig
import numpy as np

'''
这是该系列的主程序
目的是为每个子图准备数据
同时定义子图的title等
'''

data = []
data.append([[0, 1], [1, 1]])
data.append([[0, 1], [2, 2]])
data.append([[0, 1], [3, 3]])
data.append([[0, 1], [4, 4]])
data.append([[0, 1], [5, 5]])
data.append([[0, 1], [6, 6]])
data.append([[0, 1], [7, 7]])

fig1 = my_fig.Fig1()
fig1.fig_ax1(data)

xlim = [0, 1]
ylim = [0, 8]
parameters = {'xlabel': '',
              'ylabel': '',
              'xlim': xlim,
              'ylim': ylim,
              'title': '',
              'legend': ''
              }
fig1.fig_ax1_pre(parameters)

fig1.show()


fig2 = my_fig.Fig2()

x = np.array([1, 2, 3, 4])
p0 = np.poly1d([1])
y = p0(x)
data = [x, y]

fig2.fig_ax00(data)

xlim = [min(x), max(x)]
ylim = [min(y)-1, max(y)+1]

parameters = {'xlabel': '',
              'ylabel': '',
              'xlim': xlim,
              'ylim': ylim,
              'title': '',
              'legend': ''
              }
fig2.fig_ax00_pre(parameters)

x = np.array([1, 2, 3, 4])
p1 = np.poly1d([1, 0])
y = p1(x)
data = [x, y]

fig2.fig_ax01(data)

xlim = [min(x), max(x)]
ylim = [min(y)-1, max(y)+1]

parameters = {'xlabel': '',
              'ylabel': '',
              'xlim': xlim,
              'ylim': ylim,
              'title': '',
              'legend': ''
              }
fig2.fig_ax01_pre(parameters)

x = np.array([1, 2, 3, 4])
p2 = np.poly1d([1, 0, 0])
y = p2(x)
data = [x, y]

fig2.fig_ax10(data)

xlim = [min(x), max(x)]
ylim = [min(y)-1, max(y)+1]

parameters = {'xlabel': '',
              'ylabel': '',
              'xlim': xlim,
              'ylim': ylim,
              'title': '',
              'legend': ''
              }
fig2.fig_ax10_pre(parameters)

x = np.array([1, 2, 3, 4])
p3 = np.poly1d([1, 0, 0, 0])
y = p3(x)
data = [x, y]

fig2.fig_ax11(data)

xlim = [min(x), max(x)]
ylim = [min(y)-1, max(y)+1]

parameters = {'xlabel': '',
              'ylabel': '',
              'xlim': xlim,
              'ylim': ylim,
              'title': '',
              'legend': ''
              }
fig2.fig_ax11_pre(parameters)

fig2.show()
