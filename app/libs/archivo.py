from pathlib import Path
from os.path import exists as file_exists

def encontrar(_file):
    fileName = r"{0}".format(_file)
    fileObj = Path(fileName)
    print(fileObj.is_file())
    return fileObj.is_file()

def existe(_file):
    fileName = r"{0}".format(_file)
    response = file_exists(fileName)
    print(response)
    return response
