from chemblmining import main as miner 
from cnn import main as cnn 
from descriptors import main as desc 

from configparser import ConfigParser

def main():
    parser = ConfigParser()
    parser.read("config.file")
    configPath = parser.get('init', 'configPath')
    ligands = miner.main(configPath)
    descriptors, labels = desc.main(configPath, ligands)
    cnn.main(configPath, descriptors, labels)

    
if __name__ == "__main__":
    main()