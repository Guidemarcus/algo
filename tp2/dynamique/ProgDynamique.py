from bloque import Bloque
from cell import Cell
import time
import os


solution = []
hauteurSolution = 0


def findBiggerBlock(index, arrayBlocks, currentCell, previousCell):
    temp = None
    for x in range(index):
        # Check if the tour does not already contain the block or if the block if not smaller than the already stacked blocks
        if not previousCell.contains(arrayBlocks[x]) and previousCell.canBeAdded(arrayBlocks[x]):
            if temp is not None and arrayBlocks[x].hauteur > temp.hauteur:
                temp = arrayBlocks[x]
            elif not currentCell.contains(arrayBlocks[x]):
                if temp is not None and arrayBlocks[x].hauteur > temp.hauteur:
                    temp = arrayBlocks[x]
                elif not temp:
                    temp = arrayBlocks[x]
    return temp


def dynamique(arrayBlocks, matrix):
    global solution
    global hauteurSolution
    for j in range(0, len(arrayBlocks)):
        for i in range(0, len(arrayBlocks)):
            if j == 0:
                # Pour la premiere colonne
                matrix[i][j].addBlock(arrayBlocks[i], Cell())
            else:
                biggerBlock = findBiggerBlock(i, arrayBlocks, matrix[i][j], matrix[i][j - 1])
                if biggerBlock is not None:
                    # Add the new bigger block on top of the previous one
                    if matrix[i][j - 1].hauteur > 0:
                        matrix[i][j].addBlock(biggerBlock, matrix[i][j - 1])

    return matrix

def findHighestTower(matrix, size):
    highest = None
    for i in range(0, size):
        for j in range(0, size):
            if highest is None:
                highest = matrix[i][j]
            elif highest.hauteur < matrix[i][j].hauteur:
                highest = matrix[i][j]
    return highest

def afficherBlocUtilise(cell):
    for i in range(0, len(cell.tour)):
        print("[", cell.tour[i].hauteur, ",", cell.tour[i].largeur, ",", cell.tour[i].profondeur, "]")

def afficherTempsExecution(start, end):
    print("Time in milliseconds : ", (end - start) * 1000)


def sortFileBySurface(fileToRead):
    global hauteurSolution
    global solution
    fileBlocks = open("../data/" + fileToRead)
    blocksArray = []
    line = fileBlocks.readline()
    while line:
        blockInfo = line.split()
        newBlock = Bloque(blockInfo)
        blocksArray.append(newBlock)
        line = fileBlocks.readline()

    Matrix = [[Cell() for x in range(len(blocksArray))] for y in range(len(blocksArray))]
    fileBlocks.close()
    blocksArray.sort(key=lambda x: x.surface, reverse=True)
    start = time.time()
    matrix = dynamique(blocksArray, Matrix)
    end = time.time()
    # TODO:: Ajouter la condition pour afficher seulement si -p
    afficherBlocUtilise(findHighestTower(matrix, len(blocksArray)))
    # TODO:: Ajouter la condition pour afficher seulment si -t
    afficherTempsExecution(start, end)

if __name__ == '__main__':
    txtFiles = os.listdir("../data")
    for file in txtFiles:
        sortFileBySurface(file)
