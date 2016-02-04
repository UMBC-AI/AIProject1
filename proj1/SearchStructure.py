from abc import ABCMeta, abstractmethod
from SearchNode import SearchNode


class SearchStructure:
    """
    Abstract Search data Structure
    """
    __metaclass__ = ABCMeta

    def __init__(self):
        """
        Constructor
        :return:
        """
        self.__history = {}
        self.__visited = []

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

    @abstractmethod
    def push(self, node: SearchNode, placed_by: SearchNode = None) -> bool:
        """
        Abstract push function
        :param node: node to push onto structure
        :param placed_by: What pushed it on?
        :return:
        """
        pass

    @abstractmethod
    def pop(self) -> SearchNode:
        """
        Remove item off of structure
        :return:
        """
        pass

    @abstractmethod
    def __len__(self):
        """
        Return length of data structure
        :return:
        """
        return None

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

class SearchQueue(SearchStructure):
    """
    SearchQueue for breadth first search
    """
    def __init__(self):
        """
        Implement queue, history (placed_by) and already visited nodes
        :return:
        """
        self.__queue = []
        super().__init__()

    def push(self, node: SearchNode, placed_by: SearchNode = None) -> bool:
        """
        Push node onto the queue
        :param node:
        :param placed_by:
        :return:
        """
        if node.name in self.visited:
            return False

        self.__queue.append((node, placed_by))
        self.visited.append(node.name)
        return True

    def pop(self) -> SearchNode:
        """
        Remove node off front of queue
        :return:
        """
        ret = self.__queue.pop(0)
        self.history[ret[0].name] = ret

        return ret[0]

    def __len__(self):
        """
        Length of queue
        :return:
        """
        return len(self.__queue)

class SearchStack(SearchStructure):

    def __init__(self):
        self.__stack = []
        super().__init__()

