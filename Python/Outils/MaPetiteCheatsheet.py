#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 25 10:19:29 2018

@author: cyril
"""
#Modules utiles

from random import randint

import matplotlib.pyplot as plt

import time
import datetime
from time import gmtime

import re
from re import search

#Formules utiles

i = randint(0,len("Insérez liste ici sans guillemets")-1)

l = list(range(0,17,2))


#Fonctions récursives


def factorielle(n):
    if (n==1):
        return 1
    else:
         return n * factorielle (n-1)

def fibbonacci(n):
    if (n==0) or (n==1):
        return 1
    else:
        return fibbonacci(n-1) + fibbonacci(n-2)

#Fonction sur les fractions

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

#Regex

for i in list:
    nomRegex = re.search(r"regex entre guillemets", i) != None
    if nomRegex:
        prit(i)

Exemple
for i in totalPrenoms:
    res = re.search(r"a$", i) != None
    if res:
        print(i)

#Fonction utile

def repeterFonction(rep):
    i =0
    stockage = []
    while i < rep:
        usageFonction = "insérer fonction ici sans guillemets"
        if usageFonction not in stockage:
            stockage.append(usageFonction)
            i += 1
    return(stockage)

print(repeterFonction(7))
