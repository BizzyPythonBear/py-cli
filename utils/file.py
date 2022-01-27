import os
from utils.error import error

def create_file(file: str) -> int:
    file = open(f"{file}", "w+")
    file.close()
    return 0

def write_file(file: str, text: str) -> int:
    file = open(f"{file}", "w")
    file.write(text)
    file.close()
    return 0

def read_file(file: str) -> int:
    file = open(f"{file}", "r")
    print(file.read())
    file.close()
    return 0

def remove_file(file: str) -> int:
    if os.path.exists(file):
        os.remove(file)
        return 0
    else:
        error(file, 1, "file")
        return 1