from configparser import ConfigParser


def main(configPath):
    parser = ConfigParser()
    parser.read(configPath)
    targetName = parser.get('init', 'target')

def test():
    print("hello")