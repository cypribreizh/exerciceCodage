#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 20 10:08:12 2018

@author: cyril
"""
#Ne pas executer ce brouillon

import matplotlib.pyplot as plt

x = [0,5]
y = [0,0]
plt.plot(x,y)
plt.axis('equal')
plt.show()
plt.close()

#centre =[x=0,y=0]
#Evidemment, ça ne marche pas ainsi mais j'aurai essayé...
#Il doit bien exister un moyen de donner une identité à un point...

Xcentre = [0]
Ycentre = [0]
centre = plt.plot(Xcentre,Ycentre)
# Je sais que c'est ridicule mais on fait avec ce qu'on a...
plt.show()
plt.close()

#En supposant que j'arrive à "identifier" un point de réferénce
#Ici, il va y avaoir beaucoup "d'algorithmique" personnelle

pointRef = [x=5, y=0]

n = eval(imput("Veillez donner un nombre de côtés n pour votre figure géométrique (n>2)"))

angleAlpha = 360/n

i=1

while i*angleAlpha <= 360:
    créer nouveau point de coordonnée polaire(5,i*angleAlpha)
    i += 1

#Sympathique... Quand mon raisonnement et mes capaités de codage ne sont
#pas au même niveau...


