
echo "Bonjour, ceci est un menu." 


Choose_A_User()
{
	echo "Tapez le nom d'un utilisateur :"
	read chosen_User
	# TODO : Trouver le moyen de supprimer le warning.
	return $chosen_User
}


Checking_User()
{
	if id "$1" >/dev/null 2>&1; then
	# https://www.xaprb.com/blog/2006/06/06/what-does-devnull-21-mean/
	#if id "$1"; then
	        echo $1 " user exists"
	else
	        echo $1 " user does not exist"
	fi
}

Checking_IUD()
{
	if id "$1"; then
		echo "IUD trouvé"
		id -u "$1"
	else
		echo "$1" "IUD non trouvé"
	fi
}






while true
do

	echo "1 - pour vérifier l'existence d'un utilisateur"
	echo "2 - pour connaitre l'uid d'un utilisateur"
	echo "q - pour quitter"
	read optionchoisie
	echo $optionchoisie

	if (( $optionchoisie == 1 ))
		then
		Choose_A_User	
		Checking_User $chosen_User
	elif (( $optionchoisie == 2 ))
		then
		Choose_A_User
		Checking_IUD $chosen_User
		#if (( $chosen_User in $USERLIST ))
		# 	cut -d: -f1 /etc/passwd
		# else
		# 	echo "Utilisateur inexistant ou non trouvé, donc pas d'UID..."
	elif (( $optionchoisie == "q" ))
		then
		break
	else
		echo "Choix inexistant"
	fi
done





