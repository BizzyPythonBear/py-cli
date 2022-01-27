import sys

def error(error: str, error_line: int, type: str):
    if type == 'str':
        print(f"{error} | Error on line: {str(error_line)} | Not a string", file=sys.stderr)
    elif type == 'int':
        print(f"{error} | Error on line: {str(error_line)} | Not a integer", file=sys.stderr)
    elif type == 'file':
        print(f"{error} | Error on line: {str(error_line)} | File doesn't exist", file=sys.stderr)
    for i in error:
        print("^", end="")