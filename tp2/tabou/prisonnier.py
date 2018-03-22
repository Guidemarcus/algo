class Prisonnier:


    def __init__(self, block):
        self.blockPrisonnier = block
        self.jourEnDedans = 0


    def addJour(self):
        self.jourEnDedans += 1


    def getJour(self):
        return self.jourEnDedans


    def getBlock(self):
        return self.blockPrisonnier
