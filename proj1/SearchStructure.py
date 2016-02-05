"""
SearchStructure.py - Search structures for Search algorithms
CMSC 471 - Spring 2016
Author: Christopher Sidell (csidell1@umbc.edu)
ID: JZ28610

Abstract Search structure, queue(FIFO), stack(FILO), and a priority queue
"""
from abc import ABCMeta, abstractmethod
from SearchNode import SearchNode
from typing import List


class SearchStructure:
    """
    Abstract Search data Structure
    """
    __metaclass__ = ABCMeta

    def __init__(self):
        """
        Constructor, creates history, visited, and list structure
        :return:
        """
        self.__history = {}
        self.__visited = []
        self.__structure = []

    @property
    def history(self):
        """
        history variable
        :return:
        """
        return self.__history

    @property
    def visited(self):
        """
        visited variable
        :return:
        """
        return self.__visited

    @property
    def structure(self):
        """
        Data structure
        :return:
        """
        return self.__structure

    def push(self, node: SearchNode, placed_by: SearchNode = None) -> bool:
        """
        Push node onto the structure object (the back)
        :param node: node to push onto structure
        :param placed_by: What pushed it on?
        :return:
        """
        if node.name in self.visited:
            return False

        self.structure.append((node, placed_by))
        self.visited.append(node.name)
        return True

    @abstractmethod
    def pop(self) -> SearchNode:
        """
        Remove item off of structure
        :return:
        """
        pass

    def __len__(self):
        """
        Return length of data structure
        :return:
        """
        return len(self.structure)

    def placed_by(self, name: str) -> SearchNode:
        """
        Find what placed given node name onto the structure
        :param name:
        :return:
        """
        node = self.history.get(name, None)
        if node is None:
            return None

        return node[1]

    def get_path(self, end_node: SearchNode) -> List[SearchNode]:
        """
        Gets the path of the current node to start
        :param end_node: last node in the chain
        :return:
        """
        # Put last node in the list
        path = [end_node]

        # while we have nodes to traverse
        while True:
            # What placed the first node in the list?
            prev = self.placed_by(path[0].name)

            # If node is not None
            if prev:
                # Put that node on the front
                path.insert(0, prev)
            else:
                break

        return path

    def path_cost(self, end_node: SearchNode) -> float:
        """
        Find the path cost given the end node
        (Two traversals of the path)
        :param end_node:
        :return:
        """
        # Find path from last node
        path = self.get_path(end_node)

        if len(path) > 1:
            # Get the cost
            return SearchNode.cost(path[0], path[1:])
        else:
            return 0


class SearchQueue(SearchStructure):
    """
    SearchQueue for breadth first search FIFO
    """

    def __init__(self):
        # Call parent
        super().__init__()

    def pop(self) -> SearchNode:
        """
        Remove node off front of queue
        :return:
        """
        ret = self.structure.pop(0)
        self.history[ret[0].name] = ret

        return ret[0]


class SearchStack(SearchStructure):
    """
    SearchStack for depth first search FILO
    """

    def __init__(self):
        # Call parent
        super().__init__()

    def pop(self) -> SearchNode:
        """
        Remove node off front of queue
        :return:
        """
        ret = self.structure.pop()
        self.history[ret[0].name] = ret

        return ret[0]


class SearchPriorityQueue(SearchStructure):

    def __init__(self):
        # Call parent
        super().__init__()

    def push(self, node: SearchNode, placed_by: SearchNode = None) -> bool:
        """
        Push node onto priority queue
        :param node:
        :param placed_by:
        :return:
        """
        if node.name in self.visited:
            return False

        # Find cost of node we're pushing (TODO: Make less expensive to do this)
        cost = 0.0
        if placed_by:
            pcost = self.path_cost(placed_by)
            wcost = placed_by.weight(node.name)
            cost = pcost + wcost

        # Append to queue
        self.structure.append((node, placed_by, cost))

        # Sort structure on the 3rd item (cost)
        self.structure.sort(key=lambda tup: tup[2])
        return True

    def pop(self) -> SearchNode:
        """
        Pop element off the stack
        :return:
        """
        if len(self.structure) <= 0:
            return None

        ret = self.structure.pop(0)
        if ret[0].name in self.history:
            return self.pop()

        self.history[ret[0].name] = ret
        self.visited.append(ret[0].name)

        return ret[0]
