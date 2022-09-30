#Créé par Dev Patel
#Créé le 29 septembre 2022
#Créer un jeu de devinette dans lequel l'usager doit trouver le nombre aléatoire (entre 1 et 100) choisi par l'ordinateur

import random

chaine = print("J'ai choisi un nombre entre 0 et 100. Ton objectif est de le deviner")
essai = None
nombre_mystere = random.randint(1,100)

count = 1
if essai != nombre_mystere:

    essai = input("Entrez votre essaie:")


    if essai == nombre_mystere:
        print("Bravo!")

        print("Ça t'as pris", count, "essaies")

    else:
        print("Réessayer")
        count += 1

