import mysql.connector
from socket import socket
from rdkit import Chem
from rdkit.Chem import AllChem
import os


def molto3D(mol):
    m_3d = Chem.AddHs(mol) 
    AllChem.EmbedMolecule(m_3d,AllChem.ETKDG())
    return m_3d

def pdbWriterFromSdf(file,path):
    suppl = Chem.SDMolSupplier(file)
    for i in suppl:
        if i is None: continue
        cid = i.GetProp('chembl_id')
        mol = molto3d(i)
        AllChem.rdmolfiles.MolToPDBFile(mol, path+cid+".pdb")
        

def pdbWriterFromSmiles(smiles,path):
    for smile in smiles:
        m = Chem.MolFromSmiles(smile[1])
        mol = molto3d(m)
        AllChem.rdmolfiles.MolToPDBFile(mol, path+smile[0]+".pdb")

def pdbToPdbqt(smiles,path):
    for s in smiles:
        os.system("/Library/MGLTools/1.5.6/MGLToolsPckgs/AutoDockTools/Utilities24/prepare_receptor4.py -r "+ smile[0] +".pdb -o "+smile[0]+".pdbqt")