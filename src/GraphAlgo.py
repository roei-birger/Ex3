from typing import List

import matplotlib.pyplot as plt
from Map import Map
import heapq
import random
from collections import deque
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
        """This function saves the directed weighted graph to the given
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
        """Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm.
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
        """
        @param id1 - The node id
        @return the Strongly Connected Component(SCC) node list of the given node id.
        Notes:
        If the graph is None or id1 is not in the graph, the function should return an empty list []"""
        if self.my_g is None or id1 not in self.my_g.vertices:
            return []
        if self.my_g.node_size == 1:
            return [id1]
        for i in self.my_g.vertices:
            self.my_g.get_node(i).tag = 0
        q = deque()
        self.my_g.get_node(id1).tag = 1
        q.append(id1)
        my_list_out = []
        while q:
            temp = q.popleft()
            if self.my_g.get_node(temp).tag == 1:
                for j in self.my_g.get_node(temp).outEdges:
                    if self.my_g.get_node(j).tag == 0:
                        q.append(j)
                        self.my_g.get_node(j).tag = 1
            my_list_out.append(temp)
            self.my_g.get_node(temp).tag = 2

        for i in self.my_g.vertices:
            self.my_g.get_node(i).tag = 0
        self.my_g.get_node(id1).tag = 1
        q.append(id1)
        my_list_in = []
        while q:
            temp = q.popleft()
            if self.my_g.get_node(temp).tag == 1:
                for j in self.my_g.get_node(temp).inEdges:
                    if self.my_g.get_node(j).tag == 0:
                        q.append(j)
                        self.my_g.get_node(j).tag = 1
            my_list_in.append(temp)
            self.my_g.get_node(temp).tag = 2
        return list(set(my_list_out) & set(my_list_in))

    def connected_components(self) -> List[list]:
        """
        @return the list all the Strongly Connected Component(SCC) in the graph.
        Notes:
        If the graph is None, the function should return an empty list []
        """
        if self.my_g is None:
            return []
        used = {}
        final_list = []
        for i in self.my_g.vertices:
            if i not in used:
                temp_list = self.connected_component(i)
                for j in temp_list:
                    used[j] = j
                final_list.append(temp_list)
        return final_list

    def plot_graph(self) -> None:
        """Plots the graph."""
        x = []
        y = []

        for i in self.my_g.vertices:
            if self.my_g.get_node(i).myLocation == (-1, -1, -1):
                self.my_g.get_node(i).myLocation = (random.uniform(0.0, 60.0), random.uniform(0.0, 50.0), 0.0)
            pos = self.my_g.get_node(i).myLocation
            x.append(pos[0])
            y.append(pos[1])
            plt.annotate(i, (pos[0], pos[1]+1))
        plt.plot(x, y, 'o')

        for i in self.my_g.vertices:
            for j in self.my_g.all_out_edges_of_node(i):
                ix = self.my_g.get_node(i).myLocation[0]
                iy = self.my_g.get_node(i).myLocation[1]
                jx = self.my_g.get_node(j).myLocation[0]
                jy = self.my_g.get_node(j).myLocation[1]
                plt.annotate(text="", xy=(ix, iy), xytext=(jx, jy), arrowprops=dict(arrowstyle="<|-"))
                #plt.annotate(self.my_g.get_node(i).getWeight(j), ((ix+jx)/2, (iy+jy)/2))

        plt.title('Yaara & Roei graph')

        plt.show()



