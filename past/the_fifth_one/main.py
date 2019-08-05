import the_fifth_one.lib as lib
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

axis = lib.Axis(ax)

x = np.array([1, 2, 3, 4, 5])
y = x*x
xlim = [0, 6]
ylim = [0, 30]

parameters = {'x': x,
              'y': y,
              'linestyle': '',
              'color': '',
              'linewidth': '',
              'marker': 'o',
              'markercolor': 'r',
              'markersize': '',
              'label': ''
              }
axis.object1(parameters)

parameters = {'xlabel': '',
              'ylabel': '',
              'xlim': xlim,
              'ylim': ylim,
              'title': '',
              'legend': ''
              }
axis.ax_pre(parameters)

plt.show()
