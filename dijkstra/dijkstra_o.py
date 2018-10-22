import networkx as nx
import numpy as np
from tools import read_graph_structure_scheme


class Dijkstra(object):
    def __init__(self):
        self.graph = None
        self.neighbors = None
        self.__edges = False

    def create_directed_graph(self):
        self.graph = nx.DiGraph()

    def create_undirected_graph(self):
        self.graph = nx.Graph()

    def add_weighted_edges(self, graph_scheme):
        self.graph.add_weighted_edges_from(graph_scheme)
        self.__edges = True

    def __set_neighbours(self):
        if self.__edges is False:
            raise IOError('Set graph structure with add_weighted_edges method, before try set neighbours')
        if self.graph is not None:
            self.neighbors = {key: list(self.graph.neighbors(key)) for key in list(self.graph.node)}
        else:
            Warning('Create graph with create_graph() method')

    def dijkstra(self, start):
        if self.graph is None:
            raise KeyError('Create graph with proper method')
        if self.__edges is False:
            raise IOError('Set graph structure with add_weighted_edges method')
        if start not in self.graph:
            raise IOError('Initialization point not in graph')
        if self.neighbors is None:
            self.__set_neighbours()

        S = set()
        delta = dict.fromkeys(list(self.graph.adj), np.inf)
        previous = dict.fromkeys(list(self.graph.adj), None)

        delta[start] = 0

        while S != set(self.graph.node):
            v = min((set(delta.keys()) - S), key=delta.get)
            for neighbor in set(self.neighbors[v]) - S:
                new_path = delta[v] + self.graph[v][neighbor]['weight']
                if new_path < delta[neighbor]:
                    delta[neighbor] = new_path
                    previous[neighbor] = v

            S.add(v)

        return (delta, previous)

    def shortest_path(self, start, end):
        if start not in self.graph:
            raise IOError('Initialization point not in graph')
        if end not in self.graph:
            raise IOError('End point not in graph')

        delta, previous = self.dijkstra(start)

        path = []
        vertex = end

        while vertex is not None:
            path.append(vertex)
            vertex = previous[vertex]

        path.reverse()

        return path


graph_structure_file = './dijkstra/graf.txt'
structure_scheme = read_graph_structure_scheme(graph_structure_file, ';')
structure_scheme = np.asarray(structure_scheme, dtype=int)

f = Dijkstra()
f.create_directed_graph()
f.add_weighted_edges(structure_scheme)
print(f.shortest_path(1, 20))

#  SHORT TEST
graph = nx.DiGraph()
graph.add_weighted_edges_from(structure_scheme)
assert nx.dijkstra_path(graph, 1, 20) == f.shortest_path(1, 20)
