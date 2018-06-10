#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 18 08:10:22 2018

@author: cyril
"""

liste1 = ["Jérome", "Le Marchal", "45 ans", "18 rue de Saint Germain des Prés", "Paris"]
liste2 = ["Anne", "Jézéquel", "27 ans", "7 rue des Lilas", "Rennes"]
liste3 = ["JUL", "Wesh Gros", "Age inconnu, trop d'autotune", "Mars...eille", "On m'appelle l'OVNI"]

listeDeListes = liste1 + liste2 +liste3
print(listeDeListes)

print(len(listeDeListes))

# Ok, sur Python, impossible de faire des listes de listes comme sur R

listeDeListes2 = [liste1, liste2, liste3]
print(listeDeListes2)

#Autant pour moi, c'est possible

print(len(listeDeListes2))
print(listeDeListes2[0])
print(listeDeListes2[0][0])
print(listeDeListes2[0][1])
print(listeDeListes2[1][0])
