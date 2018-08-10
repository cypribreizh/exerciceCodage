#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 24 07:56:52 2018

@author: cyril
"""
from random import randint

verbe = ["mange", "mouille", "vend", "dessine", "torture", "caline", "coupe","nage avec", "joue avec","fais l'amour avec"]

mot1 = ["un gâteau", "un tableau", "une cuillère", "ta maman", "un arbre"]
mot2 =["un cambrioleur", "mon chat", "un personnage de manga", "une bouteille", "une armoire"]
motsTotaux = mot1 + mot2

objectif1 = ["devenir riche", "vaincre Chuck Norris", "apprendre le Japonais", "avoir un passeport américain", "faire des bébés"]
objectif2 = ["obtenir un prix Nobel", "guérir du Cancer", "devenir Maître du Monde", "rien", "être ton esclave"]
objectifsTotaux = objectif1 + objectif2


iVerbe = randint(0,len(verbe)-1)
aleaVerbe = verbe[iVerbe]

iMot = randint(0,len(motsTotaux)-1)
aleaMot = motsTotaux[iMot]

iObjectif = randint(0,len(objectifsTotaux)-1)
aleaObjectif = objectifsTotaux[iObjectif]

print("Je " + aleaVerbe + " " + aleaMot + " pour " + aleaObjectif)



