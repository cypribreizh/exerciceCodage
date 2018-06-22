#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  7 08:23:17 2018

@author: cyril
"""

import re
from re import search

Interets1 = ["langues", "histoire", "géographie", "biologie", "politique"]
Interets2 = ["Jeux vidéo", "Anime et mangas", "Musique", "Vidéos Youtube"]
Interets3 = ["Amour et sexualité", "Psychologie", "Bouffe", "Théories du complot"]

MaListeDinterets = Interets1 + Interets2 + Interets3

print(MaListeDinterets)

# sorted(MalisteDinterets)


#MaListeDinterets.remove("Théories du complot")
#MaListeDinterets.insert(12, "Illuminti confirmed")

def IlluminatiConfirmed (list) :
    for i in list:
        Illuminati = re.search(r"Théories du complot", i) != None
        if Illuminati:
            list[i] = "Circulez, il n'y a rien à voir..."
            print(list)	

IlluminatiConfirmed(MaListeDinterets)

