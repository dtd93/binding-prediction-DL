from htmd import *
from htmd.molecule import voxeldescriptors as vd
from htmd.molecule import util as u
#Descriptors



#TODO make as a function the first loop (getmaxDistance)

def get_descriptors(path, ligands, boxSize):
    batch = len(ligands)/100
    cont = batch
    descriptors = []
    labels= np.empty(shape=[0,1])

    contFails = 0
    maxSize = 0
    if boxSize != "Null":
        maxSize = int(boxSize)

    else:
        print("Calculating box size descriptors ...")
        maxSize = 0
        for i, ligand in enumerate(ligands):
            cont -= 1
            if cont < 0:
                cont = batch
                print(str((i/len(ligands))*100)+"%")
            try:
                mol = Molecule(path + ligand[0] +".pdbqt")
                dist = u.maxDistance(mol, sel='all', origin=[0, 0, 0])
                if maxSize < dist:
                    maxSize = dist
            except:
                continue

    print("Box Size = " + str(maxSize))
    print("Bulding descriptors ...")

    bindingCount = 0
    noBindingCount = 0
    cont = batch
    
    for i, ligand in enumerate(ligands):
        cont -= 1
        if cont < 0:
            cont = batch
            print(str((i/len(ligands))*100)+"%")
        try:
            mol = Molecule(path + ligand[0] +".pdbqt")
            point = np.squeeze(mol.coords).mean(axis=0)
            desc = vd.getPointDescriptors(mol, point, size=[int(maxSize)]*3)
            dist = u.maxDistance(mol, sel='all', origin=[0, 0, 0])
            if dist > int(maxSize):
                continue
        except:
            contFails += 1
            print("pdb " + str(ligand[0]) + " not found : " +str(contFails))
            continue
        
        if ligand[2] == "0":
            noBindingCount += 1
        elif ligand[2] == "1":
            bindingCount += 1
    
        labels = np.append(labels, ligand[2])
        descriptors.append(desc)
    print("Final binding " + str(bindingCount))
    print("Final no binding " + str(noBindingCount))
    return np.array(descriptors), labels, int(maxSize)


    #maxDistance