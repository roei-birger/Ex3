import math


class Map:
    """This class represents a support object for the "shortestPath" method,
     at the "shortestPathDist" method the graph is tested to find the shortest
     path between vertices. Each vertex that is found in this way is preserved
     by this object in order to know which vertex was "his parent"
     on the way and what is the weight of the edge between them."""
    def __init__(self, id: int):
        """Constructs a Map with a basic fields."""
        self.id = id
        self.dis = math.inf
        self.parent = None
        self.flag = 0

    def __lt__(self, other):
        """Defines the behaviour of the less-than operator"""
        return self.dis < other.dis

    def __gt__(self, other):
        """Defines the behaviour of the greater-than operator"""
        return self.dis > other.dis

    def __eq__(self, other):
        """Defines the behaviour of the equality operator"""
        return self.dis == other.dis

    def __str__(self) -> str:
        """@return a string (str) representation of the Map"""
        return f"{self.id}"

    def __repr__(self) -> str:
        """@return a string (repr) representation of the Map"""
        return f"{self.id}"
