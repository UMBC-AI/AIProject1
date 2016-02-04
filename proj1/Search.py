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

    input_file = args[0]
    output_file = args[1]
    start = args[2]
    end = args[3]
    search_type = args[4]

    search = None

    with open(input_file) as data:
        search = SearchAlgo(data.readlines())

    print("Graph built with:", len(search), "nodes")

    path = []
    if search_type == 'breadth':
        print("Breadth first search:", start, "->", end)
        path = search.breadth(start, end)
    elif search_type == 'depth':
        path = search.depth(start, end)
    elif search_type == 'uniform':
        path = search.depth(start, end)

    print_path(output_file, path)

main()
