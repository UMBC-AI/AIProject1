import unittest
from SearchStructure import SearchPriorityQueue
from SearchNode import SearchNode


class MyPQueue(unittest.TestCase):
    def test_queue_push(self):
        A = SearchNode('A')

        queue = SearchPriorityQueue()

        result = queue.push(A)

        self.assertTrue(result)
        self.assertEquals(len(queue), 1)

        queue.push(A)
        self.assertEquals(len(queue), 2)

    def test_queue_pop(self):
        A = SearchNode('A')
        B = SearchNode('B')

        queue = SearchPriorityQueue()

        queue.push(A)
        queue.push(B)

        self.assertEquals(len(queue), 2)

        node = queue.pop()

        self.assertEquals(len(queue), 1)
        self.assertIsInstance(node, SearchNode)
        self.assertEquals(node.name, 'A')

    def test_advanced_pushpop(self):
        A = SearchNode('A')

        queue = SearchPriorityQueue()

        result = queue.push(A)

        self.assertTrue(result)
        self.assertEquals(len(queue), 1)

        queue.push(A)
        self.assertEquals(len(queue), 2)

        queue.pop()
        queue.push(A)

        self.assertEquals(len(queue), 1)

        # Should pop other A and not return
        result = queue.pop()
        self.assertIsNone(result)
        self.assertEquals(len(queue), 0)

    def test_placed_by(self):
        A = SearchNode('A')
        B = SearchNode('B')
        C = SearchNode('C')
        D = SearchNode('D')

        queue = SearchPriorityQueue()

        A.add_link(B, 40)
        A.add_link(C, 1)
        A.add_link(D, 20)

        queue.push(A)
        queue.push(B, A)
        queue.push(C, A)
        queue.push(D, A)

        node = queue.pop()

        self.assertIsNone(queue.placed_by(node.name))

        node = queue.pop()

        # C has shortest distance,
        self.assertEquals(node.name, 'C')
        self.assertEquals(queue.placed_by(node.name).name, 'A')


if __name__ == '__main__':
    unittest.main()
