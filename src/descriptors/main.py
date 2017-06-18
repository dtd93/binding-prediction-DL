from configparser import ConfigParser
from descriptors import descriptor_builder as db


def main(configPath, ligands):
    parser = ConfigParser()
    parser.read(configPath)
    datafolder = parser.get('init', 'datafolder')
    boxSize = parser.get('init', 'boxSize')
    descriptors = db.get_descriptors(datafolder+"aux/", ligands, boxSize)
    return descriptors
    
def test():
    print("hello")