import os
from bloque import Bloque
from random import randint
import sys
import time


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
    #fileBlocks = open("../data/" + fileToRead)
    if "-e" in sys.argv:
        fileBlocks = open(sys.argv[sys.argv.index("-e") + 1])
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
        del blocksCandidats[:]

def printSolution():
    global solution
    for x in solution:
        print(x.largeur, x.profondeur, x.hauteur)

if __name__ == '__main__':
    #txtFiles = os.listdir("../data")
    #for file in txtFiles:
    start  = time.time()
    #vorace(file)
    vorace("")
    end = time.time()
    if "-t" in sys.argv:
        print(end - start)
    if "-p" in sys.argv:
        printSolution()
       # print(hauteurSolution)
    hauteurSolution = 0
    del solution[:]
