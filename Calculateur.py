#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 08:00:25 2018

@author: cyril
"""
from random import randint


nombre_a_multiplier = eval(input("Choisissez un nombre " ))

multiplications = eval(input("Choisissez un entier " ))


stockageFacteurs = list(range(1,multiplications+1))

castNombre_a_multiplier = str(nombre_a_multiplier)


print("Multiples de " + castNombre_a_multiplier)
print()

stockResultats = []

for i in stockageFacteurs:
    calcul = nombre_a_multiplier*i
    stockResultats.append(calcul)

print(stockResultats)
print()

print("Carré et Cube de " + castNombre_a_multiplier)
print(nombre_a_multiplier**2, nombre_a_multiplier**3)