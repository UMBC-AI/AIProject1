# TODO: HEADER

import sys
from Algorithms import SearchAlgo


def main():
    args = sys.argv[1:]
    if len(args) < 5:
        print("Usage: Search.py <input> <output> <start> <end> <type>")
        return -1

    search = SearchAlgo(args[0])

    search.breadth(args[2], args[3])

main()