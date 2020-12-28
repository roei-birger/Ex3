import unittest

from src.NodeData import NodeData


class NodeDataTest(unittest.TestCase):
    def setUp(self):
        global n, n1, n2
        n = NodeData(5)
        n1 = NodeData(2)
        n2 = NodeData(4)
        n.addNi(n1, 4.4)
        n.addNi(n2, 9.4)
        n.tag = 1
        n.info = "b"
        n.myLocation = (1, 1, 1)

    def test_hasNi(self):
        self.assertTrue(n.hasNi(2), "hasNi didn't return the correct answer")
        self.assertTrue(n.hasNi(4), "hasNi didn't return the correct answer")
        self.assertFalse(n.hasNi(3), "hasNi didn't return the correct answer")

    def test_addNi(self):
        n.addNi(NodeData(6), 0.0)
        self.assertTrue(n.hasNi(6), "addNi couldn't update successfully")

    def test_getWeight(self):
        self.assertEqual(4.4, n.getWeight(n1.id), "getWeight didn't return the correct weight")

    def test_removeNode(self):
        temp = NodeData(6)
        n.addNi(temp, 0.8)
        n.removeNode(temp)
        self.assertFalse(n.hasNi(6), "removeNode couldn't update successfully")


if __name__ == '__main__':
    unittest.main()
