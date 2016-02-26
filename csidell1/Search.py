"""
Search.py - Main Search Driver
CMSC 471 - Spring 2016
Author: Christopher Sidell (csidell1@umbc.edu)
ID: JZ28610

Search.py is the driver for proj1
PYTHON VERSION: 3.5.1

Usage: Search.py <input_file> <output_file> <start_node> <end_node> <search_type>
"""
import sys
import os
from Algorithms import SearchAlgo
from SearchNode import SearchNode
from typing import List


def print_path(file, path: List[SearchNode]):
    """
    Writes the path to a file
    :param file: filepath
    :param path: list of nodes
    :return:
    """
    fp = open(file, 'w')
    if len(path) <= 0:
        fp.write('')
    else:
        for node in path:
            fp.write(node.name+'\n')

    fp.close()


def main():
    """
    Main function, starts all the stuff
    :return:
    """

    # Figure if the arguments are good
    args = sys.argv[1:]
    if len(args) < 5:
        print('Usage: Search.py <input> <output> <start> <end> <type>')
        return -1

    input_file = args[0]
    output_file = args[1]
    start = args[2]
    end = args[3]
    search_type = args[4]

    # Check args
    if not isinstance(input_file, str) or not isinstance(output_file, str):
        print('One of your files are not strings')
        return -1

    # Check if input exists
    if not os.path.exists(input_file):
        print('Input file does not exist!')
        return -1

    # Generate the graph
    search = None
    with open(input_file) as data:
        search = SearchAlgo(data.readlines())
        print('Graph built with:', len(search), 'nodes')

    # See if nodes we're searching for are in the graph
    if not search.node_exists(start) or not search.node_exists(end):
        print('One of the given nodes were not in the graph!')
        return -1

    # Start searching
    path = []
    if search_type == 'breadth':
        print('Breadth first search:', start, '->', end)
        path = search.breadth(start, end)
    elif search_type == 'depth':
        print('Depth first search:', start, '->', end)
        path = search.depth(start, end)
    elif search_type == 'uniform':
        print('Uniform first search:', start, '->', end)
        path = search.uniform(start, end)

    # Print it out to the file
    if path:
        print_path(output_file, path)
    else:
        print_path(output_file, [])
        print('No path returned')

main()
