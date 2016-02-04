# TODO: HEADER

import sys
from Algorithms import SearchAlgo

def print_path(file, path):
    fp = open(file, 'w')
    if len(path) <= 0:
        fp.write('')
    else:
        for node in path:
            fp.write(node.name+'\n')

    fp.close()


def main():
    args = sys.argv[1:]
    if len(args) < 5:
        print("Usage: Search.py <input> <output> <start> <end> <type>")
        return -1

    search = None

    with open(args[0]) as data:
        search = SearchAlgo(data.readlines())

    path = []
    if args[4] == 'breadth':
        path = search.breadth(args[2], args[3])
    elif args[4] == 'depth':
        path = search.depth(args[2], args[3])
    elif args[4] == 'uniform':
        path = search.depth(args[2], args[3])

    print_path(args[1], path)

main()