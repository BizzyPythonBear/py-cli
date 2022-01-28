import os
from utils.error import error
from utils.size import size_unit

def create_file(file: str) -> int:
    file = open(f"{file}", "w+")
    file.close()
    return 0
def write_file(file: str, text: str) -> int:
    if os.path.exists(file):
        file = open(f"{file}", "w")
        file.write(text)
        file.close()
        return 0
    else:
        error(file, 1, "file")
        return 1

def read_file(file: str) -> int:
    if os.path.exists(file):
        file_o = open(f"{file}", "r")
        file_s = os.stat(str(file))
        size_u = size_unit(file_s.st_size)
        size_s = str(file_s.st_size)

        if size_u == "kb":
            size_s = int(size_s) / 1000

        print(file_o.read())
        print(f"\nFile size: {size_s} {size_u}")

        file_o.close()
        return 0
    else:
        error(file, 1, "file")
        return 1

def remove_file(file: str) -> int:
    if os.path.exists(file):
        os.remove(file)
        return 0
    else:
        error(file, 1, "file")
        return 1