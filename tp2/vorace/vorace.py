import os
from bloque import Bloque
from random import randint


candidatNum = 60
solution = []
hauteurSolution = 0


def glouton(candidat):
    i = 0
    global hauteurSolution
    while i < len(candidat):
        if len(solution) == 0:
            solution.append(candidat[0])
            hauteurSolution = hauteurSolution + candidat[0].hauteur
        else:
            #trouver le plus a gauche qui rentre
            if solution[(len(solution)-1)].profondeur > candidat[i].profondeur and solution[(len(solution)-1)].largeur > candidat[i].largeur:
                solution.append(candidat[i])
                hauteurSolution = hauteurSolution + candidat[i].hauteur
            i = i+1


def vorace(fileToRead):
    fileBlocks = open("../data/" + fileToRead)
    blocksArray = []
    line = fileBlocks.readline()
    while line:
        blockInfo = line.split()
        newBlock = Bloque(blockInfo)
        blocksArray.append(newBlock)
        line = fileBlocks.readline()
    fileBlocks.close()
    blocksCandidats = []
    while len(blocksArray) > 0:
        for i in range(0, candidatNum):
            if len(blocksArray) == 0:
                print("")
            else:
                x = randint(0, (len(blocksArray)-1))
                blocksCandidats.append(blocksArray[x])
                del blocksArray[x]
        blocksCandidats.sort(key=lambda x: x.ratio, reverse=False);
        glouton(blocksCandidats)
        blocksCandidats.clear()


if __name__ == '__main__':
    txtFiles = os.listdir("../data")
    for file in txtFiles:
        vorace(file)
        print(hauteurSolution)
        hauteurSolution = 0
        solution.clear()
        break
