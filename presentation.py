#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 09:40:07 2018

@author: cyril
"""

class personne:
    
    def __init__(self,nom,age,lieuDhabitation,reve,soucis):
        self.nom = nom
        self.age = age
        self.lieuDhabitation = lieuDhabitation
        self.reve = reve
        self.soucis = soucis

    def presentation(self):
        print("Bonjour, je m'appelle " + self.nom + ", j'ai " + self.age + " ans, j'habite à "+ self.lieuDhabitation +". Mon rêve est de " +self.reve + ". Mais j'ai un petit soucis : " + self.soucis)

jeanne = personne(nom = "Jeanne Deschamps", age = "34", lieuDhabitation = "Lille", reve = "fêter mes 20 ans de mariage avec mon chéri... Plus que 8 ans et ce sera le cas", soucis = "j'ai quelques soucis de liquidité... Quelqu'un pourrait-il m'aider à éponger un peu mes dettes ?")
bertrand = personne(nom = "Bertrand Lignou", age = "72", lieuDhabitation = "Toulouse", reve = "vivre une retraite épanouie avec mes petits enfants", soucis = "mes tomates deviennent noires et rabougries... Vous ne connaitriez pas un bon livre qui parle des maladies des plantes, par hasard ?")
julien = personne(nom = "Julien Laveille", age = "27", lieuDhabitation = "Paris", reve = "gravir les échelons de mon entreprise, et obtenir les hautes responsabilités que je mérite", soucis = "je suis en instance de divorce... Je suis à la recherche d'un bon avocat.")
roger = personne(nom = "Roger Monille", age = "42", lieuDhabitation = "Strasbourg", reve = "vivre une vie aussi tranquille que possible", soucis = "je suis cocu pour au moins la quatrième fois... Est-ce que vous connaissez l'adresse d'un bon psychanaliste ?")
juliette = personne(nom = "Juliette Vérone", age = "31", lieuDhabitation = "Ajaccio", reve = "ouvrir un refuge à chat. Je rêve de le faire depuis ma plus tendre enfance...", soucis = "j'aime beaucoup trop les chats ! J'en ai 7 à la maison, et c'est compliqué pour mon budget et mes relations sociales...")



jeanne.presentation()
print()
bertrand.presentation()
print()
julien.presentation()
print()
roger.presentation()
print()
juliette.presentation()

