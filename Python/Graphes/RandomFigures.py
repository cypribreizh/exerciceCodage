#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  9 09:05:49 2018

@author: cyril
"""

from random import randint

import matplotlib.pyplot as plt


ListeDesX = []
ListeDesY = []


i=0
n=0
while i <= 6:
    alea = randint(-5,5)
    n = alea
    ListeDesX.append(n)
    alea = randint(-5,5)
    n = alea
    ListeDesY.append(n)
    i += 1


x = ListeDesX
y = ListeDesY
plt.plot(x,y)
plt.show()







