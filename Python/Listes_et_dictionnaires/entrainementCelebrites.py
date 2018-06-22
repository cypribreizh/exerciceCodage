#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 12 14:04:28 2018

@author: cyril
"""
from random import randint

a, b, c, d = "Mickael Jackson", "Mariah Carey", "Rihanna", "Elvis"

e, f, g, h = "Britney Spears", "Miley Cyrus", "Nicky Minaj", "Cathy Perry"

i, j, k ,l = "David Bowie", "George Mickael", "Eminem", "Avril Lavigne"

m, n, o, p = "Bennassi Bros", "Cascada", "Evanescence", "Pink"

groupe1 = [a ,e, i, m]
groupe2 = [b, f, j, n]
groupe3 = [c, g, k, o]
groupe4 = [d, h, l, p]

print(groupe1)
print(groupe2)
print(groupe3)
print(groupe4)

StarSystem = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p]
print(StarSystem)

selectionTournee = []

nombre = 0

while nombre <= 4:
    ialea = randint(0,len(StarSystem)-1)
    if StarSystem[ialea] not in selectionTournee:
        selectionTournee.append(StarSystem[ialea])
        nombre = nombre + 1

print(selectionTournee)




