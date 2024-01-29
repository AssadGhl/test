
import random


class Grille:

    def __init__(self,plateau):
        self.plateau=plateau

    def ajouter_nouveau_nombre(self): # cette méthode permet d'ajouter des nombres dans la grille qui sont soit 2 ou 4. 
        nouveau_nombre = random.choice([2, 4])
        self.plateau[random.randint(0,3)][random.randint(0,3)]=nouveau_nombre


    def afficherGrille(self):
        for i in range(len(self.plateau)):
            print("-----------------") 
            for j in range(len(self.plateau[i])):
                print("|",end="   ")
            print("|")
            for j in range(len(self.plateau[i])):
                print("|",self.plateau[i][j],end=" ")
            print("|")
            for j in range(len(self.plateau[i])):
                print("|",end="   ")
            print("|")
        print("-----------------")
    
    
    def initialiser_grille(self): # cette méthode permet d'initialiser la grille du jeu de taille 4x4 afin de faire une nouvelle partie. 
        self.ajouter_nouveau_nombre(self.plateau)
        return self.plateau

    

    

    





