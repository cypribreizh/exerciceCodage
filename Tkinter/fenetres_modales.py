#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 08:30:08 2018

@author: cyril
"""
import tkinter
from tkinter import messagebox

app = tkinter.Tk()


def show_error_message():
    messagebox.showerror("ERREUR","Une division par zéro !? Arrêtez ça tout de suite, pauvre fou !")

btn1 = tkinter.Button(app, text = "Déclencher une erreur", command = show_error_message)
btn1.pack()

def show_info():
    messagebox.showinfo("Localisation GPS","Vous êtes actuellement dans le XVIème arrondissement, plus précisément dans le bois de Boulogne...")

btn2 = tkinter.Button(app, text = "SOS GPS", command = show_info)
btn2.pack()

def show_warning():
    messagebox.showinfo("ALERTE ROUGE !!","Vous circulez à vitesse lumière !! Vous risquez de vous crasher contre un astéroïde, une planète ou un autre vaisseau...")

btn3 = tkinter.Button(app, text = "ALERTE !", command = show_warning)
btn3.pack()

def ask_question():
    messagebox.askquestion("Enigme","Dieu existe-t-il ?")

btn3 = tkinter.Button(app, text = "Question qui hante l'Homme depuis plus de 3000 ans", command = ask_question)
btn3.pack()

def ok_or_cancel():
    messagebox.askokcancel("De la part de Google","Voulez-vous vraiment imprimer l'intégralité de Wikipédia ?")

btn4 = tkinter.Button(app, text = "On risque d'avoir un petit problème...", command = ok_or_cancel)
btn4.pack()

def yes_or_no():
    messagebox.askyesno("Follow me... For Chaos !!","Do you want to sleep with me ? \nLike you see, i'm a magnificent and sultry Daemonette... \nI'm devoted to the dark Lord Slaanesh. \nJoin me... Come on ! Where I live, there are thousands of pretty chicks like me... \nThey're so beautiful you will cry ! They gonna make you mad, for sure...")

btn5 = tkinter.Button(app, text = "Temptation from 40k", command = yes_or_no)
btn5.pack()

def retry_or_not():
    messagebox.askretrycancel("Encore derrière les barreaux !","C'est au moins la 3ème fois que vous êtes en prison pour avoir voulu créer une armée de robots mutants... \nVoulez-vous essayer de vous évader et retempter de conquérir le monde ? \n\nAllez, la prochaine fois sera la bonne...")

btn6 = tkinter.Button(app, text = "Oh Flûte...", command = retry_or_not)
btn6.pack()

app.mainloop()
