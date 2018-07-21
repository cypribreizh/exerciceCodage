#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 11 13:12:09 2018

@author: cyril
"""

def ajouteFrac(n1,d1,n2,d2):
    if d1 == 0 or d2 == 0:
        print("Division par zéro impossible")
    else:
        calcul = n1/d1 + n2/d2
        print(calcul)

def multiplieFrac(n1,d1,n2,d2):
    if d1 == 0 or d2 == 0:
        print("Division par zéro impossible")
    else:
        calcul = (n1/d1)*(n2/d2)
        print(calcul)

ajouteFrac(1,3,1,2)
multiplieFrac(3,1,2,1)

def simplifieFrac(n1,d1,n2,d2):
    x = [2,3,5,7]
    ajouteFrac(n1,d1,n2,d2)
    multiplieFrac(n1,d1,n2,d2)
    for diviseur in x:
        if (n1*d2)/(n2*d1) == diviseur:
            calcul2 = ((n1*d2)/diviseur)

