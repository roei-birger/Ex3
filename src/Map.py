import math


class Map:
    def __init__(self, id: int):
        self.id = id
        self.dis = math.inf
        self.parent = None
        self.flag = 0

    def __lt__(self, other):
        return self.dis < other.dis

    def __gt__(self, other):
        return self.dis > other.dis

    def __eq__(self, other):
        return self.dis == other.dis

    """object"""

    def __str__(self) -> str:
        return f"{self.id}"

    """inner object"""

    def __repr__(self) -> str:
        return f"{self.id}"
