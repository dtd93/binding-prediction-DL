import numpy as np


def getLabels(ligands):
    labels= np.empty(shape=[0,1])
    for ligand in ligands:
        labels = np.append(labels, ligand[2])
    return labels