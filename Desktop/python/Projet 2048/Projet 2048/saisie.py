

def saisie_toucheDirection(): # cette fonction permet de connaitre quelle touche du clavier permet d'aller dans une direction à une autre ou quitter la partie. 
    while True:
            touche = input("Appuyez sur une touche (H = haut, B = bas, G = gauche, D = droit, Q = quitter la partie, A = annuler la partie, R = rejouer, S = sauvegarder la partie ) : ")
            if touche != 'H' or touche != 'B' or touche != 'G' or touche != 'D' or touche != 'Q' or touche != 'A' or touche != 'R' or touche != 'S':
                print("Touche non valide. Utilisez 'H', 'B', 'G', 'D', 'Q', 'A', 'R', 'S'.")
            else :
                return touche
def saisie_toucheEtat() :
    while True:
            touche = input("Appuyez sur une touche ( Q = quitter la partie, A = annuler la partie, R = rejouer, S = sauvegarder la partie ) : ")
            if touche != 'H' or touche != 'B' or touche != 'G' or touche != 'D' or touche != 'Q' or touche != 'A' or touche != 'R' or touche != 'S':
                print("Touche non valide. Utilisez 'H', 'B', 'G', 'D', 'Q', 'A', 'R', 'S'.")
            else :
                return touche


def deplacement(direction):
    return True
def rejouer_ou_sauvegarder(): # cette fonction permet au joueur de sauvegarder sa partie ou de rejouer. 
    while True:
        choix = input("Voulez-vous rejouer, R, ou sauvegarder, S, votre score ? ")
        
        if choix == 'r':
            self.initialiser_grille
            print("La grille a été réinitialisé, vous pouvez rejouer.")
            break #l'instruction break permet de quitter une boucle au moment où une condition externe est déclenchée.
        elif choix == 's':
            self.score
            print("Votre score a été auvegarder. ")
            break #l'instruction break permet de quitter une boucle au moment où une condition externe est déclenchée.
        else:
            print("Choix invalide. Veuillez entrer 'R' pour rejouer ou 'S' pour sauvegarder.")

#rejouer_ou_sauvegarder()


def test_fin_de_partie(score_actuel, score_maximal): # cette fonction permet de tester la fin d'une partie. 
    if score_actuel >= score_maximal:
        return True
    else:
        return False


def fusionner_ligne(ligne): #cette fonction permet de fusionner les lignes ensembles afin d'évoluer dans le jeu. 
    nouvelle_ligne = []
    i = 0
    while i < len(ligne):
        if i < len(ligne) - 1 and ligne[i] == ligne[i + 1]:
            nouvelle_valeur = 2 * ligne[i]
            i += 2  
        else:
            nouvelle_valeur = ligne[i]
            i += 1  
        nouvelle_ligne.append(nouvelle_valeur)
    
    nouvelle_ligne += [0] * (len(ligne) - len(nouvelle_ligne))
    return nouvelle_ligne

def deplacer_et_fusionner(grille, direction): #cette fonction permet de fusionner les nombres entre-eux afin d'évoluer dans le jeu. 
    nouvelle_grille = []

    if direction == "gauche":
        for ligne in grille:
            nouvelle_ligne = fusionner_ligne(ligne)
            nouvelle_grille.append(nouvelle_ligne)

    elif direction == "droite":
        for ligne in grille:
            ligne_inverse = list(reversed(ligne)) #la fonction reversed retourne un itérateur sur l'inverse de la séquence de base. 
            nouvelle_ligne = fusionner_ligne(ligne_inverse)
            nouvelle_grille.append(list(reversed(nouvelle_ligne)))

    elif direction == "haut":
        taille = len(grille)
        for j in range(taille):
            colonne = [grille[i][j] for i in range(taille)]
            nouvelle_colonne = fusionner_ligne(colonne)
            for i in range(taille):
                nouvelle_grille[i][j] = nouvelle_colonne[i]

    elif direction == "bas":
        taille = len(grille)
        for j in range(taille):
            colonne = [grille[i][j] for i in range(taille)]

            colonne_inverse = list(reversed(colonne))
            nouvelle_colonne = fusionner_ligne(colonne_inverse)
            for i in range(taille):
                nouvelle_grille[i][j] = list(reversed(nouvelle_colonne))[i]

    return nouvelle_grille