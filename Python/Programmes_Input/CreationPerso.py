#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 10:21:57 2018

@author: cyril
"""

class personnage:
    
#    def __init__(self,nom,age,lieuDhabitation,reve,soucis):
#        self.nom = nom
#        self.age = age
#        self.lieuDhabitation = lieuDhabitation
#        self.reve = reve
#        self.soucis = soucis
        
#        self.nom = "Vincent"
#        self.age = "23"
#        self.lieuDhabitation = "Lille"
#        self.reve = "avoir un boulot et une copine"
#        self.soucis = "les problèmes de trains et de bus !"

    def creationPerso(self):
        self.nom = input("Choisissez un nom ")
        self.age = input("Choisissez un age ")
        self.lieuDhabitation = input("Choisissez un lieu d'habitation ")
        self.reve = input("Choisissez le rêve de votre personnage ")
        self.soucis = input("Choisissez le ou les petits problèmes de votre perso ")

    def __repr__(self):
        return "Votre perso s'appelle " + self.nom + ", il a " + self.age + "ans et il habite à "+self.lieuDhabitation + ". Son rêve est de " + self.reve + ". Mais il a quelques soucis : " + self.soucis + "..."

    def __str__(self):
        pass

essai = personnage()
essai.creationPerso()
print(essai)

