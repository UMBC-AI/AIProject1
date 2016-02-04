# TODO: header
from SearchNode import SearchNode

class SearchAlgo:

    def __node_exist_or_create(self, node):
        if node not in self.__nodes:
            self.__nodes[node] = SearchNode(node)

    def __build_graph(self, lines):
        for line in lines:
            node, link, weight = line.rstrip('\n').split(' ')

            self.__node_exist_or_create(node)
            self.__node_exist_or_create(link)

            self.__nodes[node].add_link(self.__nodes[link], float(weight))

    def __init__(self, file):
        self.__nodes = {}
        with open(file) as data:
            self.__build_graph(data.readlines())

    def breadth(self, start: str, end: str):
        start = self.__nodes[start]
        end = self.__nodes[end]

        # TODO:

    def depth(self, start: str, end: str):
        start = self.__nodes[start]
        end = self.__nodes[end]

        # TODO:

    def uniform(self, start: str, end: str):
        start = self.__nodes[start]
        end = self.__nodes[end]

        # TODO:
