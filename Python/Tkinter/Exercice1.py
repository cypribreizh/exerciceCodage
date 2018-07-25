import tkinter
from tkinter import * 

fenetre_Exo1= Tk()           


#Consigne

#Ouvrir une fenetre de dimension 500x500. Dessiner un carré rouge de 5px*5px en position (100, 100). Dessiner un cercle bleu de 20px*20px en position (200, 200)

zone_dessin = Canvas(fenetre_Exo1, width=500, height=500) 
zone_dessin.pack() 
zone_dessin.create_rectangle(100,100,300,200,fill='red',width=1) 
zone_dessin.create_oval(200,200,220,220,fill='blue',width=1) 

fenetre_Exo1.mainloop() 

