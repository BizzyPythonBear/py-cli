import os
import re
import signal
import sys
from typing import Sequence
import argparse
from utils.output import *
from utils.file import *

# Py 3.10 Rules!
def main() -> int:
    parser = argparse.ArgumentParser(description="Utility testing")
    parser.add_argument('-c', '--cout', type=str, metavar='', help="Output string: COUT")
    parser.add_argument('-i', '--iout', type=str, metavar='', help="Output integer: IOUT")
    parser.add_argument('-fc', '--filec', type=str, metavar='', help="Create a file")
    parser.add_argument('-fr', '--filer', type=str, metavar='', help="Read a file")
    parser.add_argument('-fw', '--filew', type=str, metavar='', help="Write to a file")
    parser.add_argument('-fd', '--filed', type=str, metavar='', help="Delete a file")

    args = parser.parse_args()
    if args.cout is not None:
        cout(args.cout)
    elif args.iout is not None:
        iout(args.iout)
    elif args.filec is not None:
        create_file(args.filec)
    elif args.filer is not None:
        read_file(args.filer)
    elif args.filew is not None:
        tw = input("t: ")
        if tw is not None:
            write_file(args.filew, str(tw))
        else:
            print("No text inputted, not writing...")
    elif args.filed is not None:
        remove_file(args.filed)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
