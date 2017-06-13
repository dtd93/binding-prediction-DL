from chemblmining import miner as m
from chemblmining import sdf_cuter as sc
from chemblmining import smile_seeker as ss
rom chemblmining import mol_converter as mc
from configparser import ConfigParser


def main(configPath):
    parser = ConfigParser()
    parser.read(configPath)
    targetId = parser.get('init', 'target')
    sdfFilePath = parser.get('init', 'sdfFilePath')
    datafolder = parser.get('init', 'datafolder')
    mysqlPass = parser.get('init', 'mysqlPass')
    ligands = m.getLigandsCMolregno(targetId,mysqlPass)
    allInfo = ss.getSmiles(ligands)
    mc.pdbWriterFromSmiles(allInfo,datafolder+aux/)
    return allInfo
    
def test():
    print("hello")