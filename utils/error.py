def error(error: str, error_line: int, type: str):
    if type == 'str':
        print(f"{error} | Error on line: {str(error_line)} | Not a string")
    elif type == 'int':
        print(f"{error} | Error on line: {str(error_line)} | Not a integer")
    for i in error:
        print("^", end="")