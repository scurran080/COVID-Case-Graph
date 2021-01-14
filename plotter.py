import matplotlib.pyplot as plt
import numpy as np
import math

# data is passed through as a list
#include an x label and a y label
def plot(data, x_label, y_label):
   x_axis = []
   y_axis = []
   for i in data:
      x_axis.append(str(i[0]))
      y_axis.append(i[1])
   xpos = np.arange(len(x_axis))
   plt.bar(x_axis,y_axis)
   plt.xticks(xpos, x_axis)
   plt.ylabel(y_label)
   plt.title(x_label)
   plt.xlim(0,56)
   plt.ylim(min(y_axis))
   plt.show()