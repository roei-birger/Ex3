from typing import List
from Map import Map
import heapq

from GraphAlgoInterface import GraphAlgoInterface
from NodeData import NodeData
from DiGraph import DiGraph


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, g: DiGraph):
        self.my_g = g
        self.path = {}

    def get_graph(self) -> DiGraph:
        return self.my_g

    def load_from_json(self, file_name: str) -> bool:
        pass

    def save_to_json(self, file_name: str) -> bool:
        pass

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        pass

    def shortest_path_dist(self, id1: int, id2: int) -> float:
        global path
        path = {}
        if self.my_g is None:
            return -1
        if id1 not in self.my_g.vertices or id2 not in self.my_g.vertices:
            return -1
        q = []
        if id1 == id2:
            return 0
        first = Map(id1)
        first.flag = 1
        first.dis = 0
        heapq.heappush(q, first)
        path[id1] = first
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


if __name__ == '__main__':
    print("f")
    # q = []
    # first = Map(3)
    # first.dis = 5
    # heapq.heappush(q, first)
    # sec = Map(4)
    # sec.dis = 6
    # heapq.heappush(q, sec)
    # print(q.pop(0).id)
    # print(q.pop(0).id)
