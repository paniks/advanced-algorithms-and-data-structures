class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        from computer_graphics_algorithm.vector import Vector
        if isinstance(other, Vector):
            return Point(self.x + other.x,
                         self.y + other.y,
                         self.z + other.z)

    def __sub__(self, other):
        from computer_graphics_algorithm.vector import Vector
        if isinstance(other, Vector):
            return Point(self.x - other.x,
                         self.y - other.y,
                         self.z - other.z)


class Edge:
    def __init__(self, p0, p1):
        self.p0 = p0
        self.p1 = p1


class Face:
    def __init__(self, p0, p1, p2):
        self.p0 = p0
        self.p1 = p1
        self.p2 = p2

    @property
    def edges(self):
        return [Edge(self.p0, self.p1),
                Edge(self.p1, self.p2),
                Edge(self.p0, self.p2)]


class Solid:
    def __init__(self, faces: list):
        self.faces = faces
