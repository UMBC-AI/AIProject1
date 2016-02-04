# TODO: HEADER


class SearchNode:
    """
    SearchNode
    Basic SearchNode class that implements nodes and links between nodes
    """

    def __init__(self, name: str):
        """
        Constructor
        :param name: Name of the node
        :return:
        """
        self.__links = {}
        self.__linkOrder = []
        self.__name = name

    @property
    def name(self) -> str:
        """
        Returns name of node
        :return: name of the node
        """
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        """
        Sets the name of the node
        :param value: name of the node
        :return: None
        """
        self.__name = value

    @staticmethod
    def cost(start, path) -> float:
        """
        Calculate cost from start following a path
        :param start: Start SearchNode
        :param path: Path consisting a list of SearchNodes, Letters, or a String of letters
        :return: Cost of the path
        """
        cost = 0.0

        if isinstance(path, list):
            # list of strings
            if isinstance(path[0], str):
                curr = start
                for letter in path:
                    cost += curr.weight(letter)
                    curr = getattr(curr, letter)
            # list of nodes
            else:
                curr = start
                for node in path:
                    cost += curr.weight(node.name)
                    curr = node
        # path is a string
        else:
            if '.' in path:
                path = path.split('.')

            curr = start
            for letter in path:
                cost += curr.weight(letter)
                curr = getattr(curr, letter)

        return cost

    def links(self) -> dict:
        """
        Return links list (in no particular order)
        :return: dictionary of nodes
        """
        return self.__links

    def linked_nodes(self) -> list:
        """
        Return all nodes that are linked (in insertion order)
        :return: list of node letters in order
        """
        return self.__linkOrder

    def weight(self, name: str) -> float:
        """
        Get weight to node given
        :param name: Node to get weight to (Only direct links)
        :return: Value of weight
        """
        return self.links().get(name, (None, None))[1]

    def add_link(self, node, weight: float) -> bool:
        """
        Add node link
        :param node: Node to add
        :param weight: Weight to give the link
        :return: boolean for success
        """
        if self.links().get(node.name, None):
            return False

        if weight is None:
            raise ValueError

        # Add it to the dictionary
        self.links()[node.name] = (node, weight)

        # Keep insert order
        self.linked_nodes().append(node.name)
        return True

    def remove_link(self, name: str) -> bool:
        """
        Remove link from name node if possible
        :param name: Name of node to be removed
        :return: boolean if success
        """
        exist = self.__links.pop(name, None)

        if exist:
            self.linked_nodes().remove(name)

        return True

    def __getitem__(self, item: str) -> tuple:
        """
        Get item using [] syntax
        :param item: item to get
        :return: node tuple (node, weight)
        """
        return self.links()[item]

    def __getattr__(self, item: str):
        """
        Get attr using dot syntax, returns next Node
        :param item: item to get
        :return: node
        """
        return self.links()[item][0]

    def __iter__(self) -> str:
        """
        Iterate through list of nodes in insertion order
        :return: yields node letter
        """
        for x in self.linked_nodes():
            yield x

    def __str__(self) -> str:
        return self.name+" children: "+str(self.linked_nodes())