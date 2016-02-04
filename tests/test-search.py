import unittest
from Algorithms import SearchAlgo
from SearchNode import SearchNode


class MySearchAlgos(unittest.TestCase):

    def test_breadth_first_search(self):
        text = "A B 1\nB C 1\nC B 1".split('\n')
        search = SearchAlgo(text)
        path = search.breadth('A', 'C')
        known_path = ['A', 'B', 'C']
        known_cost = 2
        for idx, node in enumerate(path):
            self.assertEquals(node.name, known_path[idx])

        self.assertEquals(SearchNode.cost(path[0], path[1:]), known_cost)

        path = search.breadth('C', 'C')
        self.assertEquals(len(path), 1)
        self.assertEquals(path[0].name, 'C')


if __name__ == '__main__':
    unittest.main()
