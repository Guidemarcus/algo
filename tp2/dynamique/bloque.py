class Bloque:
    profondeur = 0
    largeur = 0
    hauteur = 0
    surface = 0
    ratio = 0

    def __init__(self, info):
        self.hauteur = int(info[2])
        self.largeur = int(info[0])
        self.profondeur = int(info[1])
        self.surface = self.largeur * self.profondeur
        self.ratio = self.surface / self.hauteur

    def getLongueur(self):
        return self.longueur
