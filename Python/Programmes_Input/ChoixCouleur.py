#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 13 08:15:54 2018

@author: cyril
"""

# Choississez une couleur : "bleu", "vert", "rouge", "jaune", "autre"

premierChoix = eval(input("Bleu = 1, Vert = 2, Rouge = 3, Jaune = 4, Autre =5 :"))

if premierChoix == 1:
    secondChoix1 = 0
    secondChoix1 = eval(input("Cyan = 1, Turquoise =2, Bl.Marine = 3, Azur = 4 :"))
    if secondChoix1 == 1:
        print("Cyan")
    elif secondChoix1 == 2:
        print("Turquoise")
    elif secondChoix1 == 3:
        print("Bleu Marine")
    elif secondChoix1 == 4:
        print("Azur")
    else:
        print("Valeur incorrecte")

elif premierChoix == 2:
    secondChoix2 = 0
    secondChoix2 = eval(input("Pomme = 1, Gazon = 2, Sapin = 3, Jade = 4 :"))
    if secondChoix2 == 1:
        print("Pomme")
    elif secondChoix2 == 2:
        print("Gazon")
    elif secondChoix2 == 3:
        print("Sapin")
    elif secondChoix2 == 4:
        print("Jade")
    else:
        print("Valeur incorrecte")
    

elif premierChoix == 3:
    secondChoix3 = 0
    secondChoix3 = eval(input("Feu = 1, Carmin = 2, Pourpre = 3, Vermillon = 4 :"))
    if secondChoix3 == 1:
        print("Feu")
    elif secondChoix3 == 2:
        print("Carmin")
    elif secondChoix3 == 3:
        print("Pourpre")
    elif secondChoix3 == 4:
        print("Vermillon")
    else:
        print("Valeur incorrecte")

elif premierChoix == 4:
    secondChoix4 = 0
    secondChoix4 = eval(input("Citron = 1, Doré = 2, Blond Vénitier = 3, Caca d'oie = 4 :"))
    if secondChoix4 == 1:
        print("Citron")
    elif secondChoix4 == 2:
        print("Doré")
    elif secondChoix4 == 3:
        print("Blond Vénitien")
    elif secondChoix4 == 4:
        print("Caca d'oie")
    else:
        print("Valeur incorrecte")


elif premierChoix == 5:
    secondChoix5 = 0
    secondChoix5 = eval(input("Violet = 1, Orange = 2, Noir = 3, Blanc = 4, Rose = 5 :"))
    if secondChoix5 == 1:
        print("Violet")
    elif secondChoix5 == 2:
        print("Orange")
    elif secondChoix5 == 3:
        print("Noir")
    elif secondChoix5 == 4:
        print("Blanc")
    elif secondChoix5 == 5:
        print("Rose")
    else:
        print("Valeur incorrecte")
    
    
else:
    print("Valeur incorrecte")
   
