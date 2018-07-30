#!/bin/bash

"""
Auteur : Cyril PRIGENT

Cet exercice est similaire à l'exercice 1 (notation d'élève).

La principale différence est qu'il fonctionne avec ou sans précision de paramètre.

Ex : ./exercice3_Avec_ou_sans_parametre.sh 15    -----> Le programme vous répondra 'Bien'.

Et si vous décidez de ne pas mettre de paramètre :

./exercice3_Avec_ou_sans_parametre.sh		 -----> Le programme vous demandera de saisir 
							une note avant de répondre.

"""

Appreciation ()
{
if (( $1 <= 20 )) && (( $1 >= 16 ))
then
	echo "Très bien"
elif (( $1 < 16 )) && (( $1 >= 14 ))
then
	echo "Bien"
elif (( $1 < 14 )) && (( $1 >= 12 ))
then
	echo "Assez bien"
elif (( $1 < 12 )) && (( $1 >= 10 ))
then
	echo "Passable"
elif (( $1 < 10 )) && (( $1 >= 0 ))
then
	echo "Insuffisant"
else
	echo "Valeur incorrecte"
fi
}

if [ $# -eq 1 ]
then
	Appreciation $1
else
	echo "Veuillez écrire une note entre 0 et 20"
read note
Appreciation $note
fi



