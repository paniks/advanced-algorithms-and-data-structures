import re
import itertools

from multimethod import multimethod
from math import sqrt

from computer_graphics_algorithm.structures import Point, Face, Solid, Edge
from computer_graphics_algorithm.vector import Vector, dot, cross


SMALL_NUM = 0.00000001


def open_data(filename):
    lines = open(filename, 'r').read()
    solids = re.split("--- SOLID \[\d*\]---", lines)
    return [
        Solid([
            Face(
                *[Point(*[float(p) for p in point.split(";")])
                  for point in face.split("\n") if len(point) != 0]
            ) for face in solid.split("\n\n") if face != ""
        ]) for solid in solids if solid != ""
    ]


@multimethod
def distance(a: Point, b: Point) -> float:
    return sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2 + (a.z - b.z) ** 2)


@multimethod
def distance(e: Edge, p: Point) -> float:
    v = Vector(e.p0, e.p1)
    w = Vector(e.p0, p)

    c1 = dot(w, v)
    c2 = dot(v, v)
    if c1 <= 0:
        return distance(p, e.p0)
    if c2 <= c1:
        return distance(p, e.p1)

    b = c1 / c2

    pb = Point(
        e.p0.x + b * v.x,
        e.p0.y + b * v.y,
        e.p0.z + b * v.z
    )

    return distance(p, pb)


@multimethod
def distance(e1: Edge, e2: Edge) -> float:
    # print("EDGES")
    # http://geomalgorithms.com/a07-_distance.html#dist3D_Segment_to_Segment()

    u, v, w = Vector(e1.p0, e1.p1), Vector(e2.p0, e2.p1), Vector(e2.p0, e1.p0)
    a, b, c, d, e = dot(u, u), dot(u, v), dot(v, v), dot(u, w), dot(v, w)
    D = a*c - b*b

    sc, sN, sD = D, D, D
    tc, tN, tD = D, D, D

    if D < SMALL_NUM:
        sN, sD = 0.0, 1.0
        tN, tD = e, c
    else:
        sN, tN = (b*e - c*d), (a*e - b*d)

        if sN < 0.0:
            sN, tN, tD = 0.0, e, c
        elif sN > sD:
            sN, tN, tD = sD, e + b, c

    if tN < 0.0:
        tN = 0.0
        if -d < 0.0:
            sN = 0.0
        elif -d > a:
            sN = sD
        else:
            sN, sD = -d, a
    elif tN > tD:
        tN = tD
        if (-d + b) < 0.0:
            sN = 0
        elif (-d + b) > a:
            sN = sD
        else:
            sN, sD = (-d + b), a

    sc = 0.0 if abs(sN) < SMALL_NUM else sN / sD
    tc = 0.0 if abs(tN) < SMALL_NUM else tN / tD

    dP = w + (u * sc) - (v * tc)

    return dP.norm() if dP.norm() > SMALL_NUM else 0


@multimethod
def distance(f: Face, p: Point) -> float:
    # http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.104.4264&rep=rep1&type=pdf
    # p point projection to plane which face f lays in
    # normal Np of P1P2P3
    Np = cross(Vector(f.p0, f.p1), Vector(f.p0, f.p2))

    # the angle a between normal Np and P1P0
    cosa = dot(Vector(f.p0, p), Np) / (Np.length() * Vector(f.p0, p).length())

    # the length of P0P0'
    p0p0l = Vector(p, f.p0).length() * cosa

    # the vector P0P0'
    p0p0p = (Np / Np.length()) * (-1 * p0p0l)

    # point P0' from P0 and P0P0' vector
    p0p = p + p0p0p

    # compute baricentric coordinates
    area = cross(Vector(f.p0, f.p1), Vector(f.p0, f.p2)).length() / 2
    a = cross(Vector(p0p, f.p1), Vector(p0p, f.p2)).length() / (2 * area)
    b = cross(Vector(p0p, f.p2), Vector(p0p, f.p0)).length() / (2 * area)
    c = 1 - a - b
    # print("area, a, b, c: ", area, a, b, c)

    if 0 <= a <= 1 and 0 <= b <= 1 and 0 <= c <= 1:
        return sqrt(dot(p0p0p, p0p0p))
    else:
        e1 = Edge(f.p0, f.p1)
        e2 = Edge(f.p1, f.p2)
        e3 = Edge(f.p0, f.p2)

        return min(distance(e1, p), distance(e2, p), distance(e3, p), distance(f.p0, p), distance(f.p1, p), distance(f.p2, p))


@multimethod
def distance(a: Face, b: Face) -> float:
    # http://www.ikonstantinos.com/Konstantinos_Krestenitis_ACME2015.pdf
    ae1, ae2, ae3 = a.edges
    be1, be2, be3 = b.edges
    distances = [
        distance(a, b.p0),
        distance(a, b.p1),
        distance(a, b.p2),
        distance(b, a.p0),
        distance(b, a.p1),
        distance(b, a.p2),
        distance(ae1, be1),
        distance(ae1, be2),
        distance(ae1, be3),
        distance(ae2, be1),
        distance(ae2, be2),
        distance(ae2, be3),
        distance(ae3, be1),
        distance(ae3, be2),
        distance(ae3, be3)
    ]
    return min(distances)


@multimethod
def distance(a: Edge, b: Face) -> float:
    eb1, eb2, eb3 = b.edges
    return min(
        distance(a, eb1),
        distance(a, eb2),
        distance(a, eb3),
        distance(a, b.p0),
        distance(a, b.p1),
        distance(a, b.p2)
)


@multimethod
def distance(a: Solid, b: Solid) -> float:
    distances = [distance(f1, f2) for f1, f2 in itertools.product(a.faces, b.faces)]
    return min(distances)


filename = './computer_graphics_algorithm/solid_data.txt'
solids = open_data(filename)

print("faces: ",
      distance(Face(Point(1, 0, 0), Point(0, 1, 0), Point(0, 0, 0)),
               Face(Point(100, 0, 0.13), Point(0, 100, 0.13), Point(-100, -100, 0.13))
))


print("solids: ", distance(solids[0], solids[1]))