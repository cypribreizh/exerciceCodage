from tkinter import *

#Exercice 2
#> Ouvrir une fenètre de dimension 800x600
#> Ajouter un champs de texte sur la fenetre
#> Ajouter un bouton sur la fenetre
#> Avoir une variable counter (entier initialisé à 0)
#Lorsque l'on clique sur le bouton, incrémenter counter et l'afficher dnas le champs de texte

Ikea= Tk()          
  

Ikea.geometry("800x600") 

texte=Label(Ikea, text="Venez acheter nos produits suédois")
texte['fg']='black'  
texte.pack() 


counter = 0
str_counter = str(counter)

text_counter = Label(Ikea, text= "counter = " + str_counter)
text_counter['fg']='black'  
text_counter.pack()


def buttonOrder() :
    global counter
    counter += 1
    global text_counter
    text_counter['text'] = "counter = " + str(counter)
    
acne_dAdos = Button(Ikea, text="+ 1 si vous appuyez", command= buttonOrder) 
acne_dAdos.pack() 

Ikea.mainloop() 


