from htmd import *
from htmd.molecule import voxeldescriptors as vd

#Descriptors

def get_descriptors(path, ligands, boxSize):
    descriptors= np.empty(shape=[0,1])
    for ligand in ligands:
        #Load into Molecule class
        mol = Molecule(path + ligands[0] +".pdbqt")
        point = np.squeeze(mol.coords).mean(axis=0)
        desc = vd.getPointDescriptors(mol, point, size=[boxSize]*3)
        descriptors = np.append(descriptors, desc)
    return descriptors