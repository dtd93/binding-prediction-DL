from htmd import *
from htmd.molecule import voxeldescriptors as vd

#Descriptors



def get_descriptors(path, ligands, boxSize):
    aux = len(ligands)/100
    cont = aux
    descriptors = []
    labels= np.empty(shape=[0,1])
    print("Bulding descriptors ...")
    contFails = 0
    for i, ligand in enumerate(ligands):
        cont -= 1
        if cont < 0:
            cont = aux
            print(str((i/len(ligands))*100)+"%")
        try:
            mol = Molecule(path + ligand[0] +".pdbqt")
            point = np.squeeze(mol.coords).mean(axis=0)
            desc = vd.getPointDescriptors(mol, point, size=[int(boxSize)]*3)
        except:
            contFails += 1
            print("pdb " + str(ligand[0]) + " not found : " +str(contFails))
            continue
        labels = np.append(labels, ligand[2])
        descriptors.append(desc)
    return np.array(descriptors), labels