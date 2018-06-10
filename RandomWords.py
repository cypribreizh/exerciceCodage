#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  9 09:22:54 2018

@author: cyril
"""
from random import randint

Voy = ["a","e","i","o","u","y"]
Cons = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","z"]

def Lettre(list):
    i = randint(0,len(list)-1)
    print(list[i])



Lettre(Cons), Lettre(Voy),Lettre(Voy),Lettre(Cons),Lettre(Cons),Lettre(Voy)

print()

Lettre(Voy),Lettre(Voy),Lettre(Cons),Lettre(Voy),Lettre(Cons)









