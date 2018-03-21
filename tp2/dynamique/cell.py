from bloque import Bloque

class Cell:
    hauteur = 0
    tour = []

    def __init__(self):
        self.hauteur = 0
        self.tour = []

    def addBlock(self, block):
        self.tour.append(block)
        self.hauteur += block.hauteur

    def contains(self, block):
        for i in self.tour:
            if i.largeur == block.largueur and i.longueur == block.longueur and i.hauteur == block.hauteur:
                return True
        return False
