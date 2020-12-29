from typing import List
from Map import Map
import heapq
import json
from GraphAlgoInterface import GraphAlgoInterface
from NodeData import NodeData
from DiGraph import DiGraph


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, g: DiGraph = None):
        self.my_g = g
        self.path = {}

    def get_graph(self) -> DiGraph:
        return self.my_g

    def load_from_json(self, file_name: str) -> bool:
        try:
            self.my_g = DiGraph()
            fp = open(file_name)
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
        if self.my_g is None:
            return False

        edges = []
        nodes = []

        for i in self.my_g.vertices:
            id = i
            pos = self.my_g.get_node(i).myLocation
            nodes.append({"pos": pos, "id": id})

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
        dist = self.shortest_path_dist(id1, id2)
        if dist < 0:
            return -1, None
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

