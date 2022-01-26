from typing import Sequence
import sys
import argparse

def error(error: str, error_line: int):
    print(f"{error} | Error on line: {str(error_line)}")
    for i in error:
        print("^", end="")

def parse_args(arg: str) -> bool:
    lower_arg = arg.lower()

    # ILL USE ARG PARSE SOON
    if lower_arg == 'foo':
        return True
    else:
        error(arg, 1)

def main() -> int:
    args_len = len(sys.argv)
    argument_1 = args_len - 1
    if parse_args(sys.argv[int(argument_1)]):
        print("bar")
    return 1

if __name__ == '__main__':
    raise SystemExit(main())