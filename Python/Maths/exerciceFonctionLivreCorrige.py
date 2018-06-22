#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 11 13:54:08 2018

@author: cyril
"""

def pgcd(a,b):
    while b != 0:
        a, b = b, a % b
    return a

def simplifieFrac(num,den):
    d = pgcd(num,den)
    return num // d, den // d

def ajouteFrac(n1,d1,n2,d2):
    return simplifieFrac(n1*d2 + d1*n2, d1*d2)

def multiplieFrac(n1,d1,n2,d2):
    return simplifieFrac(n1*n2, d1*d2)

print(ajouteFrac(1,2,1,6))

print(multiplieFrac(2,3,5,4))

# //: divide with integral result (discard remainder)
# Traduction littérale  // : divise avec le résultat intégral (ne tient pas compte du reste)

#Meilleure traduction // : divise en donnant le résultat intégral (ne donne pas le reste)
#Maintenant, je sais que ça permet de faire une division euclidienne.



