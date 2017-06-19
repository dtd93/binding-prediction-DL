import mysql.connector 
from socket import socket
from rdkit import Chem
import numpy as np
from chemblmining import miner as m
import random


# llamda sql traemos smile con id, 
# cogemos smile de aquella que esten en los ligandos, o de que aquellas que entren por probabilidad y guardamos en un array si hacen biniding o no
# TODO prob hardoceded -> query sql
def getSmiles(ligands):
    allLigands = m.getAllSmiles()
    size = len(ligands)*4
    total = size + len(ligands)
    prob = size/float(len(allLigands))
    w, h = 3, total;
    Matrix = [[0 for x in range(w)] for y in range(h)] 
    print(len(allLigands))
    cont1 = 0
    cont2 = 0
    h = {}
    for l in ligands:
        h[str(l)] = 1
    index = 0
    print(total)
    print(len(h))
    for l in range(len(allLigands)):
        if str(allLigands[l][0]) in h and total > 0:
            Matrix[index] = [allLigands[l][0],allLigands[l][1],1]
            index += 1
            cont1 += 1
            total -= 1
        elif random.uniform(0, 1) <= prob and str(allLigands[l][0]) not in h and total > 0:
            Matrix[index] = [allLigands[l][0],allLigands[l][1],0]
            cont2 += 1
            index += 1
            total -= 1

    print("Final binding:")
    print(cont1)
    print("Final no binding:")
    print(cont2)
    finalSelect = np.array(Matrix)
    return finalSelect


def exportFileData(info, datafolder):
    file = open(datafolder+"aux.data", "w")
    for lig in info:
        file.write(str(lig[0])+" "+str(lig[1])+" "+ str(lig[2]) +"\n")


def loadFromFile(datafolder):
    Matrix = []
    with open(datafolder+"aux.data") as f:
        for line in f:
            values = line.split() 
            Matrix.append()
    finalSelect = np.array(Matrix)
    return finalSelect