#!/bin/bash

"""
Auteur : Cyril PRIGENT

Saisissez plusieurs notes. 

Pour 'quitter' (cesser la prise de notes), veuillez taper q ou une note négative.

Avant la fin du programme, l'ordinateur comptera le nombre des notes saisies et calculera leur moyenne.

Ex : vous tapez 13, 14 et 15. Si vous tapez q ou une note négative, le programme vous calculera la moyenne 14.
"""

somme=0
nbNote=0
note=0

write_a_note()
{
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
	else [ $note -lt 10 ] && [ $note -ge 0 ]
		echo "Insuffisant"
	fi
else
	echo "Valeur incorrecte"
fi
}

while true
do
	write_a_note()

	if [ $note == "q" ] 
	then
		break
	fi

	if [ $note -ge 0 ] && [ $note -le 20 ] 
	then
		somme=$(($somme + $note))
		nbNote=$(($nbNote + 1))
	else
		echo "Nombre invalide"
	fi

	if [ $note -lt 0 ]
	then
		break
	fi
done

if [ $nbNote -ne 0 ]
then
	moyenne=`expr $somme / $nbNote`
	moyenne=$(($somme / $nbNote))
	echo "La moyenne est de $moyenne pour $nbNote notes"
else
	echo "Il y a eu une division par zéro"
fi


