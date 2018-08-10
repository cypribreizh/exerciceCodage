#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 08:35:04 2018

@author: cyril
"""
import random


#Names

Name1 = ["Ocean","Oblivion","Heaven","Sky","Thunder","Sun","Love","Woman"]
Name2 = ["Mother", "Child", "Wife", "Husband", "Fairy", "Death", "Sunset"]
Name3 = ["Dawn", "Night","Moon", "Twilight", "Flower", "Spring", "Summer", "Autumn"]
Name4 = ["Winter","God", "Eternity", "Devil", "Virgin", "Illusion", "Delight", "Tentation"]
Name5 = ["Light", "Shadow", "Time","World", "Music", "Danse", "Wedding","Harmony"]

totalNames = Name1 + Name2 + Name3 + Name4 + Name5


#Adjectives

Adj1 = ["Sweet","Bitter","Bittersweet","Eternal","Mysterious","Eerie","Celestrial"]
Adj2 = ["Infernal","Holy","Carnal","Pure","Delusional","Primordial","Harmonious"]
Adj3 = ["Noble","Natural","Humble","Feminine","Magnificent", "Sorrowful","Spiritual"]

totalAdjectives = Adj1 + Adj2 + Adj3


#Verbs

Verb1 = ["danse with","shine like","desire","tempt","guide","tear","succomb to"]
Verb2 = ["cherishe","vanishe like","love", "disappeare like", "follow"]

Verb1ing = ["dansing with","shining like","desiring","tempting","guiding","tearing","succombing to"]
Verb2ing = ["cherishing","vanishing like","loving", "disappearing like", "following"]

totalVerb = Verb1 + Verb2
totalVerbing = Verb1ing + Verb2ing

#Poème
#

print("Oh, " + random.choice(totalAdjectives) + " " + random.choice(totalNames) + "...")
print("You are the " + random.choice(totalAdjectives) + " " + random.choice(totalNames) + " of the " + random.choice(totalNames) + "...")
print("But why are you " + random.choice(totalVerbing) + " the " + random.choice(totalAdjectives) + " " + random.choice(totalNames) +" ?")
print("If one day, you might decide to " + random.choice(totalVerb) + " the " + random.choice(totalAdjectives) + " " + random.choice(totalNames) + ",")
print("I may " + random.choice(totalVerb) + " you...")







