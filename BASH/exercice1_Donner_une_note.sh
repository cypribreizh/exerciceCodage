#!/bin/bash

"""
Auteur : Cyril PRIGENT

Ce programme vous demandera de saisir une note et il l'évaluera en conséquence.

Ex : choisissez 15, le programme vous répondra 'très bien'
"""

echo "Veuillez écrire une note entre 0 et 20"
read note
echo $note

if [ $note -le 20 ] && [ $note -ge 0 ]
then
	if [ $note -le 20 ] && [ $note -ge 16 ]
	then
		echo "Très bien"

	elif [ $note -lt 16 ] && [ $note -ge 14 ]
	then
		echo "Bien"

	elif [ $note -lt 14 ] && [ $note -ge 12 ]
	then
		echo "Assez bien"

	elif [ $note -lt 12 ] && [ $note -ge 10 ]
	then
		echo "Passable"

	else	
		echo "Insuffisant"
	fi		
else
	echo "Valeur incorrecte"
fi