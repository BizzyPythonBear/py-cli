import typing

def error(error: str, error_line: int):
    print(f"{error} | Error on line {str(error_line)}")
    s = []
    for i in error:
        print("^", end ="")
