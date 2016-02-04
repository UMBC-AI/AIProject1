# TODO: header
from SearchNode import SearchNode
from typing import List

class SearchQueue:
    """
    SearchQueue for breadth first search
    """
    def __init__(self):
        """
        Implement queue, history (placed_by) and already visited nodes
        :return:
        """
        self.__queue = []
        self.__history = {}
        self.__visited = []

    def push(self, node: SearchNode, placed_by: SearchNode = None) -> bool:
        """
        Push node onto the queue
        :param node:
        :param placed_by:
        :return:
        """
        if node.name in self.__visited:
            return False

        self.__queue.append((node, placed_by))
        self.__visited.append(node.name)
        return True

    def placed_by(self, name: str) -> SearchNode:
        node = self.__history.get(name, None)
        if node is None:
            return None

        return node[1]

    def pop(self) -> SearchNode:
        ret = self.__queue.pop(0)
        self.__history[ret[0].name] = ret

        return ret[0]

    def __len__(self):
        return len(self.__queue)

class SearchAlgo:

    def __len__(self):
        return len(self.__nodes)

    def __node_exist_or_create(self, node):
        if node not in self.__nodes:
            self.__nodes[node] = SearchNode(node)

    def __build_graph(self, lines):
        for line in lines:
            node, link, weight = line.rstrip('\n').split(' ')

            self.__node_exist_or_create(node)
            self.__node_exist_or_create(link)

            self.__nodes[node].add_link(self.__nodes[link], float(weight))

    def __init__(self, data):
        self.__nodes = {}
        self.__build_graph(data)

    def breadth(self, start: str, end: str) -> List[SearchNode]:
        start = self.__nodes[start]
        end = self.__nodes[end]

        queue = SearchQueue()
        queue.push(start, None)

        # Breadth first
        found = None
        while len(queue) > 0:
            node = queue.pop()
            if node.name == end.name:
                found = node
                break

            for link in node.linked_nodes():
                queue.push(node[link][0], node)

        # Build path
        if found:
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
        start = self.__nodes[start]
        end = self.__nodes[end]

        # TODO:

    def uniform(self, start: str, end: str):
        start = self.__nodes[start]
        end = self.__nodes[end]

        # TODO:
