#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 30 13:28:30 2018

@author: cyril
"""
from random import randint

age = randint(15,99)
sexe = ["Masculin"]*10 + ["Féminin"]*10 + ["Transgenre"]*5

nationalite = ["français", "anglais", "espagnol","allemand", "italien", "americain", "chinois", "japonais", "indien", "australien", "marocain", "sénégalais", "chilien"]

orientationSexuelle = ["Hétéro"]*60 + ["Gay/lesbienne"]*24 + ["bi"]*12 + ["questionning"]*6 +["in the closet"]*6+ ["asexuel"]*2

convictionsPolitiques = ["Centriste", "Ecolo", "Féministe", "Socialiste", "Communiste","libéral", "conservateur", "royaliste", "gauliste", "fachiste", "néo-nazi", "complotiste", "apolitique", "éternel indécis", "girouette"]

religion = ["Catholique", "Protestant", "Orthodoxe", "Juif", "Sunnite", "Chiite", "Hindou", "Athée", "Agnostique", "membre d'une secte"]

class humain:
    
    def __init__(self):
        
        self.H_sexe = "Masculin"
        self.H_age = 25
        self.H_nationalite = "français"
        self.H_orientationSexuelle = "ne sais pas"
        self.H_convictionsPolitiques = "apolitique"
        self.H_religion = "athée"
        
    def randomHumain(self):
        i = randint(0,len(sexe)-1)
        self.H_sexe = sexe[i]
        self.H_age = age
        k = randint(0,len(nationalite)-1)
        self.H_nationalite = nationalite[k]
        l = randint(0,len(orientationSexuelle)-1)
        self.H_orientationSexuelle = orientationSexuelle[l]
        m = randint(0,len(convictionsPolitiques)-1)
        self.H_convictionsPolitiques = convictionsPolitiques[m]
        n = randint(0,len(religion)-1)
        self.H_religion = religion[n]
            

#control = humain()
#print(control.H_sexe,control.H_age,control.H_nationalite,control.H_orientationSexuelle,control.H_convictionsPolitiques,control.H_religion)

sim = humain()
sim.randomHumain()
print(sim.H_sexe,sim.H_age,sim.H_nationalite,sim.H_orientationSexuelle,sim.H_convictionsPolitiques,sim.H_religion)

