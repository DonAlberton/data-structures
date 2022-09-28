import unittest
from datastructures.binarytree import BinaryTree
from datastructures.binarytree import reverse


class TestBinaryTree(unittest.TestCase):
    def test_reverse_binary_tree(self):
        tree = BinaryTree()

        tree.insert(10)
        tree.insert(5)
        tree.insert(3)
        tree.insert(7)
        tree.insert(6)
        tree.insert(15)

        reverse(tree)

        self.assertEqual(tree.inorder(), [15, 10, 7, 6, 5, 3])

        reverse(tree)

        self.assertEqual(tree.inorder(), [3, 5, 6, 7, 10, 15])

    def test_add_node(self):
        tree = BinaryTree()

        tree.insert(10)
        tree.insert(5)
        tree.insert(3)
        tree.insert(7)
        tree.insert(6)
        tree.insert(15)

        self.assertEqual(tree.inorder(), [3, 5, 6, 7, 10, 15])

    def test_delete(self):
        tree = BinaryTree()

        tree.insert(10)
        tree.insert(5)
        tree.insert(3)
        tree.insert(7)
        tree.insert(6)
        tree.insert(15)

        tree.delete(15)

        self.assertEqual(tree.inorder(), [3, 5, 6, 7, 10])

        tree.delete(7)

        self.assertEqual(tree.inorder(), [3, 5, 6, 10])

    def test_delete_all(self):
        tree = BinaryTree()

        tree.insert(5)
        tree.insert(10)
        tree.insert(4)
        tree.insert(3)
        tree.insert(1)

        tree.delete(5)
        tree.delete(10)
        tree.delete(4)
        tree.delete(3)
        tree.delete(1)

        self.assertEqual(tree.inorder(), [])


if __name__ == '__main__':
    unittest.main()
