#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 08:14:12 2018

@author: cyril
"""

class Vehicule:
    
    def __init__(self,nom,typologie):
        self.nom = nom
        self.typologie = typologie

class VehiculeTerrestre(Vehicule):
    
    def __init__(self,nom,typologie,roues,moteur):
        self.nom = nom
        self.typologie = "Terrestre"
        self.roues = roues
        self.moteur = moteur

class DeuxRoues(VehiculeTerrestre):
    
    def __init__(self,nom,typologie,roues,moteur):
        self.nom = nom
        super().__init__("Terrestre","2")
        self.moteur = moteur

class Velo(DeuxRoues):
    
    def __init__(self,nom,typologie,roues,moteur):
        self.nom = nom
        super().__init__("Terrestre","2")
        self.moteur = "Tes mollets"
    
class Moto(DeuxRoues):
    
    def __init__(self,nom,typologie,roues,moteur):
        self.nom = nom
        super().__init__("Terrestre","2")
        self.moteur = "Pétrole"

class QuatreRoues(VehiculeTerrestre):
    
    def __init__(self,nom,typologie,roues,moteur,fonction):
        self.nom = nom
        super().__init__("Terrestre","4")
        self.moteur = moteur

class Voiture(QuatreRoues):
    
     def __init__(self,nom,typologie,roues,moteur,fonction):
        self.nom = nom
        super().__init__("Terrestre","4")
        self.moteur = "Pétrole le plus souvent"
        self.fonction = "Personnelle la plupart du temps"
        
class Camion(QuatreRoues):
    
    def __init__(self,nom,typologie,roues,moteur,fonction):
        self.nom = nom
        super().__init__("Terrestre","4","Pétrole")
        self.fonction = "Professionnelle : transport de marchandises"
    
    
class Tracteur(QuatreRoues):
    
    def __init__(self,nom,typologie,roues,moteur,fonction):
        self.nom = nom
        super().__init__("Terrestre","4","Pétrole")
        self.fonction = "Professionnelle : travaux agricoles"

class Bus(QuatreRoues):
    
    def __init__(self,nom,typologie,roues,moteur,fonction):
        self.nom = nom
        super().__init__("Terrestre","4","Pétrole")
        self.fonction = "Professionnelle ou transport en commun"

class Train(VehiculeTerrestre):
    
    def __init__(self,nom,typologie,roues,moteur,fonction):
        self.nom = nom
        self.typologie = "Terrestre"
        self.roues = "?"
        self.moteur = "fonctionne à l'électricité"
        self.fonction = "Transports en commun"

class Tramway(VehiculeTerrestre):
    
    def __init__(self,nom,typologie,roues,moteur,fonction):
        self.nom = nom
        super().__init__("Terrestre","zéro","Fonctionne à l'électricité", "Transports en commun")
        

class Metro(VehiculeTerrestre):
    
    def __init__(self,nom,typologie,roues,moteur,fonction):
        self.nom = nom
        super().__init__("Terrestre","zéro","Fonctionne à l'électricité", "Transports en commun")
        
class Carosse(VehiculeTerrestre):
    
    def __init__(self,nom,typologie,roues,moteur,fonction):
        self.nom = nom
        self.typologie = "Terrestre"
        self.roues = "4"
        self.moteur = "4 à 6 vrais chevaux"
        self.fonction = "voyages princiers"
    
    
        


    
    
    
    
    
    
    

     
        
