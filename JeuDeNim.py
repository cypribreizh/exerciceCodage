#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 07:53:39 2018

@author: cyril
"""

class JeuDeNim:
    
    def __init__(self,nbAllumettes,joueurCourant):
        self.nbAllumettes = nbAllumettes
        self.joueurCourant = 1

    def nextPlayer():
        if self.joueurCourant == 1:
            self.joueurCourant = 2
        else:
            self.joueurCourant = 1

    def play(nbAllumettes):
        self.nbAlumettes = self.nbAlumettes - choix()
    
    def choix(nbAllumettes):
        choixAllumettes = eval(input("Veuillez choisir 1 ou 2 allumettes"))

    def run():
        while self.nbAllumettes > 0:
            nextPlayer()
            print("C'est au tour de " + self.joueurCourant)
            choix()
            if choix(nbAllumettes == 1 or nbAllumettes ==2):
                choix(nbAllumettes)
            else:
                print("Veuillez insérer une valeur correcte !")
                choix(nbAllumettes)
            play()
            nextPlayer()
        print(self.joueurCourant + " a perdu !")
            
            
jeu = JeuDeNim(22)
jeu.run()