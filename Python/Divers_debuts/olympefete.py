#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 18:21:42 2018

@author: cyril
"""
from random import randint

def rechercheDieu(nomDieu,listeOlympe):
    for unDieu in listeOlympe:
        if nomDieu == unDieu:
            return True
    return False

listedieux = ["Zeus", "Poséidon", "Hadès", "Athéna", "Aphrodite"]
listedieux2 =["Héra","Apollon", "Hermès", "Artémis", "Hestia"]

#for i in range(len(listedieux)):
#    print (listedieux[i] + " donne un cadeau à " + listedieux2[i])
    
listeOlympe = listedieux +listedieux2
#print(listeOlympe)

listeInvites = []

i = 0

while i <= len(listeOlympe)-1:
    ialea = randint(0,len(listeOlympe)-1)
    print(ialea)
    if ialea != i and listeOlympe[ialea] not in listeInvites:
        listeInvites.append(listeOlympe[ialea])
        i = i+1
        

for i in range(len(listeOlympe)):
    print (listeOlympe[i] + " donne un cadeau à " + listeInvites[i])
 
    

    