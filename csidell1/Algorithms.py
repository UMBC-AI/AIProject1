"""
Algorithms.py - Search algorithms
CMSC 471 - Spring 2016
Author: Christopher Sidell (csidell1@umbc.edu)
ID: JZ28610

Algorithms holds the methods for carrying out breadth, depth, and uniform searches
"""
from SearchNode import SearchNode
from typing import List
from SearchStructure import SearchQueue, SearchStack, SearchPriorityQueue, SearchStructure


class SearchAlgo:
    """
    Search Algorithms - CMSC 471 - Proj1
    """

    def __len__(self) -> int:
        """
        Size of the graph
        :return:
        """
        return len(self.__nodes)

    def node_exists(self, node: str) -> bool:
        """
        Checks if node is in graph
        :param node: node name
        :return:
        """
        return node in self.__nodes

    def __node_exist_or_create(self, node: str) -> None:
        """
        Create node if it doesn't exist in graph
        :param node: node name
        :return:
        """
        if node not in self.__nodes:
            self.__nodes[node] = SearchNode(node)

    def __build_graph(self, lines: List[str]) -> None:
        """
        Build the graph
        :param lines: lines of data
        :return:
        """
        for line in lines:
            node, link, weight = line.rstrip('\n').split(' ')

            # Make sure node and linked node are in the graph
            self.__node_exist_or_create(node)
            self.__node_exist_or_create(link)

            self.__nodes[node].add_link(self.__nodes[link], float(weight))

    def __init__(self, data):
        """
        Constructor that builds the graph out
        :param data:
        :return:
        """
        self.__nodes = {}
        self.__build_graph(data)

    @staticmethod
    def basic_search(structure: SearchStructure, start: SearchNode, end: SearchNode) -> SearchNode:
        """
        Basic search that untilizes data structure
        :param structure: SearchStructure data structure
        :param start: start name node
        :param end: end name node
        :return:
        """
        # Push start onto the data structure
        structure.push(start, None)

        found = None
        # While there are nodes in the queue
        while len(structure) > 0:
            # Remove from the top
            node = structure.pop()

            # Is it the goal?
            if node.name == end.name:
                found = node
                break

            # Get all nodes linked to this node
            nodes = []
            for link in node.linked_nodes():
                nodes.append(link)

            # Make sure it's alphabetical
            nodes.sort()

            # Push nodes onto structure
            for link in nodes:
                structure.push(node[link][0], node)

        return found

    def breadth(self, start: str, end: str) -> List[SearchNode]:
        """
        Breadth First Search
        :param start: Start node name
        :param end: End node name
        :return:
        """
        # Get start and end node
        start = self.__nodes[start]
        end = self.__nodes[end]

        # Create search queue
        queue = SearchQueue()

        # Do a basic search using a queue
        node = SearchAlgo.basic_search(queue, start, end)

        # Build path
        if node:
            # Find path from last node
            return queue.get_path(node)
        else:
            return []

    def depth(self, start: str, end: str):
        """
        Depth first node
        :param start: node name
        :param end: node name
        :return:
        """
        start = self.__nodes[start]
        end = self.__nodes[end]

        # Create search stack
        stack = SearchStack()

        # Do a basic search using a stack
        node = SearchAlgo.basic_search(stack, start, end)

        # Build path
        if node:
            # Find path from last node
            return stack.get_path(node)
        else:
            return []

    def uniform(self, start: str, end: str):
        """
        Uniform search
        :param start: node name
        :param end: node name
        :return:
        """
        start = self.__nodes[start]
        end = self.__nodes[end]

        # Create priority queue
        pqueue = SearchPriorityQueue()

        # Do a basic search using priority queue
        node = SearchAlgo.basic_search(pqueue, start, end)

        # Build path
        if node:
            path = pqueue.get_path(node)
            # Find path from last node
            return path
        else:
            return []
