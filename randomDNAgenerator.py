#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 21 08:26:31 2018

@author: cyril
"""
from random import randint

nucleotide = ["A", "C", "G", "T"]

#brin1 = []
#i=0

#while i <= 60:
#    alea = randint(0,len(nucleotide)-1)
#    brin1.append(nucleotide[alea])
#    i += 1

brin1 = ""
i=0

while i <= 60:
    alea = randint(0,len(nucleotide)-1)
    brin1 = brin1 +nucleotide[alea]
    i += 1

print(brin1)

#Maintenant que je sais qu'on peut remplir une chaîne de caractères vide aussi facilement que pour une liste vide...

