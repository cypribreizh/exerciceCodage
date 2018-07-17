
echo "Bonjour, ceci est un menu." 


Choose_A_User()
{
	echo "Tapez le nom d'un utilisateur :"
	read chosen_User
	return $chosen_User
}


Checking_User()
{
	if id "$1" >/dev/null 2>&1; then
	        echo $1 " user exists"
	else
	        echo $1 " user does not exist"
	fi
}

# intégrer une boucle

echo "1 - pour vérifier l'existence d'un utilisateur"
echo "2 - pour connaitre l'uid d'un utilisateur"
echo "q - pour quitter"
read optionchoisie
echo $optionchoisie


if (( $optionchoisie == 1 ))
	then
	Choose_A_User $chosen_User	
	Checking_User $chosen_User
	fi
elif (( $optionchoisie == 2 ))
	then
	# checking_User $chosen_User
	# if (( $chosen_User in $USERLIST ))
	# 	echo `grep $chosen_User /etc/passwd | cut -d: -f3`
	# else
	# 	echo "Utilisateur inexistant ou non trouvé, donc pas d'UID..."
	# fi
elif (( $optionchoisie == "q" ))
	break
	fi
else
	echo "Choix inexistant"
	fi
fi





