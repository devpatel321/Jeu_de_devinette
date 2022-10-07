#Créé par Dev Patel
#Créé le 29 septembre 2022
#Créer un jeu de devinette dans lequel l'usager doit trouver le nombre aléatoire (entre 1 et 10) choisi par l'ordinateur


from random import *

chaine = print("J'ai choisi un nombre entre 1 et 10. Ton objectif est de le deviner")


def jeu():

    nb_essais = 0


    play_code = True

    while play_code:
        nombre_mystere = randint(1, 10)

        not_found = True
        while not_found:

            essai = int(input("Entrez votre essai:"))

            if essai < nombre_mystere:
                print("Le nombre mystère est plus gros")
                nb_essais += 1

            elif essai > nombre_mystere:
                print("Le nombre mystère est plus petit")
                nb_essais += 1

            elif essai == nombre_mystere:
                print(f"Bravo! Vous avez devinez le numéro en {nb_essais} essaies.")
                restart = input("Si vous voulez rejouer, écrivez (oui). Sinon, écrivez (non)")


                if restart == "oui":
                    play_code = True

                elif restart == "non":
                    play_code = False

                else:
                    play_code = False

jeu()