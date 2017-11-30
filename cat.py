
import argparse
import fileinput
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
parser.add_argument("FILE", nargs="*")
args = parser.parse_args()