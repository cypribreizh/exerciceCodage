#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 09:09:05 2018

@author: cyril
"""
from random import randint

class personnage:

    def __init__(self,nom):
        self.nom = nom
        

    def __repr__(self):
        return "Votre perso s'appelle " + self.nom

    def randomPhrase(self):
        aleaPhrase = ["Je pense à " + self.nom, "J'écris le nom de " + self.nom + " dans mon carnet d'adresse","Je bats " +self.nom + " aux échecs","Je fais un tour en taxi avec "+self.nom,"J'invite " + self.nom + " à danser la rumba", "J'envoute " + self.nom + " avec une poupée vaudoue", "J'enquête sur les secrets familiaux de " + self.nom]
        i = randint(0,len(aleaPhrase)-1)
        print(aleaPhrase[i])

amelie = personnage(nom = "Amélie Poulain")
chuck = personnage(nom = "Chuck Norris")
laurent = personnage(nom = "Laurent Ruquier")

amelie.randomPhrase()
chuck.randomPhrase()
laurent.randomPhrase()
        
    