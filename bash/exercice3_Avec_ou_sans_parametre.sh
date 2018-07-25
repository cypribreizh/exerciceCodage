#!/bin/bash

"""
Cet exercice marche avec ou sans paramètre.
(si vous ne mettez pas une note comme premier paramètre, le programme vous demandera une saisie)
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



