#! /usr/bin/env python3

import argparse
import fileinput
import sys
from textwrap import dedent

parser = argparse.ArgumentParser(description=dedent("""
                                                    Concatenate FILE(s) to standard output.

                                                    With no FILE, or when FILE is -, read standard input."""),
                                 formatter_class=argparse.RawDescriptionHelpFormatter)

parser.add_argument("-n", "--number", help="number all output lines", action="store_true")
parser.add_argument("-b", "--number-nonblank", help="number nonempty output lines, overrides -n", action="store_true")
parser.add_argument("-E", "--show-ends", help="display $ at end of each line", action="store_true")
parser.add_argument("-T", "--show-tabs", help="display TAB characters as ^I", action="store_true")
parser.add_argument("-v", "--version", help="print version", action="version", version="%(prog)s 0.1")
parser.add_argument("-O", "--outfile", nargs="?", type=argparse.FileType("w"),
                    help="Concatenate to a file", default=sys.stdout)
parser.add_argument("FILE", nargs="*", default=sys.stdin)
args = parser.parse_args()


def number_lines(file):
    try:
        with open(file) as f:
            file_as_list = f.readlines()
            for i in range(len(file_as_list)):
                print('    ', i+1, ' ', file_as_list[i], end='')
    except FileNotFoundError:
        print(file,":", "No such file or directory")



if args.FILE is sys.stdin:
    for file in args.FILE:
        print(file.strip())
else:
    for file in args.FILE:
        try:
            if args.number:
                number_lines(file.strip())
            else:
                with open(file) as f:
                    print(f.read())
        except FileNotFoundError:
            print(file,":", "No such file or directory")
