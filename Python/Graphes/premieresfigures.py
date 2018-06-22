# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

"""

import matplotlib.pyplot as plt

#Ligne droite et brisée

plt.plot([0,1,2])
plt.show()
plt.close()

plt.plot([1,0,2])
plt.show()
plt.close()

x=[0,1,2]
y=[1,0,2]
plt.plot(x,y)
plt.show()
plt.close()

#Triangle

x=[1, 2, 0, 1]
y=[0, 2, 1, 0]
plt.plot(x,y)
plt.show()
plt.close()

#Plusieurs droites

x = [0, 1, 0]
y = [0, 1, 2]
x1 = [0, 2, 0]
y1 = [2, 1, 0]
x2 = [0, 1, 2]
y2 = [0, 1, 2]

plt.plot(x,y)
plt.plot(x1,y1)
plt.plot(x2,y2)
plt.show()
plt.close()

#2 carrés

x = [-1, 1, 1, -1, -1]
y = [-1, -1, 1, 1, -1]
plt.plot(x,y)
plt.show()
plt.close()

x = [-1, 0, 1, 0, -1]
y = [0, -1, 0, 1, 0]
plt.plot(x,y)
plt.show()
plt.close()

#Fonction carrés et autres figures

def carre (x, y):
    
    X = [x, x+10, x+10, x, x]
    Y = [y, y, y+10, y+10, y]
    plt.plot (X, Y)
    print ('carre')

  
for i in range(1,5):
    X=i
    Y=i
    carre (X, Y)

plt.show()

def rectangle (x, y):
    
    X = [x, x+20, x+20, x, x]
    Y = [y, y, y+10, y+10, y]
    plt.plot (X, Y)
    print ('rectangle')

  
for i in range(1,5):
    X=i
    Y=i
    rectangle (X, Y)

plt.show()

def triangle (x, y):
    
    X = [x, x+20, x+10, x]
    Y = [y, y, y+10, y]
    plt.plot (X, Y)
    print ('triangle')

  
for i in range(1,5):
    X=i
    Y=i
    triangle (X, Y)

plt.show()

#def cercle (a):
#    X = cos(a)
#    Y = sin(a)
#    plt.plot(X,Y)
#
#for i in range(0,360):
#    cercle(i)
#
#plt.show()





    




