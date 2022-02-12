#!/usr/bin/env python
# coding: utf-8

# In[25]:


import random as rn 

import numpy as np 

import math as ma 

import matplotlib as mpl

import matplotlib.pyplot as plt


# In[80]:


#without drag

v_o = float(input('Starting velocity? '))

theta = float(input('Starting angle? '))

dt = float(input('Time step? '))

x = 0.0
y = 0.0
vx = v_o*ma.cos(ma.radians(theta))
vy = v_o*ma.sin(ma.radians(theta))
ax = 0.0
ay = -9.8

q = 1

x_positions = []
y_positions = []

while q == 1: 
    while y >= 0: 
        x = vx*dt + x
        x_positions.append(x)
        vx = ax*dt + vx
        y = vy*dt + y
        y_positions.append(y)
        vy = ay*dt + vy
    if 7.5 > x > 6.5: 
        print('Hit!')
        print('Final position: ', x)
    else:
        print('Better luck next time!')
        print('Final position: ', x)
        print('You missed by: ', abs(7 - x))
    q = 0
        
    
print(x_positions)
print(y_positions)


# In[82]:


#with drag

v_o = float(input('Starting velocity? '))

theta = float(input('Starting angle? '))

dt = float(input('Time step? '))

g = -9.8

x2 = 0.0
y2 = 0.0
vx = v_o*ma.cos(ma.radians(theta))
vy = v_o*ma.sin(ma.radians(theta))
ax = 0.0
ay = g

print(vx)
print(vy)

b = 0.001

x2_positions = []
y2_positions = []

q = 1

while q == 1: 
    while y2 >= 0: 
        x2 = vx*dt + x2
        x2_positions.append(x2)
        vx = ax*dt + vx
        ax = 0 - b*vx
        y2 = vy*dt + y2
        y2_positions.append(y2)
        vy = ay*dt + vy
        ay = g - (b*vy)      
    if 7.5 > x > 6.5: 
        print('Hit!')
        print('Final position: ', x2)
    else:
        print('Better luck next time!')
        print('Final position: ', x2)
        print('You missed by: ', abs(7 - x2))
    q = 0
        
    
print(x2_positions)
print(y2_positions)


# In[83]:


#difference between analytical and simulated 

difference = x - x2

print(difference)


# In[81]:


plt.scatter(x_positions, y_positions)
plt.show()


# In[79]:


plt.scatter(x2_positions, y2_positions)
plt.show() 


# In[ ]:




