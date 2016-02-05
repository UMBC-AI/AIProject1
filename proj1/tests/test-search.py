import unittest
from Algorithms import SearchAlgo
from SearchNode import SearchNode


class MySearchAlgos(unittest.TestCase):

    def test_breadth_first_search(self):
        print('Test breadth')
        text = 'A B 1\nB C 1\nC B 1'.split('\n')
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

    def test_depth_first_search(self):
        print('Test depth')
        text = 'A B 1\nA D 1\nB C 1\nD C 1'.split('\n')
        search = SearchAlgo(text)
        path = search.depth('A', 'C')
        known_path = ['A', 'D', 'C']
        known_cost = 2

        for idx, node in enumerate(path):
            self.assertEquals(node.name, known_path[idx])

        self.assertEquals(SearchNode.cost(path[0], path[1:]), known_cost)

        path = search.breadth('C', 'C')
        self.assertEquals(len(path), 1)
        self.assertEquals(path[0].name, 'C')

    def test_uniform_search(self):
        print('Test uniform')
        cases = [
            'A B 20\nA D 1\nB C 1\nD C 1'.split('\n'),
            'A B 1\nA D 20\nB C 1\nD C 1'.split('\n')
        ]
        known_path = [
            ['A', 'D', 'C'],
            ['A', 'B', 'C'],
        ]

        for cidx, case in enumerate(cases):
            search = SearchAlgo(case)
            path = search.uniform('A', 'C')

            for idx, node in enumerate(path):
                self.assertEquals(node.name, known_path[cidx][idx])

        path = search.uniform('C', 'C')
        self.assertEquals(len(path), 1)
        self.assertEquals(path[0].name, 'C')


if __name__ == '__main__':
    unittest.main()
