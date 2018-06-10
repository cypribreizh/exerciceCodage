#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 09:02:09 2018

@author: cyril
"""

class Vehicule:
    
    def __init__(self,nom,typologie):
        self.nom = nom
        self.typologie = typologie

class VehiculeAquatique(Vehicule):
    
    def __init__(self,nom,typologie):
        self.nom = nom
        self.typologie = "aquatique"

class Bateau(VehiculeAquatique):
    
    def __init__(self,nom,typologie,taille,energie):
        self.nom = nom
        self.typologie = "aquatique"
        self.taille = taille
        self.energie = energie

class barque(Bateau):
    
    def __init__(self,nom,typologie,taille,energie):
        self.nom = nom
        self.typologie = "aquatique"
        self.taille = "petit"
        self.energie = "Allez, rames !"
    
class trimaran(Bateau):
    
    def __init__(self,nom,typologie,taille,energie,coques):
        self.nom = nom
        self.typologie = "aquatique"
        self.taille = "moyen"
        self.energie = "Vent"
        self.coques = "3"

class chalutier(Bateau):
    
    def __init__(self,nom,typologie,taille,energie):
        self.nom = nom
        self.typologie = "aquatique"
        self.taille = "moyen"
        self.energie = "Pétrole"

class Transatlantique(Bateau):
    
    def __init__(self,nom,energie,longueur,ponts,passagers):
        self.nom = nom
        self.typologie = "aquatique"
        self.taille = "gigantesque"
        self.energie = energie
        self.longueur = longueur
        self.ponts = ponts

Titanic = Transatlantique(nom = "Titanic",energie = "Charbon",longueur = "269 m",ponts = "10",passagers = "2471")
QueenMary2 = Transatlantique(nom = "Queen Mary 2",energie = "Pétrole",longueur = "345 m",ponts = "17",passagers = "3000 maximum")
    
class TroisMats(Bateau):
    
    def __init__(self,nom,typologie,taille,energie):
        self.nom = nom
        self.typologie = "aquatique"
        self.taille = "grande"
        self.energie = "vent"

class PorteAvions(Bateau):
    
    def __init__(self,nom,typologie,taille,energie):
        self.nom = nom
        self.typologie = "aquatique"
        self.taille = "gigantesque"
        self.energie = "Pétrole"

class SousMarin(VehiculeAquatique):
    
    def __init__(self,nom,typologie,taille,energie,autonomie,profondeurMax):
        self.nom = nom
        self.typologie = "aquatique"
        self.taille = "grande"
        self.energie = "Pétrole"
        self.autonomie = "7 jours"
        self.profondeurMax = "150 m"

class VehiculeAerien(Vehicule):
    
    def __init__(self,nom,typologie):
        self.nom = nom
        self.typologie = "aérien"
        
class Avion(VehiculeAerien):
    
    def __init__(self,nom,typologie,ailes,energie):
        self.nom = nom
        self.typologie = "aérien"
        self.ailes = "2"
        self.energie = "Pétrole le plus souvent"

class Helicoptere(VehiculeAerien):
    
    def __init__(self,nom,typologie,VoiluresTournantes,energie):
        self.nom = nom
        self.typologie = "aérien"
        self.VoiluresTournantes = "2"
        self.energie = "Pétrole"

class Montgolfière(VehiculeAerien):
    
    def __init__(self,nom,typologie,Nacelle,energie):
        self.nom = nom
        self.typologie = "aérien"
        self.VoiluresTournantes = "1"
        self.energie = "Air chaud et vent"

class VehiculeSpacial(Vehicule):
    
    def __init__(self,nom,typologie):
        self.nom = nom
        self.typologie = "spacial"

class fusee(VehiculeSpacial):
    
    def __init__(self,nom,typologie,etages,energie):
        self.nom = nom
        self.typologie = "spacial"
        self.etages = "3"
        self.energie = "Pétrole, puis solaire pour le dernier étage"
    
class satellite(VehiculeSpacial):
    
    def __init__(self,nom,typologie,energie,deplacement):
        self.nom = nom
        self.typologie = "spacial"
        self.energie = "Solaire"
        self.deplacement = "circulaire ou géostationnaire"

class Ovni(VehiculeSpacial):
    
    def __init__(self,nom,typologie,etages,energie,origine):
        self.nom = "Inconnu"
        self.typologie = "spacial"
        self.energie = "Inconnue"
        self.origine = "Inconnue"
    
    
    
    




    
    



    
    
    
    

 
    
    
        
