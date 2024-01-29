

def lire_highscores():
   highscores = []  # Créer une liste vide pour stocker les scores

   with open(" highscores.txt ", " r ") as fichier:
       for ligne in fichier:
           nom, score = ligne.strip().split( " , ")  # Diviser chaque ligne en nom et score
           highscores.append((nom, int(score)))  # Ajouter le tuple (nom, score) à la liste

   return highscores

# Tri à bulles pour trier les scores en ordre décroissant
def trier_scores(scores):
   n = len(scores)
   for i in range(n - 1):
       for j in range(0, n - i - 1):
           if scores[j][1] < scores[j + 1][1]:
               scores[j], scores[j + 1] = scores[j + 1], scores[j]

# Appeler les fonction pour les scores 
if __name__ == " __main__ ":
   scores = lire_highscores()
   trier_scores(scores)

   # Afficher les dix meilleurs scores
   for i, (nom, score) in enumerate(scores[:10]):
       print ("f") ;  {i + 1},  {nom}: {score}