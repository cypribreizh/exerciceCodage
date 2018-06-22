#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 31 10:48:28 2018

@author: cyril
"""

class JeuDeNim:
    
    def __init__(self,nbAllumettes,joueur):
        self.nbAllumettes = nbAllumettes
        self.joueurCourant = 1

    def nextPlayer():
        if self.joueurCourant == 1:
            self.joueurCourant = 2
        else:
            self.joueurCourant = 1

    def play(nbAllumettes):
        self.nbAlumettes = self.nbAlumettes - nbAllumettes

    def run():
        # tant que le nombre d'allumettes != 0 (ou supérieur)
            # afficher à qui de joueur
            # demander une valeur entre 1 et 2
            # verifier que la valeur est correcte (1 ou 2)
            # retirer le nombre d'alllumettes choisies (méthode play)
            # changer de joueur (méthode nextPlayer)
        # Afficher le gagnant/perdant
            
jeu = JeuDeNim(22)
jeu.run()