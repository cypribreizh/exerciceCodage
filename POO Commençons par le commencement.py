#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 30 11:59:14 2018

@author: cyril
"""

class Animal:
    
    def __init__(self,espece,cri,deplacement):
        self.espece = espece
        self.cri = cri
        self.deplacement = deplacement
        
class chat(Animal):
    
    def __init__(self,nom, sexe):
        self.nom = nom
        self.sexe = sexe
        """
        self.espece = "Felis sylvestris catus"
        self.cri = "miaou"
        self.deplacement = "je me faufile"
        """
        super().__init__("Felis sylvestris catus", "miaou", "je me faufile")


mistigri = chat(nom = "Mistigri",sexe = "masculin")
midinette = chat(nom = "Midinette", sexe = "féminin")
patachon = chat(nom = "Patachon", sexe = "je suis castré")

print(mistigri.espece)
print(midinette.nom)
print(patachon.sexe)
print(midinette.deplacement)

class chien(Animal):
    
    def __init__(self,nom, sexe, race):
        self.espece = "Canis lupus familiaris"
        self.nom = nom
        self.sexe = sexe
        self.race = race
        self.cri = "Ouaf, ouaf !!"
        self.deplacement = "je saute !!"

ulrich = chien (nom = "Ulrich", sexe ="Masculin", race ="Berger allemand")
bernadette = chien (nom = "Bernadette", sexe = "Féminin", race = "Saint Bernard")
medor = chien (nom = "Médor", sexe ="Masculin", race ="Je suis un bâtard. Plus précisement un croisement entre un bouledogue et un chow chow")

print(bernadette.nom)
print(medor.race)

class escargot(Animal):
    
    def __init__(self,nom):
        self.espece = "Je suis un escargot de Gascogne"
        self.nom = nom
        self.sexe = "Hermaphrodite"
        self.cri = "Seules les fourmis peuvent m'entendre baver !!"
        self.deplacement = "je bave pour avancer dans la vie"

davidBowie = escargot(nom = "David Bowie")
print(davidBowie.espece)
print(davidBowie.sexe)
print(davidBowie.cri)

class humain(Animal):
    
    def __init__(self,nom,sexe,age,nationalite,langue,orientationSexuelle):
        self.espece = "Homo Sapiens"
        self.nom = nom
        self.sexe = sexe
        self.age = age
        self.nationalite = nationalite
        self.cri = langue
        self.langue = langue
        self.orientationSexuelle = orientationSexuelle
        self.deplacement = "je marche"

david = humain(nom = "David", sexe = "Masculin", age ="17 ans", nationalite = "française", langue = "franco-breton", orientationSexuelle = "Hétéro")
nathaly = humain(nom = "Nathaly", sexe = "Feminin", age ="32 ans", nationalite = "Canadienne", langue = "anglais", orientationSexuelle = "Sapphique")
timothe = humain(nom = "Timothé", sexe = "Masculin", age ="7 jours", nationalite = "suisse", langue = "doit apprendre la vie", orientationSexuelle = "n'a pas encore fait son choix")

print(david.langue)
print(david.cri)
print(nathaly.nationalite)
print(timothe.age)

print()
print(timothe.nom,timothe.age)





    


