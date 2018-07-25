
from tkinter import *  
 
maFenetre= Tk()           # vous pouvez choisir le nom que vous voulez pour votre fenêtre
maFenetre.mainloop()     # lance la boucle principale

monBouton = Button(Fenetre, text="quitter", command=Fenetre.destroy) # Bouton qui détruit la fenêtre
monBouton.pack()        # insère le bouton dans la fenêtre
maFenetre.mainloop()       # lance la boucle principale

# Le fameux "Hello wolrd"

Fenetre=Tk()
texte=Label(Fenetre, text="Hello World")
texte['fg']='black'  # Création du texte "Hello World" de couleur noire
texte.pack() # Insère le texte dans la fenêtre
Fenetre.mainloop()

# Création d'une entrée

Fenetre1 = Tk() 
Entree = Entry(Fenetre1)     # On définit l'objet Entry qui porte le nom Entree
Entree.pack()               # On place "Entree"
Fenetre1.mainloop()          # On lance la boucle du programme

#def repondre():
# affichage['text'] = reponse.get()	# lecture du contenu du widget "reponse"

#Fenetre = Tk()
#Fenetre.title('Mon nom')

#nom = Label(Fenetre, text = 'Votre nom :')
#reponse = Entry(Fenetre)
#valeur = Button(Fenetre, text =' Valider', command=repondre)
#affichage = Label(Fenetre, width=30)
#votre_nom=Label(Fenetre, text='Votre nom est :')
#nom.pack()
#reponse.pack()
#valeur.pack()
#votre_nom.pack()
#affichage.pack()

#Fenetre.mainloop()

#Création d'un canevas

racine= Tk()

zone_dessin = Canvas(racine, width=500, height=500) #Définit les dimensions du canevas
zone_dessin.pack() 					#Affiche le canevas
zone_dessin.create_line(0,0,500,500) 			#Dessine une ligne en diagonale
zone_dessin.create_rectangle(100,100,200,200) 		#dessine un rectangle

bouton_sortir = Button(racine,text="Sortir",command=racine.destroy)
bouton_sortir.pack()

racine.mainloop()

