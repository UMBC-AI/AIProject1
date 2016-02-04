# TODO: header
from SearchNode import SearchNode
from typing import List
from SearchStructure import SearchQueue, SearchStack

class SearchAlgo:
    """
    Search Algorithms - CMSC 471 - Proj1
    """
    def __len__(self):
        """
        Size of the graph
        :return:
        """
        return len(self.__nodes)

    def __node_exist_or_create(self, node):
        """
        Create node if it doesn't exist in graph
        :param node: node name
        :return:
        """
        if node not in self.__nodes:
            self.__nodes[node] = SearchNode(node)

    def __build_graph(self, lines):
        """
        Build the graph
        :param lines: lines of data
        :return:
        """
        for line in lines:
            node, link, weight = line.rstrip('\n').split(' ')

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

        # Create queue
        queue = SearchQueue()
        queue.push(start, None)

        found = None
        # While there are nodes in the queue
        while len(queue) > 0:
            # Remove from the top
            node = queue.pop()
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

            # Push nodes onto queue
            for link in nodes:
                queue.push(node[link][0], node)

        # Build path
        if found:
            # Find path from last node
            path = [found]
            while True:
                prev = queue.placed_by(path[0].name)
                if prev:
                    path.insert(0, prev)
                else:
                    break

            return path
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

        stack = SearchStack()

        # TODO:

    def uniform(self, start: str, end: str):
        start = self.__nodes[start]
        end = self.__nodes[end]

        # TODO:
