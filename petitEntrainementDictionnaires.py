#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 15 13:23:41 2018

@author: cyril
"""

animauxSauvages = {}
animauxSauvages["Lions"] = 12
animauxSauvages["Eléphants"] = 7
animauxSauvages["Giraffes"] = 5
animauxSauvages["Gazelles"] = 20
animauxSauvages["Ouistitis"] = 32

print(animauxSauvages)

animauxDomestiques = {}
animauxDomestiques["Chats"] = 5
animauxDomestiques["Chiens"] = 4
animauxDomestiques["Lapins"] = 6
animauxDomestiques["Perruches"] = 7
animauxDomestiques["Poissons rouges"] = 5

print(animauxDomestiques)

#animaux_totaux = animauxSauvages + animauxDomestiques
#print(animaux_totaux)
#Apparemment, on ne peut pas additionner 2 dictionnaires

dicoStupide = {1 :"jeux de villains", 2 : "retourne au pieux", 3 : "perd la foi"}

for cle in animauxSauvages:
    print(cle)

print(dicoStupide[1])

dicoPlusUtile = {"Prénom" : "Jean", "Nom" : "Valjean", "Age" : "55", "Adresse" : "Rues de Paris"}

print(dicoPlusUtile["Adresse"])

for cle, valeur in dicoPlusUtile.items():
    print(valeur)

for cle, valeur in dicoPlusUtile.items():
    print(dicoPlusUtile[cle])
