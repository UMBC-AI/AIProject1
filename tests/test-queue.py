import unittest

from Algorithms import SearchQueue
from SearchNode import SearchNode


class MyQueue(unittest.TestCase):
    def test_queue_push(self):
        A = SearchNode('A')
        B = SearchNode('B')

        queue = SearchQueue()

        result = queue.push(A)

        self.assertTrue(result)
        self.assertEquals(len(queue), 1)

        queue.push(A)
        self.assertEquals(len(queue), 1)

    def test_queue_pop(self):
        A = SearchNode('A')
        B = SearchNode('B')

        queue = SearchQueue()

        queue.push(A)
        queue.push(B)

        self.assertEquals(len(queue), 2)

        node = queue.pop()

        self.assertEquals(len(queue), 1)
        self.assertIsInstance(node, SearchNode)
        self.assertEquals(node.name, 'A')

    def test_placed_by(self):
        A = SearchNode('A')
        B = SearchNode('B')

        queue = SearchQueue()

        queue.push(A)
        queue.push(B, A)

        node = queue.pop()

        self.assertIsNone(queue.placed_by(node.name))

        node = queue.pop()

        self.assertEquals(queue.placed_by(node.name).name, 'A')



if __name__ == '__main__':
    unittest.main()
