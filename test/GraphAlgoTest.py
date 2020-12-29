import unittest
from NodeData import NodeData
from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo


class MyTestCase(unittest.TestCase):
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

        global ga
        ga = GraphAlgo(g)

    def test_shortest_path_dist_base(self):
        g.add_edge(13, -1, 40)
        self.assertEqual(28.4, ga.shortest_path_dist(53, -101), "shortest_path_dist returns uncorrected dist")
        self.assertEqual(19, ga.shortest_path_dist(13, -1), "shortest_path_dist returns uncorrected dist")
        self.assertEqual(6.5, ga.shortest_path_dist(66, 555), "shortest_path_dist returns uncorrected dist")

    def test_shortest_path_dist_node_to_himself(self):
        self.assertEqual(0, ga.shortest_path_dist(0, 0), "shortest_path_dist returns uncorrected dist from a node to "
                                                         "himself")

    def test_shortest_path_dist_none(self):
        ga = GraphAlgo(None)
        self.assertEqual(-1, ga.shortest_path_dist(0, -1), "shortest_path_dist returns uncorrected dist at null graph")

    def test_shortest_path_dist_not_exist(self):
        self.assertEqual(-1, ga.shortest_path_dist(0, -11),
                         "shortest_path_dist returns uncorrected dist if one node doesn't exist")
        self.assertEqual(-1, ga.shortest_path_dist(50, -11),
                         "shortest_path_dist returns uncorrected dist if two node doesn't exist")

    def test_shortest_path_dist_no_dist(self):
        g.add_node(NodeData(16).id)
        self.assertEqual(-1, ga.shortest_path_dist(0, 16), "shortest_path_dist returns uncorrected dist")

    def test_shortest_path_base(self):
        g.add_edge(13, -1, 40)
        finalList = [53, 555, 66, 0, -101]
        self.assertEqual((28.4, finalList).__str__(), ga.shortest_path(53, -101).__str__(), "shortest_path returns "
                                                                                            "uncorrected list")
        finalList = [13, 3, -15, -1]
        self.assertEqual((19.0, finalList).__str__(), ga.shortest_path(13, -1).__str__(), "shortest_path returns "
                                                                                          "uncorrected list")
        finalList = [66, 0, 555]
        self.assertEqual((6.5, finalList).__str__(), ga.shortest_path(66, 555).__str__(), "shortest_path returns "
                                                                                          "uncorrected list")

    def test_shortest_path_node_to_himself(self):
        finalList = [0]
        self.assertEqual((0, finalList).__str__(), ga.shortest_path(0, 0).__str__(),
                         "shortest_path returns uncorrected list from a node to itself")

    def test_shortest_path_null_graph(self):
        ga = GraphAlgo(None)
        self.assertEqual((-1, None), ga.shortest_path(0, 4), "shortest_path returns uncorrected list at null graph")


if __name__ == '__main__':
    unittest.main()
