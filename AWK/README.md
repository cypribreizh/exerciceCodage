# Exercices AWK

Ce repertoire contient les informations sur actuellement 4 exerices AWK.


## Exercice 1 : Bulletin scolaire

Calcul des moyennes de 4 élèves.

`awk -f 01_bulletins.AWK 01_bulletins_data.txt`



## Exercice 2 : Formatage d'une présentation anarchique

Cet exercice est similaire au précédent, mais on ajoute un formatage
des données permettant au tableau d'être interprétable par l'ordinateur.

`awk -f 02_formatage.AWK 02_formatage_data.txt`



## Exercice 3 : Begin et End

Exemple d'utilisation de la notion de BEGIN/END

`awk -f 03_BeginEnd.AWK 03_BeginEnd_data.txt`



## Exercice 4 : Calcul des moyennes et des abscences

Les lignes représentes les données personnelles des 5 étudiants durant
les 6 contrôles.

Par conséquent, les colonnes $3 à $8 représentent les données pour chaque
contrôle.

Le programme comptabilise les absences pour chacun des étudiants. 
Ensuite, il calcule les moyennes (par colonnes) pour les différents contrôles.

`awk -f 04_Moyenne_Abscences.AWK 04_Moyenne_Abscences_data.txt`
