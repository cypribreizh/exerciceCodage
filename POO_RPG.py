#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 31 10:24:49 2018

@author: cyril
"""

class personnage:
    
    def __init__(self,nom, categorie):
        self.nom = nom
        self.categorie = categorie


class joueur(personnage):
    
    def __init__(self,nom,sexe,race,classe):
        self.nom = nom
        self.categorie = "joueur"
        self.sexe = sexe
        self.race = race
        self.classe = classe

class elfe_sylvestre(joueur):
    
    def __init__(self,nom,sexe,race,classe):
        self.nom = nom
        self.categorie = "joueur"
        self.sexe = sexe
        self.race = "elfe"
        self.classe = classe

class PNJ(personnage):
    
    def __init__(self,nom,sexe,race,classe,alignement):
        self.nom = nom
        self.categorie = "PNJ"
        self.sexe = sexe
        self.race = race
        self.classe = classe
        self.alignement = alignement

class haut_elfe(PNJ):
    
    def __init__(self,nom,sexe,race,classe):
        self.nom = nom
        self.categorie = "joueur"
        self.sexe = sexe
        self.race = "elfe"
        self.classe = classe

class humain(joueur):
    
    def __init__(self,nom,sexe,race,classe):
        self.nom = nom
        self.categorie = "joueur"
        self.sexe = sexe
        self.race = "humain"
        self.classe = classe

class ennemi(PNJ):
    
    def __init__(self,nom,sexe,race,classe):
        self.nom = nom
        self.categorie = "joueur"
        self.sexe = sexe
        self.race = race
#        self.classe = classe comment faire s'il n'a pas de classe ? Un dragon n'a pas de classe
        self.alignement = "Mauvais (chaotique, loyal ou neutre, au choix)"

class guerrier(joueur):
    
    def __init__(self,nom,sexe,race,classe):
        self.nom = nom
        self.categorie = "joueur"
        self.sexe = sexe
        self.race = race
        self.classe = "guerrier"
        


        
        