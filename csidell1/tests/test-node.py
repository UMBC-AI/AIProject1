import unittest
from copy import copy

import SearchNode

class TestSearchNode(unittest.TestCase):
    def test_node_name(self):
        node = SearchNode.SearchNode('A')
        self.assertEquals(node.name, 'A', 'name does not match')
        self.assertNotEquals(node.name, 'B', 'name matches B')

    def test_node_add(self):
        A = SearchNode.SearchNode('A')
        B = SearchNode.SearchNode('B')

        # Doesn't already exist
        self.assertNotIn('B', A.linked_nodes(), 'node should not exist')
        result = A.add_link(B, 1)

        # Should be added
        self.assertTrue(result, 'function says not added')
        self.assertIn('B', A.linked_nodes(), 'should be added')

        # Cannot add result
        result = A.add_link(B, 2)
        self.assertFalse(result, 'should not be able to add twice')

    def test_node_remove(self):
        A = SearchNode.SearchNode('A')
        B = SearchNode.SearchNode('B')

        result = A.add_link(B, 1)
        result = A.remove_link('B')
        self.assertTrue(result, 'function says removed failed')
        self.assertNotIn('B', A.linked_nodes(), 'node was not removed')

    def test_node_weight(self):
        A = SearchNode.SearchNode('A')
        B = SearchNode.SearchNode('B')

        weight = A.weight('B')
        self.assertEquals(weight, None, 'weight exists before initialized')

        A.add_link(B, 1)
        weight = A.weight('B')

        self.assertEquals(weight, 1, 'weight is not correct')

    def test_node_list(self):
        A = SearchNode.SearchNode('A')
        B = SearchNode.SearchNode('B')
        C = SearchNode.SearchNode('C')

        A.add_link(B, 1)
        A.add_link(C, 1)

        self.assertIn('B', A.linked_nodes())
        self.assertIn('C', A.linked_nodes())

        nodes = ['B', 'C']
        nodeOrder = copy(nodes)

        for idx, node in enumerate(A):
            self.assertEquals(nodeOrder[idx], node, 'nodes out of order of entry!')
            nodes.remove(node)

        self.assertEquals(len(nodes), 0, 'not all nodes were found')

    def test_node_getlist(self):
        A = SearchNode.SearchNode('A')
        B = SearchNode.SearchNode('B')

        A.add_link(B, 1)
        self.assertIsInstance(A['B'], tuple, 'attr is not a tuple')
        self.assertEquals(A['B'][0].name, 'B')
        self.assertEquals(A['B'][1], 1, 'weight is not correct')

    def test_node_getattr(self):
        A = SearchNode.SearchNode('A')
        B = SearchNode.SearchNode('B')

        A.add_link(B, 1)
        self.assertEquals(A.B.name, 'B', 'node is not correct')

    def test_node_chain(self):
        A = SearchNode.SearchNode('A')
        B = SearchNode.SearchNode('B')
        C = SearchNode.SearchNode('C')

        A.add_link(B, 1)
        B.add_link(C, 1)

        self.assertEquals(A.B.C.name, 'C')

    def test_node_cost(self):
        A = SearchNode.SearchNode('A')
        B = SearchNode.SearchNode('B')
        C = SearchNode.SearchNode('C')

        A.add_link(B, 1)
        B.add_link(C, 1)

        self.assertEquals(SearchNode.SearchNode.cost(A, [B, C]), 2)
        self.assertEquals(SearchNode.SearchNode.cost(A, ['B', 'C']), 2)
        self.assertEquals(SearchNode.SearchNode.cost(A, 'B.C'), 2)
        self.assertEquals(SearchNode.SearchNode.cost(A, 'BC'), 2)


if __name__ == '__main__':
    unittest.main()