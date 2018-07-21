#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 12 16:49:23 2018

@author: cyril
"""

# Choisissez pour a, b, c et d des valeurs non nulles (pour éviter les problèmes
# avec les multiplications et les divisions)

a = 17
b = 23
c = 31
d = 45

tours = 12

def additionsFolles(a,b,c,d,tours):
    i = 0
    while i <= tours:
        a, b, c, d = a+b, b+c, c+d, d+a
        print(a, b, c, d)
        i = i+1

def soustractionsFolles(a,b,c,d,tours):
    i = 0
    while i <= tours:
        a, b, c, d = a-b, b-c, c-d, d-a
        print(a, b, c, d)
        i = i+1

def multiplicationsFolles(a,b,c,d,tours):
    i = 0
    while i <= tours:
        a, b, c, d = a*b, b*c, c*d, d*a
        print(a, b, c, d)
        i = i+1

def divisionsFolles(a,b,c,d,tours):
    i = 0
    while i <= tours:
        a, b, c, d = a/b, b/c, c/d, d/a
        print(a, b, c, d)
        i = i+1

def folieTotale(a,b,c,d,tours):
    i = 0
    while i <= tours:
        a, b, c, d = a+b, b-c, c*d, d/a
        print(a, b, c, d)
        i = i+1





print("Additions folles")
print(a,b,c,d)
additionsFolles(17,23,31,45,12)
print()

print("Soustractions folles")
print(a,b,c,d)
soustractionsFolles(-17,-23,-31,-45,12)
print()

print("Multiplications folles")
print(a,b,c,d)
multiplicationsFolles(3,4,5,6,5)
print()

print("Divisions folles")
print(a,b,c,d)
divisionsFolles(17,23,31,45,12)
print()

print("Folie Totale")
print(a,b,c,d)
folieTotale(17,23,31,45,12)
        
