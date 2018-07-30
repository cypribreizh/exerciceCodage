# README des exercices BASH

Ce README vous donne les descriptions de l'usage de chacun des exercices.

## exercice0_hello

Un simple "Hello world"


## exercice1_Donner_une_note.sh

Ce programme vous demandera de saisir une note et il l'évaluera en conséquence.

Ex : choisissez 15, le programme vous répondra 'très bien'


## exercice2_Moyenne_de_notes.sh

Saisissez plusieurs notes. 

Pour 'quitter' (cesser la prise de notes), veuillez taper q ou une note négative.

Avant la fin du programme, l'ordinateur comptera le nombre des notes saisies et calculera leur moyenne.

Ex : vous tapez 13, 14 et 15. Si vous tapez q ou une note négative, le programme vous calculera la moyenne 14.


## exercice3_Avec_ou_sans_parametre.sh

Cet exercice est similaire à l'exercice 1 (notation d'élève).

La principale différence est qu'il fonctionne avec ou sans précision de paramètre.


Ex : ./exercice3_Avec_ou_sans_parametre.sh 15    -----> Le programme vous répondra 'Bien'.


Et si vous décidez de ne pas mettre de paramètre :

./exercice3_Avec_ou_sans_parametre.sh		 -----> Le programme vous demandera de saisir 
							 une note avant de répondre.


## exercice4_Creation_menu.sh

Ce programme est un entraînement pour la création d'un menu.
Trois options s'offrent à vous :

	1) Vérifier l'existance d'un utilisateur
	     				   L---------> Le programme vous demande de saisir le nom d'un
						       utilisateur (système) et il vérifie son existence.

	2) Connaître l'IUD d'un utilisateur
	     				   L---------> Saisissez le nom d'un utilisateur système. S'il existe,
						       le programme vous donnera son IUD.
	q) Quitter le menu.

## exercice5_calculatrice.sh

Ce programme fonctionne comme une calculatrice.

Pour fonctionner, il a besoin de deux nombres ($1 et $3) et d'un opérateur $2(+,-,x,/).

Voici quelques exemples :

./exercice5.sh 7 + 4
Le resultat est 11

./exercice5.sh 7 - 4
Le resultat est 3

./exercice5.sh 7 x 4
Le resultat est 28

