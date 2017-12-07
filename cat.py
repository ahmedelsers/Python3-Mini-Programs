#! /usr/bin/env python3

import argparse
import fileinput
from textwrap import dedent

parser = argparse.ArgumentParser(description=dedent("""
                                                    Concatenate FILE(s) to standard output.

                                                    With no FILE, or when FILE is -, read standard input."""),
                                 formatter_class=argparse.RawDescriptionHelpFormatter)

parser.add_argument("-n", "--number", help="number all output lines", action="store_true")
parser.add_argument("-b", "--number-nonblank", help="number nonempty output lines,overrides -n", action="store_true")
parser.add_argument("-E", "--show-ends", help="display $ at end of each line", action="store_true")
parser.add_argument("-T", "--show-tabs", help="display TAB characters as ^I", action="store_true")
parser.add_argument("-v", "--version", help="print version", action="version", version="%(prog)s 0.1")
parser.add_argument("FILE", nargs="*")
args = parser.parse_args()


def simple_cat(args):
    for file in fileinput.input(args.FILE):
        print(file, end="")

def cat_with_args(args):
    # line_number is used to print number only to nonempty lines.
    line_number = 1
    for file in fileinput.input(args.FILE):
        if args.number and not args.number_nonblank:
            if args.show_tabs and not args.show_ends:
                print('    ', fileinput.lineno(), file.replace('\t', '^I'), end="")
            elif args.show_ends and not args.show_tabs:
                if file.endswith('\n'):
                    print('    ', fileinput.lineno(), file.replace('\n', '$'))
            elif args.show_tabs and args.show_ends:
                if file.endswith('\n'):
                    print('    ', fileinput.lineno(), file.replace('\t', '^I').replace('\n', '$'))
            else:
                print('    ', fileinput.lineno(), file, end="")

        elif args.number_nonblank:
            if file.strip():
                if args.show_tabs and not args.show_ends:
                    print('    ', line_number, file.replace('\t', '^I'), end="")
                elif args.show_ends and not args.show_tabs:
                    if file.endswith('\n'):
                        print('    ', line_number, file.replace('\n', '$'))
                elif args.show_tabs and args.show_ends:
                    if file.endswith('\n'):
                        print('    ', line_number, file.replace('\t', '^I').replace('\n', '$'))
                else:
                    print('    ', line_number, file, end="")
                line_number += 1
            else:
                if args.show_tabs and not args.show_ends:
                    print('    ', file.replace('\t', '^I'), end="")
                elif args.show_ends and not args.show_tabs:
                    print('    ', file.replace('\n', '$'), end="")
                elif args.show_tabs and args.show_ends:
                    print('    ', file.replace('\n', '$').replace('\t', '^I'), end="")
                print()
                continue

        elif args.show_tabs and not args.show_ends:
            print('    ', file.replace('\t', '^I'), end="")
        elif args.show_ends and not args.show_tabs:
            print('    ', file.replace('\n', '$'))
        elif args.show_tabs and args.show_ends:
            print('    ', file.replace('\n', '$').replace('\t', '^I'))

try:
    if not (args.number or args.number_nonblank or args.show_ends or args.show_tabs):
        simple_cat(args)
    else:
        cat_with_args(args)
except FileNotFoundError:
    print(fileinput.filename(),":", "No such file or directory")
except IsADirectoryError:
    print(fileinput.filename(),":", "Is a directory")


parser.exit(message="Thank You for using my Script!\n")
