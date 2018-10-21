import networkx as nx
import numpy as np


def read_graph_structure_scheme(graph_structure_scheme_file):
    with open(graph_structure_scheme_file, 'r') as f:
        tmp_structure = f.read().splitlines()
    f.close()

    structure = []
    for line in tmp_structure:
        structure.append(line.split('\t'))

    return structure


structure_scheme = read_graph_structure_scheme('ford_fulkerson/graf.txt')
structure_scheme = np.asarray(structure_scheme)
structure_scheme = structure_scheme[:, 0:3].astype(float)

graph = nx.DiGraph()
graph.add_weighted_edges_from(structure_scheme)

