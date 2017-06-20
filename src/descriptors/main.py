from configparser import ConfigParser
from descriptors import descriptor_builder as db


def main(configPath, ligands):
    parser = ConfigParser()
    parser.read(configPath)
    datafolder = parser.get('init', 'datafolder')
    boxSize = parser.get('init', 'boxSize')
    descriptors, labels, maxSize  = db.get_descriptors(datafolder+"auxQT/", ligands, boxSize)
    return descriptors, labels, maxSize

    
def test():
    print("hello")