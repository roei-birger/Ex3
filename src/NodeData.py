class NodeData:
    """ This class represents the set of operations applicable on a node (vertex) in a directional weighted graph.
    The vertex's neighbors and the connected edges are implemented by HashMap for high efficiency."""

    def __init__(self, id: int, tag: int = 0, location: tuple = None):
        """Constructs a NodeData with the same details that was received."""
        self.id = id
        self.tag = tag
        self.info = ""
        if location is not None:
            self.myLocation = location
        else:
            self.myLocation = (0, 0, 0)
        self.myNeighbors = {}  # <id_node , node_data>
        self.inEdges = {}  # <id_src , weight>
        self.outEdges = {}  # <id_dest , weight>

    def __str__(self) -> str:
        """@return a string (str) representation of the NodeData"""
        return f"{self.id}"

    def __repr__(self) -> str:
        """@return a string (repr) representation of the NodeData"""
        return f"{self.id}"

    def hasNi(self, node_id: int) -> bool:
        """ @param node_id
        @return true if there's an edge between the vertices."""
        return node_id in self.myNeighbors

    def addNi(self, node, weight: float) -> bool:
        """This function creates an edge between this vertex and node_data (t).
        @param node
        @param weight
        @return true if success."""
        if node.id not in self.myNeighbors and node.id != self.id and weight >= 0:
            self.myNeighbors[node.id] = node
            self.outEdges[node.id] = weight
            node.inEdges[self.id] = weight
        elif node.id in self.myNeighbors and node.id != self.id and weight >= 0:
            self.outEdges[node.id] = weight
            node.inEdges[self.id] = weight
        else:
            return False
        return True

    def removeNode(self, node) -> bool:
        """Removes the node and the edges between this vertex and others.
         @param node
         @return true if success."""
        if node.id in self.myNeighbors:
            self.myNeighbors.pop(node.id)
            self.outEdges.pop(node.id)
            node.inEdges.pop(self.id)
            return True
        return False


def getWeight(self, dest: int) -> float:
    """@return the weight of the edge."""
    if dest in self.outEdges:
        return self.outEdges.get(dest)
    return -1


def __eq__(self, o: object) -> bool:
    """Indicates whether some other NodeData is "equal to" this one.
    by examining each element in the NodeInfo obj.
    @param o (NodeData)
    @return true if this NodeData is the same as the NodeData; false otherwise."""
    if isinstance(o, NodeData):
        if self.id != o.id:
            return False

        if self.tag != o.tag:
            return False

        if self.info != o.info:
            return False

        if self.myNeighbors != o.myNeighbors:
            return False

        if self.inEdges != o.inEdges:
            return False

        if self.outEdges != o.outEdges:
            return False
        return True
    return False
