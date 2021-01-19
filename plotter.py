import matplotlib.pyplot as plt
import matplotlib.legend
import numpy as np
import math

# data is passed through as a list
#include an x label and a y label
def bar_graph(data, x_label, y_label,title):
   x_axis = []
   y_axis = []
   for i in data:
      x_axis.append(str(i[0]))
      y_axis.append(i[1])
   xpos = np.arange(len(x_axis))
   plt.bar(x_axis,y_axis)
   plt.grid()
   plt.xticks(xpos, x_axis)
   plt.ylabel(y_label)
   plt.xlabel(x_label)
   plt.title(title)
   plt.xlim(0,len(data))
   plt.ylim(min(y_axis))
   plt.show()

def line_graph(data, x_label, y_label, title):
   x_axis = []
   y_axis = []
   for i in data:
      x_axis.append(str(i[0]))
      y_axis.append(i[1])
   xpos = np.arange(len(x_axis))
   plt.plot(y_axis)
   plt.grid()
   plt.xticks(xpos, x_axis, rotation = "vertical")
   plt.title(title)
   plt.ylabel(y_label)
   plt.xlabel(x_label)
   plt.xlim(0, len(data))
   plt.ylim(min(y_axis))
   plt.show()
