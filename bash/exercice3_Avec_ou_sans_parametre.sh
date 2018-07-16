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

# Ne tenez pas trop compte des commentaires ci-dessous (quand je débutais sur Bash, cet exercice m'a fait voir de toutes les couleurs).


# Satané "opérateur unaire attendu". Sans lui, la méthode "classique" marche, mais en voulant remplacer les -lt et les -ge
# par des < et des >=, ça a empiré la situation ! Fluuuuuute !! (pour ne pas dire autre chose)
# Vraiment Bash, tu sais être génial, tu sais...
#(Tout le monde a le droit de "péter un cable" à un moment ou à un autre...)

