from GraphInterface import GraphInterface
from NodeData import NodeData


class DiGraph(GraphInterface):

    def __init__(self):
        self.mc = 0
        self.edge_size = 0
        self.node_size = 0
        self.vertices = {}  # <key , NodeData>

    def get_node(self, node_id: int) -> NodeData:
        if node_id in self.vertices:
            return self.vertices.get(node_id)
        return None

    def v_size(self) -> int:
        return self.node_size

    def e_size(self) -> int:
        return self.edge_size

    def get_mc(self) -> int:
        return self.mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if weight >= 0 and id1 in self.vertices and id2 in self.vertices and id1 != id2:
            if id2 not in self.get_node(id1).outEdges:
                self.edge_size = self.edge_size + 1
            if id2 not in self.get_node(id1).outEdges or weight != self.get_node(id1).getWeight(id2):
                self.mc = self.mc + 1
            self.get_node(id1).addNi(self.get_node(id2), weight)
            return True
        return False

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if node_id in self.vertices:
            return False
        self.vertices[node_id] = NodeData(node_id, 0, pos)
        if len(self.vertices) == self.node_size + 1:
            self.node_size = self.node_size + 1
            self.mc = self.mc + 1
        return True

    def remove_node(self, node_id: int) -> bool:
        if node_id not in self.vertices:
            return False
        counter = len(self.get_node(node_id).outEdges)
        for i in self.vertices.keys():
            if i != node_id:
                if node_id in self.get_node(i).inEdges:
                    self.get_node(node_id).removeNode(self.get_node(i))
                    self.edge_size = self.edge_size - 1
                    self.mc = self.mc + 1
                if node_id in self.get_node(i).outEdges:
                    self.get_node(i).removeNode(self.get_node(node_id))
                    self.edge_size = self.edge_size - 1
                    self.mc = self.mc + 1
        self.edge_size = self.edge_size - counter
        self.vertices.pop(node_id)
        self.node_size = self.node_size - 1
        self.mc = self.mc + 1
        return True

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if node_id1 != node_id2 and node_id1 in self.vertices and node_id2 in self.vertices and \
                node_id2 in self.get_node(node_id1).outEdges:
            self.get_node(node_id1).removeNode(self.get_node(node_id2))
            self.edge_size = self.edge_size - 1
            self.mc = self.mc + 1
            return True
        return False

    """object"""

    def __str__(self) -> str:
        return f"{self.vertices}"

    """inner object"""

    def __repr__(self) -> str:
        return f"{self.vertices}"
