from bloque import Bloque
from cell import Cell
import os


solution = []
hauteurSolution = 0


def findBiggerBlock(index, arrayBlocks, currentCell):
    temp = None
    for x in range(index):
        if arrayBlocks[index].profondeur < arrayBlocks[x].profondeur and arrayBlocks[index].largeur < arrayBlocks[x].largeur:
            if temp is not None and arrayBlocks[x].hauteur > temp.hauteur and not currentCell.contains(arrayBlocks[x]):
                temp = arrayBlocks[x]
            else:
                temp = arrayBlocks[x]
    return temp


def dynamique(arrayBlocks, matrix):
    global solution
    global hauteurSolution
    for j in range(0, len(arrayBlocks)):
        for i in range(0, len(arrayBlocks)):
            if j == 0:
                matrix[i][j].addBlock(arrayBlocks[i])
            else:
                biggerBlock = findBiggerBlock(i, arrayBlocks, matrix[i][j])



def sortFileBySurface(fileToRead):
    global hauteurSolution
    global solution
    fileBlocks = open("test")
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
    dynamique(blocksArray, Matrix)


if __name__ == '__main__':
    txtFiles = os.listdir("../data")
    for file in txtFiles:
        sortFileBySurface(file)
