# -*- coding: utf-8 -*-

#premiers calculs

print ("Hello, it's me")

calcul1 = 1
calcul2 = 2

print(calcul1 + calcul2)

valeur1 = eval(input("entrez une valeur" ))

valeur2 = eval(input("entrez une valeur" ))

print(valeur1+valeur2)

if valeur1+valeur2 == 100:
    print("code trouvé")
else:
    print("code pas trouvé")

#premiers tuple, liste et dictionnaire

premiertuple = (1, 2, 3, 5, 8, 13, 21, 34)

listedieux = ["Zeus", "Poséidon", "Hadès", "Athéna", "Aphrodite"]

print(listedieux)
athena =listedieux[3]
print(athena)
listedieux.append("Hestia")
print(listedieux)
print(len(listedieux))

bestiaire = {"Zombies" : 257, "Vampires" : 89, "Ghoules" : 167}

print(bestiaire)
bestiaire["Squelettes"]=312
bestiaire["Succubes"]=57
print(bestiaire)

bestiaire["Zombies"]=94
bestiaire["Succubes"]=bestiaire["Succubes"]+7
print(bestiaire)


