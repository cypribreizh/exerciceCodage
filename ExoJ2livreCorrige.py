#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 20 10:40:26 2018

@author: cyril
"""

from matplotlib.pyplot import *
from math import *

n = eval(input("Nb de côtés : "))
X, Y = [],[]

for k in range(n+1):
    X.append(5*cos(2*k*pi/n))
    Y.append(5*sin(2*k*pi/n))

plot(X, Y, 'b-')
axis('equal')
show()


    
