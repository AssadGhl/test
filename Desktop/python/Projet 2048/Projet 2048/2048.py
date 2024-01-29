

from grille import *







def afficher_menu():
    print("2048 - Menu Principal")
    print("1. Jouer")
    print("2. Afficher les scores")
    print("3. Afficher les règles")
    print("4. Quitter")


def menu():
    while True:
        print("Menu 2048:")
        print("1. Nouvelle partie")
        print("2. Afficher le meilleur score")
        print("3. Quitter")

        choix = input("Choisissez une option : ")

        if choix == "1":
            initialiser_grille()
        elif choix == "2":
            lire_highscores()
        elif choix == "3":
            print("Merci d'avoir joué ! Au revoir.")
            break
        else:
            print("Choix invalide. Veuillez sélectionner une option valide.")




def jouer():
   
        print("*** Bienvenue au jeu 2048 ***")
        print("Le jeu 2048 est suffisamment célèbre pour ne pas avoir à présenter les règles et le but du jeu")
        print("Rappels des touches de direction :   - H : haut, G : gauche, B : bas, D : droite")
        plateauJeu=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        grille=Grille(plateauJeu)
        grille.ajouter_nouveau_nombre()
        grille.afficherGrille()
        
if __name__ == "__main__":
    jouer()