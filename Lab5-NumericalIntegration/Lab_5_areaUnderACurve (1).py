#!/usr/bin/env python
# coding: utf-8

# In[17]:


import numpy as np 
import math as ma 
import matplotlib.pyplot as plt 
import scipy.integrate as sp


x_min = -5.0

x_max = 5.0

f_str = lambda x: (x*-0.5) + 4

s_ana = sp.quadrature(f_str, -5.0, 5.0)[0]

print('straight line analytical solution: ', s_ana)

f_para = lambda x: (-0.29*x**2) - x + 12.5

p_ana = sp.quadrature(f_para, -5.0, 5.0)[0]

print('parabolic analytical solution: ', p_ana)

f_comp = lambda x: 1.0 + 10 * (x + 1.0) * np.exp(-x**2)

c_ana = sp.quadrature(f_comp, -5.0, 5.0)[0]

print('more complicated function analytical solution: ', c_ana)

dx = float(input('\nwidth of rectangle? '))

input_steps = int((x_max - x_min)/dx)

def straight_line_y(x):
    y = (x*-0.5) + 4
    return y
    
def parabola_y(x):
    y = (-0.29*x**2) - x + 12.5
    return y
    
def more_complicated_function_y(x): 
    y = 1.0 + 10*(x + 1.0)*np.exp(-x**2)
    return y

def approximate_straight_line(steps):
    area_straight_line = 0
    for x in np.linspace(x_min, x_max, steps): 
        area_straight_line += dx*straight_line_y(x + 0.5*dx)
    return area_straight_line

print('\nstraight line')
print('approximation:', approximate_straight_line(input_steps))
percent_difference = (abs(s_ana - approximate_straight_line(input_steps))/s_ana)*100
print('percent difference:', percent_difference, '%')

def approximate_parabola(steps):
    area_parabola = 0
    for x in np.linspace(x_min, x_max, steps): 
        area_parabola += dx*parabola_y(x + 0.5*dx)
    return area_parabola

print('\nparabolic')
print('approximation:', approximate_parabola(input_steps))
percent_difference = (abs(p_ana - approximate_parabola(input_steps))/p_ana)*100
print('percent difference:', percent_difference, '%')

def approximate_more_complicated_function(steps):
    area_more_complicated_function = 0
    for x in np.linspace(x_min, x_max, steps): 
        area_more_complicated_function += dx*more_complicated_function_y(x + 0.5*dx)
    return area_more_complicated_function

print('\nmore complicated function')
print('approximation:', approximate_more_complicated_function(input_steps))
percent_difference = (abs(c_ana - approximate_more_complicated_function(input_steps))/c_ana)*100
print('percent difference:', percent_difference, '%')

straight_line_trend = []
for x in range(1, 100):
    straight_line_trend.append((abs(s_ana - approximate_straight_line(x))/s_ana)*100)
plot1 = plt.figure(1)
plt.plot(range(1,100), straight_line_trend)
plt.title("Straight line: Percent Difference Approximation vs Step Size")
plt.xlabel("Step Size")
plt.ylabel("Percent Difference (%)")

parabola_trend = []
for x in range(1, 100):
    parabola_trend.append((abs(p_ana - approximate_parabola(x))/p_ana)*100)
plot2 = plt.figure(2)
plt.plot(range(1,100), parabola_trend)
plt.title("Parabola: Percent Difference Approximation vs Step Size")
plt.xlabel("Step Size")
plt.ylabel("Percent Difference (%)")

approximate_more_complicated_function_trend = []
for x in range(1, 100):
    approximate_more_complicated_function_trend.append((abs(c_ana - approximate_more_complicated_function(x))/c_ana)*100)
plot3 = plt.figure(3)
plt.plot(range(1, 100), approximate_more_complicated_function_trend)
plt.title("More Complicated Function: Percent Difference Approximation vs Step Size")
plt.xlabel("Step Size")
plt.ylabel("Percent Difference (%)")

plt.show()

