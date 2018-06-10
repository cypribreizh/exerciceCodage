#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 22 08:20:32 2018

@author: cyril
"""

from random import randint

Voy = ["a","e","i","o","u","y"]
Cons = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","z"]


def creerMot(n):      
    mot = ""
    i = 0
    while i < n:
        pileouface = randint(0,1)
        if pileouface == 0:
            j = randint(0,len(Voy)-1)
            mot = mot + Voy[j]
        else:
            k = randint(0,len(Cons)-1)
            mot = mot + Cons[k]
        i+=1
    return(mot)

print(creerMot(9))

def repeterFonction(rep):
    i =0
    stockage = []
    while i < rep:
        usageFonction = creerMot(9)
        if usageFonction not in stockage:
            stockage.append(usageFonction)
            i += 1
    return(stockage)

print(repeterFonction(7))





  