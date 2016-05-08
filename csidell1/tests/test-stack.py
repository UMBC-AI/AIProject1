import unittest
from SearchNode import SearchNode
from SearchStructure import SearchStack


class MyStack(unittest.TestCase):

    def test_queue_push(self):
        A = SearchNode('A')

        stack = SearchStack()

        result = stack.push(A)

        self.assertTrue(result)
        self.assertEquals(len(stack), 1)

        stack.push(A)
        self.assertEquals(len(stack), 1)

    def test_stack_pop(self):
        A = SearchNode('A')
        B = SearchNode('B')

        stack = SearchStack()

        stack.push(A)
        stack.push(B)

        self.assertEquals(len(stack), 2)

        node = stack.pop()

        self.assertEquals(len(stack), 1)
        self.assertIsInstance(node, SearchNode)
        self.assertEquals(node.name, 'B')

    def test_advanced_pushpop(self):
        A = SearchNode('A')

        stack = SearchStack()

        result = stack.push(A)

        self.assertTrue(result)
        self.assertEquals(len(stack), 1)

        stack.push(A)
        self.assertEquals(len(stack), 1)

        stack.pop()
        stack.push(A)
        self.assertEquals(len(stack), 0)

    def test_placed_by(self):
        A = SearchNode('A')
        B = SearchNode('B')

        stack = SearchStack()

        stack.push(A)
        stack.push(B, A)

        node = stack.pop()

        self.assertEquals(stack.placed_by(node.name).name, 'A')

        node = stack.pop()

        self.assertIsNone(stack.placed_by(node.name))

if __name__ == '__main__':
    unittest.main()
