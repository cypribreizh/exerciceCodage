#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 08:24:46 2018

@author: cyril
"""
import re
from re import search


prenomsFeminins1 = ["Anna", "Jessica", "Laetitia", "Jeanne", "Sabrina", "Caroline"]
prenomsFeminins2 =["Lily", "Mathilde", "Gertrude", "Daniella", "Béatrice", "Fiona"]
prenomsFeminins3 =["Veronica", "Alizee", "Eve", "Nathalie", "Tiffany", "Soizig"]

totalPrenoms = prenomsFeminins1 + prenomsFeminins2 + prenomsFeminins3

print("Prénoms se terminant par a : ")
for i in totalPrenoms:
    res = re.search(r"a$", i) != None
    if res:
        print(i)

print()
print("Prénoms se terminant par e : ")
for j in totalPrenoms:
    reg = re.search(r"e$", j) != None
    if reg:
        print(j)

print()
print("Prénoms possédant la lettre y")
for k in totalPrenoms:
    rek = re.search(r"y", k) != None
    if rek:
        print(k)

print()
print("Prénoms possédant la lettre L ou l")
for l in totalPrenoms:
    rel = re.search(r"[Ll]", l) != None
    if rel:
        print(l)

#Comment utiliser l'accent circonflexe pour les regex ?
#(car il se trouve hors de son usage normal)
        

        
    

