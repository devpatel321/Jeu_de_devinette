"""
Créé par Dev Patel
Créé le 29 septembre 2022
Créer un jeu de devinette dans lequel l'usager les limites pour le nombre aléatoire
"""

from random import randint


def jeu():
    """
    jeu() correspond à la fonction qui exécute le jeu et permet au joueur d'installer des limites pour le nombre aléatoire
    """

    jeu_commence = True

    while jeu_commence:
        limite_1 = int(input("Entrez la limite pour le plus petit nombre:"))
        limite_2 = int(input("Entrez la limite pour le plus gros nombre:"))

        nombre_mystere = randint(limite_1, limite_2)
        nb_essais = 1

        not_found = True
        while not_found:
            essai = int(input("Entrez votre essai:"))
            if essai < limite_1 or essai > limite_2:
                print("Votre nombre dépasse les limites")
            elif essai < nombre_mystere:
                print("Le nombre mystère est plus gros")
                nb_essais += 1
            elif essai > nombre_mystere:
                print("Le nombre mystère est plus petit")
                nb_essais += 1
            else:
                print(f"Bravo! Vous avez devinez le numéro en {nb_essais} essaies.")
                not_found = False

                restart = input("Si vous voulez rejouer, tapez (o). Sinon, tapez (n)")

                if restart == "o":
                    jeu_commence = True
                elif restart == "n":
                    print("Au revoir!")
                    jeu_commence = False


jeu()
