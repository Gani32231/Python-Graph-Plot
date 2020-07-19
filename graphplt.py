# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 16:16:24 2020

@author: wwwds
"""


import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
fig = plt.figure()
ax = plt.axes(projection="3d")
x=[1,2,3,4,5,6,7,8,9]
y=[2,3,4,6,7,8,9,5,1]
z=[5,6,2,4,8,6,5,6,1]
ax.scatter(x,y,x,color='r')
ax.set_xlabel('X Axes')
ax.set_ylabel('Y Axes')
ax.set_zlabel('Z Axes')
plt.show()
