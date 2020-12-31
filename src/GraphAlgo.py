from typing import List
from Map import Map
import heapq
import json
from GraphAlgoInterface import GraphAlgoInterface
from NodeData import NodeData
from DiGraph import DiGraph


class GraphAlgo(GraphAlgoInterface):
    """This class creates a graph and includes algorithms:
    -if the graph is connected
    -How long it takes to get from one vertex to another
    -What is the shortest path from one vertex to another
    -Saves the graph to the given file name
    -Loads a graph to graph algorithm"""

    def __init__(self, g: DiGraph = None):
        """A default constructor and preforms a shallow copy graph.
        @param g"""
        self.my_g = g
        self.path = {}

    def get_graph(self) -> DiGraph:
        """@return the DiGraph at the GraphAlgo.init"""
        return self.my_g

    def load_from_json(self, file_name: str) -> bool:
        """This function loads a graph to graph algorithm from JSON format file.
        If the file was successfully loaded - the graph will be changed,
        If graph was not loaded the original graph should remain "as is".
        @param file_name - file name
        @return true - if the graph was successfully loaded."""
        try:
            self.my_g = DiGraph()
            fp = open(file_name, 'r')
            temp_graph = json.load(fp)
            edges_dic = temp_graph.get('Edges')
            nodes_dic = temp_graph.get('Nodes')

            for i in nodes_dic:
                if i.get('pos') is not None:
                    pos_i = i['pos']
                    pos_list = pos_i.split(sep=",", maxsplit=2)
                    temp_id = i.get('id')
                    self.my_g.add_node(node_id=NodeData(temp_id).id, pos=(float(pos_list[0]), float(pos_list[1]),
                                                                          float(pos_list[2])))
                else:
                    temp_id = i.get('id')
                    self.my_g.add_node(node_id=NodeData(temp_id).id)

            for j in edges_dic:
                weight = j.get('w')
                src = j.get('src')
                dest = j.get('dest')
                self.my_g.add_edge(src, dest, weight)
            fp.close()
        except FileExistsError:
            return False
        return True

    def save_to_json(self, file_name: str) -> bool:
        """* This function saves the directed weighted graph to the given
        file name - in JSON format
        @param file_name - the file name .
        @return true - iff the file was successfully saved"""
        if self.my_g is None:
            return False

        edges = []
        nodes = []

        for i in self.my_g.vertices:
            id = i
            pos_list = self.my_g.get_node(i).myLocation
            pos_string = "{},{},{}"
            pos_string = pos_string.format(pos_list[0], pos_list[1], pos_list[2])
            nodes.append({"pos": pos_string, "id": id})

        for j in self.my_g.vertices:
            for k in self.my_g.get_node(j).outEdges:
                src = j
                w = self.my_g.get_node(j).outEdges[k]
                dest = k
                edges.append({"src": src, "w": w, "dest": dest})

        graph = {"Nodes": nodes, "Edges": edges}
        with open(file_name, 'w') as json_file:
            json.dump(graph, json_file)

        return True

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        """Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm
        @param id1: The start node id
        @param id2: The end node id
        @return: The distance of the path, a list of the nodes ids that the path goes through"""
        dist = self.shortest_path_dist(id1, id2)
        if dist < 0:
            return float('inf'), []
        final_list = []
        temp0 = path[id2]
        tempN = self.my_g.get_node(temp0.id)
        if id1 == id2:
            final_list.append(tempN.id)
            return 0, final_list
        final_list.append(tempN.id)
        while temp0.dis > 0:
            temp0 = temp0.parent
            tempN = self.my_g.get_node(temp0.id)
            final_list.append(tempN)
        final_list.reverse()
        return dist, final_list

    def shortest_path_dist(self, id1: int, id2: int) -> float:
        """This function returns the length of the shortest path between two vertexes on the graph
        by checking all the graph vertexes edges and its neighbors edges
        by pushing them to a priority queue (Dijkstra algorithm)
        @param id1  - start node
        @param id2 - end (target) node"""
        global path
        path = {}
        if self.my_g is None:
            return -1
        if id1 not in self.my_g.vertices or id2 not in self.my_g.vertices:
            return -1
        q = []
        first = Map(id1)
        first.flag = 1
        first.dis = 0
        heapq.heappush(q, first)
        path[id1] = first
        if id1 == id2:
            return 0
        while q:
            temp = q.pop(0)
            if temp.flag == 1:
                if temp.id == id2:
                    return temp.dis
                else:
                    for i in self.my_g.get_node(temp.id).outEdges:
                        if i not in path:
                            p = Map(i)
                            path[i] = p
                            p.dis = temp.dis + self.my_g.get_node(temp.id).outEdges.get(i)
                            p.parent = temp
                            heapq.heappush(q, p)
                            p.flag = 1
                        else:
                            p = path[i]
                            sum_edge = self.my_g.get_node(temp.id).outEdges.get(i)
                            if temp.dis + sum_edge <= p.dis:
                                p.dis = temp.dis + sum_edge
                                p.parent = temp
                                heapq.heappush(q, p)
            temp.flag = 2

        return -1

    def connected_component(self, id1: int) -> list:
        pass

    def connected_components(self) -> List[list]:
        pass

    def plot_graph(self) -> None:
        pass

