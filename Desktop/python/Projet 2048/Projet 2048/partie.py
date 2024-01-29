
class Partie:
     
    def _init__(self):
        self.score = 0
        self.historique
        
    # Cette fonction permet de calculer le score du joueur.
    def score(self, grille): 
        score = 0
        for ligne in grille:
            for colonne in ligne:
                if colonne >= 2:
                    score += 2**colonne
        return score

    print("Score actuel :", score)


    # Cette fonction permet de connaitre l'historique des parties du joueur.
    def historique(self, grille):
        self.historique.append(grille)