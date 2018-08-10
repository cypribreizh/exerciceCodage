#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 24 11:04:33 2018

@author: cyril
"""
from random import randint

#Listes

verbe1 = ["déjeune", "fais du shopping", "danse le disco", "me marrie", "pratique la magie noire"]
verbe2 = ["prie","suis en train d'étudier", "prends mon bain", "commets un crime","m'amuse au lit"]
verbestotaux = verbe1+verbe2

perso1 = ["une japonaise", "mon supérieur hiérarchique", "ta maman", "Macron", "Jean-Kévin", "un parfois inconnu", "mon sosie", "Rihanna", "ta copine du lycée"]
perso2 = ["une sirène", "trois elfes", "un robot", "un alien", "Zeus", "le Diable", "Ondine", "Dieu", "le Yéti", "une poupée vivante"]
perso3 = ["mon chat", "un éléphant", "un dauphin", "un tricératops", "un requin", "une licorne", "une fourmi géante", "un arbre qui parle", "une armée de lapins"]

persoTotaux = perso1 + perso2 + perso3

Lieu = ["dans la forêt de Brocéliande", "sur une île du Pacifique", "dans une église", "dans un marécage", "sur un paquebot", "dans ma chambre", "sur la planète Mars", "dans l'univers de Dragon Ball Z"]
Moment = ["lors du Nouvel An chinois", "durant une nuit de pleine lune", "durant le 14 juillet", "pendant que le petit Matthéo nous observe de loin", "durant la fin du monde", "le jour de la St Valentin", "durant la nuit de Noel", "en présence de Barack Obama"]

#Choix aléatoires

iVerbe = randint(0,len(verbestotaux)-1)
aleaVerbe = verbestotaux[iVerbe]

persosChoisis = []
i =0
while i <3:
    iPerso = randint(0,len(persoTotaux)-1)
    aleaPerso = persoTotaux[iPerso]
    if aleaPerso not in persosChoisis:
        persosChoisis.append(aleaPerso)
        i += 1

iLieu = randint(0,len(Lieu)-1)
aleaLieu = Lieu[iLieu]

iMoment = randint(0,len(Moment)-1)
aleaMoment = Moment[iMoment]

# Phrase

print("Je " +aleaVerbe + " avec " + persosChoisis[0] + ", " + persosChoisis[1]  + " et "+ persosChoisis[2] + " " + aleaLieu + " " + aleaMoment)







