import mysql.connector 
from socket import socket
from rdkit import Chem
import numpy as np


def sdfHunter(chemblids,path,datafolder):
    suppl = Chem.SDMolSupplier(path) #coge el sdf múltiple y te da un objeto que contiene objetos mol
    ids = set(chemblids) #Lo he convertido en set para que la búsqueda sucia sea algo más rápida, he mirado a ver si había método más rápido en la documentación de rdkit pero no he encontrado la gran cosa, así que lo he acabado haciendo a lo bruto.
    bindingInfo = np.ones(len(ids))
    for i in suppl:
        if i is None: continue
        cid = i.GetProp('chembl_id') # Te coge el chemblid del mol
        if cid in ids:
            writer = Chem.SDWriter(datafolder+"aux/"+cid+'.sdf') # Te los crea donde estás
            writer.write(i)
    count = 0
    size = len(ids)*4
    prob = size/float(1678393)
    for i in suppl:
        if i is None: continue
        cid = i.GetProp('chembl_id') # Te coge el chemblid del mol
        if random.uniform(0, 1) >= prob:
            writer = Chem.SDWriter(datafolder+cid+"aux/"+'.sdf') # Te los crea donde estás
            writer.write(i)
            count += 1
            ids.add(cid)
    aux = np.zeros(count)
    bindingInfo = np.append(bindingInfo,aux)
    return bindingInfo

