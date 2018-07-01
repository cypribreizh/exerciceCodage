#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 14:46:46 2018

@author: cyril
"""

import tkinter
from tkinter import messagebox

app = tkinter.Tk()

check_widget = tkinter.Checkbutton(app,text = "Publier ?")
check_widget.pack()

"""
Note : 

Un checkbutton représente un choix optionnel.

un checkbutton a comme valeur par défaut 0 (quand il n'est pas coché).
Il a bien sûr par défaut la valeur 1 dans le cas contraire.

Si on a besoin de changer ces valeurs par défaut, on peut écrire (par exemple):

check_widget = tkinter.Checkbutton(app,text = "Publier ?",offvalue = 2, onvalue=5)
"""

radio_widget = tkinter.Radiobutton(app,text = "Homme", value = 3)
radio_widget2 = tkinter.Radiobutton(app,text = "Femme",value = 2)
radio_widget.pack()
radio_widget2.pack()

"""
Contrairement au widget précédent, le radioButton représente un choix obligatoire.
Mais comme on ne peut "pas être homme et femme en même temps" (administrativement
parlant), il faut choisir. Pour cela, il faut leur donner des valeurs différentes.
"""

scale_w = tkinter.Scale(app)
scale_w.pack()

"""
Par défaut, les valeurs sont comprises entre 0 et 100. Si on veut les changer
(par exemple):

scale_w = tkinter.Scale(app,from=20,to=70)

On peut aussi ajouter le "tickinterval" pour graduer votre échelle :

scale_w = tkinter.Scale(app,from_=25,to=75,tickinternal=10)
"""
spin_w = tkinter.Spinbox(app,from_=1,to=10)
spin_w.pack()

"""
Même en mettant des lettres dans une spinbox, on retourne à des valeurs
normales une fois qu'on utilise les flèches.
"""

lb = tkinter.Listbox(app)
lb.insert(1,"Windows")
lb.insert(2,"GNU/Linux")
lb.insert(3,"MacOS")
lb.pack()
"""
C'est une simple liste dans une boîte. On peut sélection 1 élément. (Une option
permet d'en sélectionner plusieurs. On peut aussi se déplacer avec les flèches
du clavier)
"""
#Les fenêtres modales

def show_modal_window():
    messagebox.showerror("ERREUR","Un problème est survenu...")

btn = tkinter.Button(app, text = "Déclencher une erreur", command = show_modal_window)
btn.pack()

"""
Il existe plusieurs types de fenêtres modales, dont voici une liste :
    -showerror
    -showinfo
    -showwarning
    -askquestion
    -askokcancel
    -askyesno
    -askretrycancel
"""

app.mainloop()


