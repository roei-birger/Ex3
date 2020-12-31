from GraphInterface import GraphInterface
from NodeData import NodeData


class DiGraph(GraphInterface):
    """This class implements a directed weighted graph.
      Every graph contains a map of all its vertexes,
      a counter of the number of the vertex in the graph,
      a counter of the number of edges
      and a counter of the number of changes that were made on the graph ."""

    def __init__(self):
        """A default constructor"""
        self.mc = 0
        self.edge_size = 0
        self.node_size = 0
        self.vertices = {}  # <key , NodeData>

    def get_node(self, node_id: int) -> NodeData:
        """@param node_id - the node_id
         @return the node of this key, null if none."""
        if node_id in self.vertices:
            return self.vertices.get(node_id)
        return None

    def v_size(self) -> int:
        """@return the number of vertices (nodes) on the graph."""
        return self.node_size

    def e_size(self) -> int:
        """@return the number of edges on the graph."""
        return self.edge_size

    def get_all_v(self) -> dict:
        """@return a dictionary of all the nodes in the Graph, each node is represented using a pair
        (node_id, node_data)"""
        return self.vertices

    def all_in_edges_of_node(self, id1: int) -> dict:
        """@return a dictionary of all the nodes connected to (into) node_id ,
        each node is represented using a pair (other_node_id, weight)"""
        return self.get_node(id1).inEdges

    def all_out_edges_of_node(self, id1: int) -> dict:
        """@return a dictionary of all the nodes connected from node_id , each node is represented using a pair
        (other_node_id, weight)"""
        return self.get_node(id1).outEdges

    def get_mc(self) -> int:
        """@return the Mode Count of the changes made on the graph."""
        return self.mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        """This function makes an edge from id1 to id2,
        by inserting one node into the neighbor's list of the others node,
        in addition inserting one node into the edges list of the others node.
        @return true if success."""
        if weight >= 0 and id1 in self.vertices and id2 in self.vertices and id1 != id2:
            if id2 not in self.get_node(id1).outEdges:
                self.edge_size = self.edge_size + 1
            if id2 not in self.get_node(id1).outEdges or weight != self.get_node(id1).getWeight(id2):
                self.mc = self.mc + 1
            self.get_node(id1).addNi(self.get_node(id2), weight)
            return True
        return False

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        """Add a new node to the graph with the node_id that was received.
        @param node_id
        @param pos
        @return true if success."""
        if node_id in self.vertices:
            return False
        self.vertices[node_id] = NodeData(node_id, 0, pos)
        if len(self.vertices) == self.node_size + 1:
            self.node_size = self.node_size + 1
            self.mc = self.mc + 1
        return True

    def remove_node(self, node_id: int) -> bool:
        """The function passes over all the neighbors of the vertex and removes the common edges.
        Finally deletes the vertex from the graph.
        @return true if success."""
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
        """This function removes the edge that exists between two vertexes.
        and removes it from all the edges lists it was on .
        @param node_id1
        @param node_id2
        @return true if success."""
        if node_id1 != node_id2 and node_id1 in self.vertices and node_id2 in self.vertices and \
                node_id2 in self.get_node(node_id1).outEdges:
            self.get_node(node_id1).removeNode(self.get_node(node_id2))
            self.edge_size = self.edge_size - 1
            self.mc = self.mc + 1
            return True
        return False

    def __str__(self) -> str:
        """@return a string (str) representation of the DiGraph"""
        return f"{self.vertices}"

    def __repr__(self) -> str:
        """@return a string (repr) representation of the DiGraph"""
        return f"{self.vertices}"
