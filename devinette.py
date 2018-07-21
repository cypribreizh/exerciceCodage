#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 17:15:20 2018

@author: cyril
"""

from random import randint

randomNumber = randint (0, 100)

found = False

while found == False:
    choosenNumber = eval(input("Choisissez un nomber entre 0 et cent ?" ))
    if choosenNumber != randomNumber:
        if choosenNumber < randomNumber:
            print("Trop  petit")
        else:
            print ("Trop grand")
    else:
        found = True
        print ("Bravo ! Nombre trouvé")
            
    
    
    
    