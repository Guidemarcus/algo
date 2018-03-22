import os
from bloque import Bloque
from prisonnier import Prisonnier
from solution import Solution
from random import randint
import time



candidatNum = 30
prison = []


def getTourHight(blockSol, candidat, sol):
    hauteurTemp = 0
    for block in sol.tourSolution:
        hauteurTemp += blockSol.hauteur
        if blockSol == block:
            hauteurTemp += candidat.hauteur
            break
    return hauteurTemp


def getFirstBlockComparison(candidats, blockSol, sol):
    return candidats[0].profondeur > blockSol.profondeur and candidats[0].largeur > blockSol.largeur \
                and candidats[0].hauteur > sol.hauteurSolution


def getBlockComparison(candidats, blockSol, sol):
    return candidats[0].profondeur < blockSol.profondeur and candidats[0].largeur < blockSol.largeur \
                and getTourHight(blockSol, candidats[0], sol) > sol.hauteurSolution


def algoTabou(candidats, sol):
    tourModifiee = False
    x = 0
    while x < len(sol.tourSolution):
        #si le block peut aller tout en bas
        if getFirstBlockComparison(candidats, sol.tourSolution[x], sol):
            for blockSol2 in sol.tourSolution:
                prison.append(Prisonnier(blockSol2))
            del sol.tourSolution[:]
            sol.tourSolution.append(candidats[0])
            sol.hauteurSolution = candidats[0].hauteur
            break
        #si les block a venir doivent aller en prison
        if tourModifiee:
            if sol.tourSolution[x] != candidats[0]:
                prison.append(Prisonnier(sol.tourSolution[x]))
                sol.hauteurSolution -= sol.tourSolution[x].hauteur
                sol.tourSolution.remove(sol.tourSolution[x])
                x -= 1
        #si un nouveau block peut etre mis dans le milieu ou au bout de la tour
        elif getBlockComparison(candidats, sol.tourSolution[x], sol):
            tourModifiee = True
            sol.tourSolution.insert(x+1, candidats[0])
            sol.hauteurSolution += candidats[0].hauteur
            x += 1
        x += 1


def convertFileToBlock(fileBlocks):
    blocksArray = []
    line = fileBlocks.readline()
    #lire le fichier
    while line:
        blockInfo = line.split()
        newBlock = Bloque(blockInfo)
        blocksArray.append(newBlock)
        line = fileBlocks.readline()
    fileBlocks.close()
    return blocksArray


def readFileInfo(fileToRead, sol):
    fileBlocks = open("../data/"+fileToRead)
    blocksArray = convertFileToBlock(fileBlocks)

    #initialiser premiere solution
    sol.tourSolution.append(blocksArray[0])
    sol.hauteurSolution = blocksArray[0].hauteur
    del blocksArray[0]

    #preparer le voisinage
    blocksCandidats = []
    iterationModificationTour = 0

    #codition d'arret
    while len(blocksArray) > 0 and iterationModificationTour != 100:
        tempSolution = sol.tourSolution[:]

        #remplir voisinage
        for i in range(0, candidatNum):
            if len(blocksArray) != 0:
                x = randint(0, (len(blocksArray) - 1))
                blocksCandidats.append(blocksArray[x])
                del blocksArray[x]
        blocksCandidats.sort(key=lambda x: x.ratio, reverse=False)

        algoTabou(blocksCandidats, sol)

        #verifier condition d'arret
        if tempSolution == sol.tourSolution:
            iterationModificationTour += 1
        else:
            iterationModificationTour = 0

        #trouver nouveau voisinage
        del blocksCandidats[:]

        #liberer les block en retrait
        for pris in prison:
            if pris.getJour() == 8:
                blocksArray.append(pris.getBlock())
                prison.remove(pris)
            else:
                pris.addJour()


def printSolution(sol):
    for block in sol.tourSolution:
        tempAffichage = "["+block.largeur+","+block.profondeur+","+block.hauteur+"]"
        print(tempAffichage)


if __name__ == '__main__':
    txtFiles = os.listdir("../data")
    sol = Solution()
    for file in txtFiles:
        start = time.time()
        readFileInfo(file, sol)
        end = time.time()
        print(end - start)
        print(sol.hauteurSolution)
        # reinitialiser
        sol.hauteurSolution = 0
        del sol.tourSolution[:]
        del prison[:]

