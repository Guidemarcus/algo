from bloque import Bloque

class Cell:
    hauteur = 0
    tour = []

    def __init__(self):
        self.hauteur = 0
        self.tour = []

    def addBlock(self, block, cell):
        if cell.hauteur > 0:
            if not cell.contains(block):
                for singleBlock in cell.tour:
                    self.tour.append(singleBlock)
                    self.hauteur += singleBlock.hauteur
        indexToAddBlock = self.wereToAddBlock(block)
        if indexToAddBlock == 0 and cell.hauteur == 0:
            self.tour.append(block)
        elif indexToAddBlock == len(cell.tour) + 1:
            self.tour.append(block)
        else:
            self.tour.insert(indexToAddBlock, block)
        self.hauteur += block.hauteur

    def contains(self, block):
        for i in self.tour:
            if i.largeur == block.largeur and i.profondeur == block.profondeur and i.hauteur == block.hauteur:
                return True
        return False

    def canBeAdded(self, block):

        # If we don't have a tour we can add it
        if self.hauteur == 0:
            return True

        for i in range(0, len(self.tour)):
            # If it is the bigger than the first element, we can add it
            if i == 0 and block.largeur > self.tour[i].largeur and block.profondeur > self.tour[i].profondeur:
                return True
            # If it is smaller than the last element, we can add it
            if i == len(self.tour) - 1 and block.largeur < self.tour[i].largeur and block.profondeur < self.tour[i].profondeur:
                return True
            # If it is between two elements, we can add it
            if 1 <= i < len(self.tour) - 1:
                if block.largeur > self.tour[i + 1].largeur and block.profondeur > self.tour[i + 1].profondeur:
                    if block.largeur < self.tour[i].largeur and block.profondeur < self.tour[i].profondeur:
                        return True
        return False

    def wereToAddBlock(self, block):

        # If we don't have a tour we can add it
        if self.hauteur == 0:
            return 0

        for i in range(0, len(self.tour)):
            # If it is the bigger than the first element, we can add it
            if i == 0 and block.largeur > self.tour[i].largeur and block.profondeur > self.tour[i].profondeur:
                return 0
            # If it is smaller than the last element, we can add it
            if i == len(self.tour) - 1 and block.largeur < self.tour[i].largeur and block.profondeur < self.tour[i].profondeur:
                return len(self.tour) + 1
            # If it is between two elements, we can add it
            if 1 <= i < len(self.tour) - 1:
                if block.largeur > self.tour[i + 1].largeur and block.profondeur > self.tour[i + 1].profondeur:
                    if block.largeur < self.tour[i].largeur and block.profondeur < self.tour[i].profondeur:
                        return i + 1
