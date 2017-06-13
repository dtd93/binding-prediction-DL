from htmd import *
from htmd.molecule import voxeldescriptors as vd

#Descriptors

def get_descriptors(pdbs):
    descriptors=[]
    for pdb in pdbs:
        #Load into Molecule class
        mol = Molecule(pdb)
        
        
        #Center the molecule
        coo = mol.get('coords')
        c = np.mean(coo, axis=0)
        mol.moveBy(-c)
        
        ####Rotate the molecule (?)
        #ligcenter = np.mean(mol.get('coords'),axis=0)
        #M = uniformRandomRotation()
        #mol.rotateBy(M,center=ligcenter)
        
        #Get descriptor for it
        #descriptor = vd.getVoxelDescriptors(mol, usercenters = None, voxelsize = 1, buffer = 8, channels = 0)
        #descriptors.append(descriptor)
    return descriptors