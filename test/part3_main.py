import unittest
import random
from DiGraph import DiGraph
from GraphAlgo import GraphAlgo
from NodeData import NodeData
import time


class MyTestCase(unittest.TestCase):
   # def test_save_big_graphs(self):
        # global g
        # g = DiGraph()
        # x = 1000000
        # for i in range(x):
        #     g.add_node(NodeData(id=i).id)
        #     g.get_node(i).myLocation = (random.uniform(0.0, 60.0), random.uniform(0.0, 50.0), 0.0)
        #
        # for j in range(x):
        #     g.add_edge(j, (j + 2050) % x, random.uniform(0.0, 20.0))
        #     # g.add_edge(j, int(random.uniform(0, x)), random.uniform(0.0, 20.0))
        #
        # global ga
        #
        # ga = GraphAlgo(g)
        #
        # ga.save_to_json("1000000_nodes.json")
        # print("nodes - ", ga.my_g.node_size, " edges - ", ga.my_g.edge_size)

    def test_time_100_graphs(self):
        print("__________________________________________________________________--")
        G = GraphAlgo(None)
        start_all = time.time()

        start_load = time.time()
        G.load_from_json("100_nodes.json")
        end_load = time.time()
        print("loading 100 node graph: " + (end_load - start_load).__str__())

        start_shortest_path = time.time()
        print(G.shortest_path(42, 22))
        end__shortest_path = time.time()
        print("shortest path 100 node graph: " + (end__shortest_path - start_shortest_path).__str__())

        start_connected_component = time.time()
        print(G.connected_component(82).__sizeof__())
        end_connected_component = time.time()
        print("connected_component 100 node graph: " + (end_connected_component - start_connected_component).__str__())

        start_connected_components = time.time()
        print(G.connected_components().__sizeof__())
        end_connected_components = time.time()
        print(
            "connected_components 100 node graph: " + (end_connected_components - start_connected_components).__str__())

        end_all = time.time()
        print("all 100 node graph : " + (end_all - start_all).__str__())
        print("__________________________________________________________________--")

    def test_time_10000_graphs(self):
        print("__________________________________________________________________--")

        G = GraphAlgo(None)
        start_all = time.time()

        start_load = time.time()
        G.load_from_json("10000_nodes.json")
        end_load = time.time()
        print("loading 10000 node graph: " + (end_load - start_load).__str__())

        start_shortest_path = time.time()
        print(G.shortest_path(8125, 7725))
        end__shortest_path = time.time()
        print("shortest path 10000 node graph: " + (end__shortest_path - start_shortest_path).__str__())

        start_connected_component = time.time()
        print(G.connected_component(8125).__sizeof__())
        end_connected_component = time.time()
        print(
            "connected_component 10000 node graph: " + (end_connected_component - start_connected_component).__str__())

        start_connected_components = time.time()
        print(G.connected_components().__sizeof__())
        end_connected_components = time.time()
        print("connected_components 10000 node graph: " + (
                    end_connected_components - start_connected_components).__str__())

        end_all = time.time()
        print("all 10000 node graph : " + (end_all - start_all).__str__())
        print("__________________________________________________________________--")

    def test_time_100000_graphs(self):
        print("__________________________________________________________________--")

        G = GraphAlgo(None)
        start_all = time.time()

        start_load = time.time()
        G.load_from_json("100000_nodes.json")
        end_load = time.time()
        print("loading 100000 node graph: " + (end_load - start_load).__str__())

        start_shortest_path = time.time()
        print(G.shortest_path(67596, 99996))
        end__shortest_path = time.time()
        print("shortest path 100000 node graph: " + (end__shortest_path - start_shortest_path).__str__())

        start_connected_component = time.time()
        print(G.connected_component(99996).__sizeof__())
        end_connected_component = time.time()
        print(
            "connected_component 100000 node graph: " + (end_connected_component - start_connected_component).__str__())

        start_connected_components = time.time()
        print(G.connected_components().__sizeof__())
        end_connected_components = time.time()
        print("connected_components 100000 node graph: " + (
                    end_connected_components - start_connected_components).__str__())

        end_all = time.time()
        print("all 100000 node graph : " + (end_all - start_all).__str__())
        print("__________________________________________________________________--")

    def test_time_1000000_graphs(self):
        print("__________________________________________________________________--")

        G = GraphAlgo(None)
        start_all = time.time()

        start_load = time.time()
        G.load_from_json("1000000_nodes.json")
        end_load = time.time()
        print("loading 1000000 node graph: " + (end_load - start_load).__str__())

        start_shortest_path = time.time()
        print(G.shortest_path(786296, 99996))
        end__shortest_path = time.time()
        print("shortest path 1000000 node graph: " + (end__shortest_path - start_shortest_path).__str__())

        start_connected_component = time.time()
        print(G.connected_component(99996).__sizeof__())
        end_connected_component = time.time()
        print(
            "connected_component 1000000 node graph: " + (end_connected_component - start_connected_component).__str__())

        start_connected_components = time.time()
        print(G.connected_components().__sizeof__())
        end_connected_components = time.time()
        print("connected_components 1000000 node graph: " + (
                    end_connected_components - start_connected_components).__str__())

        end_all = time.time()
        print("all 100000 node graph : " + (end_all - start_all).__str__())
        print("__________________________________________________________________--")


if __name__ == '__main__':
    unittest.main()
