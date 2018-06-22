#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 07:53:39 2018

@author: cyril
"""

class JeuDeNim:
    
    def __init__(self, nbAllumettes):
        self.nbAllumettes = nbAllumettes
        self.joueurCourant = 1

    def nextPlayer(self):
        if self.joueurCourant == 1:
            self.joueurCourant = 2
        else:
            self.joueurCourant = 1

    def play(self,nbAllumettes):
        self.nbAllumettes = self.nbAllumettes - nbAllumettes
    
    def choix(self):
        choixAllumettes = eval(input("Veuillez choisir 1 ou 2 allumettes"))
        # faire le contrôle du nombre d'allumettes : 1 ou 2 seulement
        return choixAllumettes

    def run(self):
        while self.nbAllumettes > 0:
            print(self)
            print("C'est au tour de " + str(self.joueurCourant))
            self.play(self.choix())
            self.nextPlayer()
        print("{} a perdu".format(self.joueurCourant))
        
    def __repr__(self):
        strJeu = ""
        for i in range(0, self.nbAllumettes):
            strJeu += "|"
        return strJeu
            
            
jeu = JeuDeNim(5)
jeu.run()