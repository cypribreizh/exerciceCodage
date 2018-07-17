#!/bin/bash

# permet de faire une calculatrice

# ./exercice5.sh 7 + 4
# $0 $1 $2 $3
# Le resultat est 11
# ./exercice5.sh 7 - 4
# Le resultat est 3
# ./exercice5.sh 7 x 4
# Le resultat est 28


# texte introduction
echo "Bonjour. Ceci est un simulateur de calculatrice. Choisissez deux chiffres, puis un opérande (+,-,x,/) et le programme fera le reste. Evitez tout de même les divisions par zéro..."

# Tester l'opérande ($2)
# en fonction de l'opérande, réaliser le calcul et afficher

echo "paramètres" $0 $1 $2 $3

if [ $2 == "+" ]
then
	echo "addition"
	calcul==$(( $1 + $3 ))
	echo $calcul
	
elif [ $2 == "-" ]
then
	echo "soustraction"
	calcul==$(( $1 - $3 ))
	echo $calcul

elif [ $2 == "x" ]
then
	echo "multiplication"
	calcul==$(( $1 * $3 ))
	echo $calcul
	
elif [ $2 == "/" ]
then
	echo "division"
	calcul==$(( $1 / $3 ))
	echo $calcul
else
	echo "Ceci n'est pas un opérateur"
fi


#La réponse de mon terminal m'est incompréhensible :
#ligne 18: ((: + = +  : erreur de syntaxe : opérande attendue (le symbole erroné est "= + ")
#Déjà, c'est quoi ces symboles bizarres ((: + = +  qui ne se trouvent pas dans mon script ?
#Ensuite, c'est = "+", non "= +" !! (Mais pour mon ordi, c'est du pareil au même...)
#Satané Bash, t'es vraiment sympa !
