#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 30 13:08:39 2018

@author: cyril
"""

class eleve:
    
    def __init__(self,nom,sexe,age,caractere,matieresPreferees,loisirs):
        self.nom = nom
        self.sexe = sexe
        self.age = age
        self.caractere = caractere
        self.matieresPreferees = matieresPreferees
        self.loisirs = loisirs
    
    def recup_caractere(self):
        print(self.caractere)

fiona = eleve(nom = "Fiona", sexe = "F", age = "17", caractere = "curieuse et bavarde", matieresPreferees ="Français et Anglais", loisirs = "Lecture et Shopping")
jerome = eleve(nom = "Jérome", sexe = "M", age = "15", caractere = "violent et indiscipliné", matieresPreferees ="Le sport, c'est tout", loisirs = "La drague lourde, très lourde")
emilie = eleve(nom = "Emilie", sexe = "F", age = "19", caractere = "calme et réservée", matieresPreferees = "Arts plastique et SVT", loisirs = "danse et musique")
vincent = eleve(nom = "Vincent", sexe = "M", age = "16", caractere = "l'intello de service", matieresPreferees ="Latin Grec", loisirs = "Bosser, et faire de l'astronomie")

vincent.recup_caractere()

class professeur:
    
    def __init__(self,nom,sexe,age,matieresEnseignees,caractere):
        self.nom = nom
        self.sexe = sexe
        self.age = age
        self.matieresEnseignees = matieresEnseignees
        self.caractere = caractere

Mme_Verdont = professeur(nom = "Valérie Verdont", sexe = "F", age = "42", matieresEnseignees = "SVT",caractere = "Enthousiaste et excentrique, mais compétente")
Mr_Duchemin = professeur(nom = "Gérard Duchemin", sexe = "M", age = "51", matieresEnseignees = "Histoire Géo", caractere = "Le petit vieux sympathique mais soporifique")
Mlle_Boutin = professeur(nom = "Sylvie Boutin", sexe = "F", age = "23", matieresEnseignees = "Français", caractere = "La jeune fille timide avec des lunettes et quelques courbes")
Mr_Coudrier = professeur(nom = "Vincent Coudrier",sexe = "M", age = "31", matieresEnseignees = "Mathématiques", caractere= "Le nouveau prof sévère et exigent")

print(Mme_Verdont.caractere,Mr_Duchemin.caractere,Mlle_Boutin.caractere,Mr_Coudrier.caractere)


        

