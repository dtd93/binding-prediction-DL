from cnn import network as net
from cnn import dataPreparer as dp
from configparser import ConfigParser

def main(configPath, ligands, descriptors, labels):
    parser = ConfigParser()
    parser.read(configPath)
    datafolder = parser.get('init', 'datafolder')
    boxSize = int(parser.get('init', 'boxSize'))
    kernelSize = int(parser.get('init', 'kernelSize'))
    nClases = int(parser.get('init', 'nClases'))
    nEpoch = int(parser.get('init', 'nEpoch'))
    batchSize =int( parser.get('init', 'batchSize'))
    nFilters = int(parser.get('init', 'nFilters'))
    net.runCNN(boxSize, nFilters, kernelSize, nClases, nEpoch, batchSize, descriptors, labels)
    return
    
def test():
    print("hello")