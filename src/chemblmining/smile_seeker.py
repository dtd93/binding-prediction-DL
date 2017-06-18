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
    prob = size/float(1678393)
    finalSelect = np.empty(shape=[0, 3])
    cont1 = 0
    cont2 = 0
    for l in allLigands:
        if l[0] in ligands:
            finalSelect = np.append(finalSelect, [[l[0],l[1],1]])
            cont1 += 1
        elif random.uniform(0, 1) <= prob and l[0] not in ligands:
            finalSelect = np.append(finalSelect, [[l[0],l[1],0]])
            cont2 += 1
    print("Final binding:")
    print(cont1)
    print("Final no binding:")
    print(cont2)
    return finalSelect 