import numpy as np
import matplotlib.pyplot as plt
from prettytable import PrettyTable
from re import S
# declare constants
# interval [START_POINT, END_POINT] that is used to calculate Bisection 

START_POINT = 0  
END_POINT = 3
EPSILON = 0.1


class Function():
 
  def __init__(self, x):
    self.x = x
  
  def get_function_value (self):
    return self.x**2-self.x-2         # e.g.  np.exp(x) - 3*x and etc.

class Graph():

  def __init__(self, x_axes, y_axes):
     self.x_axes = x_axes
     self.y_axes = y_axes
  
  def create_graph(self):
    # initiate graph size
    plt.subplots(1, 1, figsize=(9, 3))

    # plot linearly spaced vectors
    linear_vectors = np.linspace(START_POINT, END_POINT, 1000)
    l_value = Function(linear_vectors)
    plt.plot(linear_vectors, l_value.get_function_value(), lw=1.5)
    
    # plot the roots calculated in iteration
    plt.plot(self.x_axes, self.y_axes)
 
    for i,txt in enumerate(self.y_axes):
      plt.text(self.x_axes[i], self.y_axes[i]-0.2, 'r%f' % self.y_axes[i])
  
    plt.plot(self.x_axes[len(self.x_axes)-1], self.y_axes[len(self.y_axes)-1], 'r*')
    plt.text(self.x_axes[len(self.x_axes)-1], self.y_axes[len(self.y_axes)-1]+0.2,  r"$solution: %f$" % self.x_axes[len(self.x_axes)-1], ha='center')

class Table():

  def __init__(self, header):
    self.header = header

  def create_table (self):
    return PrettyTable(self.header)

  def add_row(self, values):
    self.add_row(values)



def bisection_method(start_point, end_point, epsilon):

    x_values = []
    y_values = []

    # get the start and end point of interval [start_point, end_point]
    s_point = Function(start_point)
    e_point = Function(end_point)
    s_value = s_point.get_function_value()
    e_value = e_point.get_function_value()
  
    f_table = Table(['No. iteration', 'interval []', 'half_point', 'f(half_point)', 'length of interval'])
    f_table = f_table.create_table()
    
    if s_value * e_value > 0:
      raise Exception(f"Invalid interval [{start_point};{end_point}]. Start_point and End_point values should be opposite sign.")
    else:
        n = 0
        while(np.abs(end_point-start_point) > epsilon):
            half_point = (start_point+end_point)/2
            half_value = Function(half_point)
            x3 = half_value.get_function_value()

            n = n + 1
            x_values.append(half_point)
            y_values.append(x3)
            f_table.add_row( [n, f"[{start_point};{end_point}]", half_point, x3, abs(end_point - start_point)])

            if s_value * x3 < 0: 
              end_point = half_point
            else: 
              start_point = half_point

    print (f"APPROXIMATELY THE ROOT FOR EQUATION: {half_point}, THE INTERVAL [{start_point};{end_point}]")
    f_graph = Graph(x_values, y_values)
    f_graph.create_graph()
    print(f_table)


bisection_method(START_POINT,END_POINT,EPSILON)