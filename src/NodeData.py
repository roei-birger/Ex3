class NodeData:
    def __init__(self, id: int, tag: int = 0):
        self.id = id
        self.tag = tag
        self.info = ""
        self.myLocation = [0, 0, 0]
        self.myNeighbors = {}  # <id_node , node_data>
        self.inEdges = {}  # <id_src , weight>
        self.outEdges = {}  # <id_dest , weight>

    """object"""

    def __str__(self) -> str:
        return f"{self.id}"

    """inner object"""

    def __repr__(self) -> str:
        return f"{self.id}"

    def hasNi(self, node_id: int) -> bool:
        return node_id in self.myNeighbors

    def addNi(self, node, weight: float) -> bool:
        if node.id in self.myNeighbors:
            return False
        self.myNeighbors[node.id] = node
        self.outEdges[node.id] = weight
        node.inEdges[self.id] = weight
        return True

    def removeNode(self, node) -> bool:
        if node.id in self.myNeighbors:
            self.myNeighbors.pop(node.id)
            self.outEdges.pop(node.id)
            node.inEdges.pop(self.id)
            return True
        return False

    def getWeight(self, dest: int) -> float:
        if dest in self.outEdges:
            return self.outEdges.get(dest)
        return -1

    def __eq__(self, o: object) -> bool:
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


if __name__ == '__main__':
    n = NodeData(5, 3)
    n2 = NodeData(4, 1)
    n3 = NodeData(6, 1)
    n.addNi(n2, 2.4)
    n.addNi(n3, 4)
    print(n.getWeight(n2.id))