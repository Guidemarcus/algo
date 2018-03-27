class Bloque:
    profondeur = 0
    largeur = 0
    hauteur = 0
    surface = 0
    ratio = 0

    def __init__(self, info):
        self.hauteur = int(info[0])
        self.largeur = int(info[1])
        self.profondeur = int(info[2])
        self.surface = self.largeur * self.profondeur
        self.ratio = self.surface / self.hauteur

    def getLongueur(self):
        return self.longueur

    # def makeBloque(longueur, largeur, hauteur):
    #    bloc = Bloque()
    ##   bloc.longueur = longueur
    #   bloc.largeur = largeur
    ##  bloc.hauteur = hauteur
    #  print(bloc.longueur)
    #  return bloc
