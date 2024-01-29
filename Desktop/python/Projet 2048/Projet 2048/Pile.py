class Pile:

    def __init__(self):
        self.empiler = []
 
    def push(self, state):
        self.empiler.append(state)
 
    # Cette fonction permet de vider la sauvegarde du dernier jeu.
    def est_vide(self):
        return len(self.empiler) == 0
 
if __name__ == "__main__":
    pile = Pile()
 
    # Cette fonction permet d'empiler les états.
    def empiler(self, element):
        self.elements.append(element)
 
 
    # Cette fonction permet de depiler les états.
    def depiler(self, element):
        if self.est_vide():
            return self.element.pop()
        else: 
            raise IndexError("La pile est vide")
 