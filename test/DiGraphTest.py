import unittest

from NodeData import NodeData
from src.DiGraph import DiGraph


class DiGraphTest(unittest.TestCase):
    def setUp(self):
        global g
        g = DiGraph()
        g.add_node(NodeData(-101).id)
        g.add_node(NodeData(-15).id)
        g.add_node(NodeData(-1).id)
        g.add_node(NodeData(0).id)
        g.add_node(NodeData(3).id)
        g.add_node(NodeData(13).id)
        g.add_node(NodeData(53).id)
        g.add_node(NodeData(66).id)
        g.add_node(NodeData(555).id)

        g.add_edge(53, 13, 6.0)
        g.add_edge(53, 555, 2.1)
        g.add_edge(13, 3, 8.9)
        g.add_edge(3, 13, 8.9)
        g.add_edge(3, -15, 0.1)
        g.add_edge(-15, -1, 10)
        g.add_edge(-1, -101, 20)
        g.add_edge(-101, 3, 7.6)
        g.add_edge(-101, 0, 12)
        g.add_edge(0, -101, 21)
        g.add_edge(0, 555, 3.2)
        g.add_edge(555, 66, 2)
        g.add_edge(66, 0, 3.3)

    def test_get_node_base(self):
        self.assertEqual(0, g.get_node(0).id, "get_node didn't return the correct node from the default constructor")

    def test_get_node_negative_key(self):
        self.assertEqual(-1, g.get_node(-1).id, "get_node didn't return the correct node from the default constructor")

    def test_get_node_none(self):
        self.assertIsNone(g.get_node(9), "get_node didn't return null if the node isn't on the graph")

    def test_v_size_base(self):
        self.assertEqual(9, g.v_size(), "v_size didn't return the correct size")

    def test_v_size_after_remove_node(self):
        g.remove_node(0)
        g.remove_node(555)
        self.assertEqual(7, g.v_size(), "v_size didn't update the nodeSize after being removed")

    def test_v_size_after_add_node(self):
        g.add_node(NodeData(10).id)
        g.add_node(NodeData(16).id)
        g.add_node(NodeData(3).id)
        self.assertEqual(11, g.v_size(), "v_size didn't update the nodeSize after adding")

    def test_e_size_base(self):
        self.assertEqual(13, g.e_size(), "e_size didn't return the correct size")

    def test_e_size_after_remove_edge(self):
        g.remove_edge(-1, -101)
        g.remove_edge(6, -101)
        g.remove_edge(3, -15)
        self.assertEqual(11, g.e_size(), "e_size didn't update the edgeSize after being removed")

    def test_e_size_after_add_edge(self):
        g.add_edge(0, -101, 9)
        g.add_edge(3, -1, 0)
        self.assertEqual(14, g.e_size(), "e_size didn't update the edgeSize after being added")

    def test_get_all_v(self):
        temp = {-101: -101, -15: -15, -1: -1, 0: 0, 3: 3, 13: 13, 53: 53, 66: 66, 555: 555}
        self.assertEqual(temp.__str__(), g.get_all_v().__str__(), "get_all_v didn't return the correct dict")

    def test_all_in_edges_of_node(self):
        temp = {13: 8.9, -101: 7.6}
        self.assertEqual(temp.__str__(), g.all_in_edges_of_node(3).__str__(), "all_in_edges_of_node didn't return the "
                                                                              "correct dict")

    def test_all_out_edges_of_node(self):
        temp = {13: 8.9, -15: 0.1}
        self.assertEqual(temp.__str__(), g.all_out_edges_of_node(3).__str__(), "all_out_edges_of_node didn't return "
                                                                               "the correct dict")

    def test_get_mc_base(self):
        self.assertEqual(22, g.get_mc(), "get_mc didn't return the correct size")

    def test_get_mc_after_remove_node(self):
        g.remove_node(0)
        g.remove_node(555)
        self.assertEqual(30, g.get_mc(), "get_mc didn't update MC after removing the node")

    def test_get_mc_after_add_node(self):
        g.add_node(NodeData(10).id)
        g.add_node(NodeData(16).id)
        g.add_node(NodeData(0).id)
        self.assertEqual(24, g.get_mc(), "get_mc didn't update MC after adding the node")

    def test_get_mc_after_add_edge(self):
        g.add_edge(0, -101, 21)
        g.add_edge(3, -1, 0)
        self.assertEqual(23, g.get_mc(), "get_mc didn't update MC after adding the Edge")

    def test_get_mc_after_remove_edge(self):
        g.remove_edge(-1, -101)
        g.remove_edge(6, -101)
        g.remove_edge(3, -15)
        self.assertEqual(24, g.get_mc(), "get_mc didn't update the MC after removing the Edge")

    def test_add_node_pos(self):
        temp1 = g.v_size()
        g.add_node(NodeData(60).id)
        temp2 = g.v_size()
        self.assertEqual(60, g.get_node(60).id, "add_node didn't add a positive node")
        self.assertEqual(temp1 + 1, temp2, "add_node didn't add a positive node")

    def test_add_node_neg(self):
        temp1 = g.v_size()
        g.add_node(NodeData(-60).id)
        temp2 = g.v_size()
        self.assertEqual(-60, g.get_node(-60).id, "add_node didn't add a positive node")
        self.assertEqual(temp1 + 1, temp2, "add_node didn't add a positive node")

    def test_add_edge_base(self):
        g.add_edge(-1, 0, 0.7)
        self.assertTrue(g.get_node(-1).hasNi(0), "add_edge didn't insert edge between the nodes")
        self.assertEqual(0.7, g.get_node(-1).getWeight(0), "add_edge didn't update correct weight")

    def test_add_edge_negative_weight(self):
        g.add_edge(-1, 0, -0.7)
        self.assertFalse(g.get_node(-1).hasNi(0), "add_edge insert edge with negative weight")

    def test_add_edge_update_negative_weight(self):
        g.add_edge(66, 0, -0.7)
        self.assertEqual(3.3, g.get_node(66).getWeight(0), "add_edge update a negative weight between exist nodes")

    def test_add_edge_not_exist_node(self):
        self.assertFalse(g.add_edge(3, 4, 0.7), "add_edge insert edge between non existing node to existing node")

    def test_add_edge_not_exist_nodes(self):
        self.assertFalse(g.add_edge(6, 4, 0.7), "add_edge insert edge between non existing nodes")

    def test_add_edge_add_edge_size(self):
        temp1 = g.e_size()
        g.add_edge(-1, 0, 0.7)
        temp2 = g.e_size()
        self.assertEqual(temp1 + 1, temp2, "add_edge didn't update edgeSize")

    def test_add_edge_not_add_edge_size(self):
        temp1 = g.e_size()
        g.add_edge(9, 6, 0.7)
        g.add_edge(3, -15, 0.7)
        g.add_edge(3, 0, -0.7)
        temp2 = g.e_size()
        self.assertEqual(temp1, temp2, "add_edge updates edgeSize when it's not needed")

    def test_remove_node_base(self):
        self.assertTrue(g.remove_node(555) and g.node_size == 8, "remove_node didn't return the correct node")

    def test_remove_node_not_exist(self):
        self.assertFalse(g.remove_node(9) and g.node_size == 9,
                         "remove_node didn't return null when the non existing node was removed")

    def test_remove_node_not_exist_size(self):
        nodeSize = g.v_size()
        edgeSize = g.e_size()
        self.assertFalse(g.remove_node(9), "remove_node didn't return null when the non existing node was removed")
        self.assertEqual(nodeSize, g.v_size(), "remove_node didn't update the correct nodeSize")
        self.assertEqual(edgeSize, g.e_size(), "remove_node didn't update the correct edgeSize")

    def test_remove_node_neighbors(self):
        self.assertTrue(g.remove_node(555) and g.node_size == 8, "remove_node didn't return the correct node")
        self.assertFalse(555 in g.get_node(53).inEdges,
                         "remove_node didn't remove the node from the neighbours list")

    def test_remove_edge_base(self):
        edgeSize = g.e_size()
        g.remove_edge(-1, -101)
        self.assertFalse(g.get_node(-1).hasNi(-101), "remove_edge didn't remove the edge")
        self.assertEqual(edgeSize - 1, g.e_size(), "remove_edge didn't update edgeSize")

    def test_remove_edge_not_exist_edge(self):
        edgeSize = g.e_size()
        g.remove_edge(-1, 0)
        self.assertEqual(edgeSize, g.e_size(), "remove_edge updates edgeSize when the non existing edge is removed")

    def test_remove_edge_not_exist_node(self):
        edgeSize = g.e_size()
        g.remove_edge(6, 4)
        self.assertEqual(edgeSize, g.e_size(), "remove_edge update edgeSize when the non existing node is removed")

    def test_remove_edge_with_himself(self):
        edgeSize = g.e_size()
        g.remove_edge(3, 3)
        self.assertEqual(edgeSize, g.e_size(),
                         "remove_edge update edgeSize when the edge between the node to itself is removed")


if __name__ == '__main__':
    unittest.main()
