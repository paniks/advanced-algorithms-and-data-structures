import networkx as nx
import numpy as np


def read_graph_structure_scheme(graph_structure_scheme_file):
    with open(graph_structure_scheme_file, 'r') as f:
        tmp_structure = f.read().splitlines()
    f.close()

    structure = []
    for line in tmp_structure:
        structure.append(line.split(';'))

    return structure


graph_structure_file = './dijkstra/graf.txt'
structure_scheme = read_graph_structure_scheme(graph_structure_file)
structure_scheme = np.asarray(structure_scheme, dtype=int)

graph = nx.DiGraph()
graph.add_weighted_edges_from(structure_scheme)

"""
for line in structure_scheme:
    graph.add_edge(line[0], line[1], weight=line[2])
"""

print(nx.dijkstra_path(graph, 1, 20))
# TODO: write above function on my own
