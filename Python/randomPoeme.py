#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 08:35:04 2018

@author: cyril
"""
from random import randint

#Names

Name1 = ["Ocean","Oblivion","Heaven","Sky","Thunder","Sun","Love","Woman"]
Name2 = ["Mother", "Children", "Wife", "Husband", "Fairy", "Death", "Sunset"]
Name3 = ["Dawn", "Night","Moon", "Twilight", "Flower", "Spring", "Summer", "Autumn"]
Name4 = ["Winter","God", "Eternity", "Devil", "Virgin", "Illusion", "Delight", "Tentation"]
Name5 = ["Light", "Shadow", "Time","World", "Music", "Danse", "Wedding","Harmony"]

totalNames = Name1 + Name2 + Name3 + Name4 + Name5

ialea = randint(0,len(totalNames)-1)
randomName = totalNames[ialea]


#Adjectives

Adj1 = ["Sweet","Bitter","Bittersweet","Eternal","Mysterious","Eerie","Celestrial"]
Adj2 = ["Infernal","Holy","Carnal","Pure","Delusional","Primordial","Harmonious"]
Adj3 = ["Noble","Natural","Humble","Feminine","Magnificent", "Sorrowful","Spiritual"]

totalAdjectives = Adj1 + Adj2 + Adj3

jalea = randint(0,len(totalAdjectives)-1)
randomAdj = totalAdjectives[jalea]

#Verbs

Verb1 = ["danse with","shine like","desire","tempt","guide","tear","succomb to"]
Verb2 = ["cherishe","vanishe like","love", "disappeare like", "follow"]

Verb1S = ["danses with","shines like","desires","tempts","guides","tears","succombs to"]
Verb2S = ["cherishes","vanishes like","loves", "disappeares like", "follows"]

Verb1ing = ["dansing with","shining like","desiring","tempting","guiding","tearing","succombing to"]
Verb2ing = ["cherishing","vanishing like","loving", "disappearing like", "following"]

totalVerb = Verb1 + Verb2
totalVerbS = Verb1S + Verb2S
totalVerbing = Verb1ing + Verb2ing

k1alea = randint(0,len(totalVerb)-1)
randomVerb = totalVerb[k1alea]

k2alea = randint(0,len(totalVerbS)-1)
randomVerbS = totalVerbS[k2alea]

k3alea = randint(0,len(totalVerbing)-1)
randomVerbing = totalVerbing[k3alea]

#Poème
#

print("Oh, " + randomAdj + " " + randomName + "...")
print("You are the " + randomAdj + " " + randomName + " of the " + randomName + "...")










