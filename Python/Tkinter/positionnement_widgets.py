#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 13:55:11 2018

@author: cyril
"""
import tkinter

# Création et paramétrage de la fenêtre

app = tkinter.Tk()
app.geometry("640x480")
app.title("Positionnement des widgets")

# Widgets

"""
Le rôle du widget Frame est de contenir d'autres widgets
"""

mon_mainframe = tkinter.Frame(app, width=300, height=200, borderwidth=1)
mon_mainframe.pack()

"""
Il existe aussi la variante Labelframe : on doit dans ce cas là ajouter un
titre après le widget parent.

Ex : mon_mainframe = tkinter.LabelFrame(app, texte="1er Frame titré", width=300, height=200, borderwidth=1

L'avantage du LabelFrame est d'avoir des limites bien visibles.                                       

Maintenant, nous devons remplir notre Frame avec d'autres widgets.
"""
ent = tkinter.Entry(mon_mainframe)
lab = tkinter.Label(mon_mainframe,text="un label")
btn = tkinter.Button(mon_mainframe,text="Bienvenue")
lab.pack()
btn.pack()
ent.pack()

"""
Note : pour un (Label)Frame, le dimensionnement est optionnel. Dans ce cas,
l'ordi se contempte de simplement contenir les widgets en question dans le
plus petit rectangle possible.
"""

"""
Evoquons maintenant les positionnements...

La méthode pack() permet de positionner des éléments de haut en bas, selon
l'ordre des appels (voir plus haut).

Note : pack() équivaut à pack(side="top") (c'est donc sa valeur par défaut). 
       ce qui implique que l'argument side peut valoir "bottom", "left" ou "right".
 
Note 2 : .pack(extend=1) veut dire "Tu met au milieu de tout le reste".
         Faites attention car extend et side sont des options qui par
         nature se contre-disent (inutile de mettre ces 2 options dans
         un même pack)
"""

# Boucle principale

app.mainloop()

#Reprendre à la 14ème minute