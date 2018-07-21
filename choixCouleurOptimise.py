#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 20 07:55:53 2018

@author: cyril
"""
# Premier choix

premierChoix = ["bleu", "vert", "rouge", "jaune", "autre"]

print(premierChoix)

premiereDecision = eval(input("Tapez 1 pour bleu, 2 pour vert, etc :"))

#try :
#    isinstance(premiereDecision, int) and premiereDecision in list(range(0,5))
#except:
#    print("valeur incorrecte")

i = premiereDecision - 1
print("Vous avez donc choisi : " + premierChoix[i])
print()

# Second choix

nuancesBleu =["Cyan", "Turquoise", "Bleu Marine", "Azur"]
nuancesVert =["Pomme", "Gazon", "Sapin", "Jade"]
nuancesRouge=["Feu", "Carmin", "Pourpre", "Vermillon"]
nuancesJaune=["Citron", "Doré" "Blond Vénitier", "Caca d'oie"]
autresCouleurs = ["Violet", "Orange", "Noir", "Blanc", "Rose"]

secondChoix = [nuancesBleu, nuancesVert, nuancesRouge, nuancesJaune, autresCouleurs]

print(secondChoix[i])
print()

deuxiemeDecision = eval(input("Même principe que précédemment : "))

j = deuxiemeDecision - 1
print("Vous avez donc choisi : " + secondChoix[i][j])


