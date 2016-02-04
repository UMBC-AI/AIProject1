import unittest
from Algorithms import SearchAlgo
from SearchNode import SearchNode


class MySearchAlgos(unittest.TestCase):

    def test_breadth_first_search(self):
        text = "A B 1\nB C 1\nC B 1".split('\n')
        search = SearchAlgo(text)
        path = search.breadth('A', 'C')
        knownPath = ['A', 'B', 'C']
        knownCost = 2
        for idx, node in enumerate(path):
            self.assertEquals(node.name, knownPath[idx])

        self.assertEquals(SearchNode.cost(path[0], path[1:]), knownCost)

if __name__ == '__main__':
    unittest.main()
