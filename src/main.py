from chemblmining import main as cm 
from configparser import ConfigParser

def main():
    parser = ConfigParser()
    parser.read("config.file")
    configPath = parser.get('init', 'configPath')

    chemblIds = cm.main(configPath)
    
    
if __name__ == "__main__":
    main()