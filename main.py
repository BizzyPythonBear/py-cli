import os
import re
import signal
import sys
from typing import Sequence
import argparse
from utils.output import *


def main() -> int:
    parser = argparse.ArgumentParser(description="Utility testing")
    parser.add_argument('-c', '--cout', type=str, metavar='', help="Output string: COUT")
    parser.add_argument('-i', '--iout', type=str, metavar='', help="Output integer: IOUT")

    args = parser.parse_args()
    if args.cout is not None:
        cout(args.cout)
    elif args.iout is not None:
        iout(args.iout)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
