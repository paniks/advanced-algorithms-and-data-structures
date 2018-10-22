import networkx as nx
import numpy as np

from tools import read_graph_structure_scheme


class FordFulkerson(object):
    def __init__(self):
        self.graph = None
        self.residual = None

    def create_graph(self, graph_scheme):
        self.graph = nx.DiGraph()
        for i in graph_scheme:
            self.graph.add_edge(str(i[0]), str(i[1]), capacity=float(i[2]), flow=0)

        self.__create_residual()

    def __create_residual(self):
        self.residual = nx.algorithms.flow.utils.build_residual_network(self.graph, 'capacity')
        for u in self.residual:
            for e in self.residual[u].values():
                e['flow'] = 0

        self.residual_successors = self.residual.succ
        self.residual_predecessors = self.residual.pred
        self.residual_nodes = self.residual.nodes

    def breadth_first_search(self, src, target):

        pred = {src: None}
        path_s = [src]
        succ = {target: None}
        path_t = [target]
        while True:
            path = []
            if len(path_s) <= len(path_t):
                for u in path_s:
                    for v, attr in self.residual_successors[u].items():
                        if v not in pred and attr['flow'] < attr['capacity']:
                            pred[v] = u
                            if v in succ:
                                return v, pred, succ
                            path.append(v)
                if not path:
                    return None, None, None
                path_s = path
            else:
                for u in path_t:
                    for v, attr in self.residual_predecessors[u].items():
                        if v not in succ and attr['flow'] < attr['capacity']:
                            succ[v] = u
                            if v in pred:
                                return v, pred, succ
                            path.append(v)
                if not path:
                    return None, None, None
                path_t = path

    def augment(self, path):
        inf = self.residual.graph['inf']
        flow = inf
        it = iter(path)
        u = next(it)
        for v in it:
            attr = self.residual_successors[u][v]
            flow = min(flow, attr['capacity'] - attr['flow'])
            u = v

        it = iter(path)
        u = next(it)
        for v in it:
            self.residual_successors[u][v]['flow'] += flow
            self.residual_successors[v][u]['flow'] -= flow
            u = v
        return flow

    def max_flow(self, source, target, cutoff=float('inf')):
        flow_value = 0
        while flow_value < cutoff:
            v, pred, succ = self.breadth_first_search(source, target)
            if pred is None:
                break

            path = [v]
            u = v

            while u != source:
                u = pred[u]
                path.append(u)
            path.reverse()

            u = v
            while u != target:
                u = succ[u]
                path.append(u)

            flow_value += self.augment(path)

        return flow_value


graph_structure_scheme_file = 'ford_fulkerson/graf.txt'
structure_scheme = read_graph_structure_scheme('ford_fulkerson/graf.txt', '\t')
structure_scheme = np.asarray(structure_scheme)

a = FordFulkerson()
a.create_graph(structure_scheme)
print(a.max_flow('10', '60'))
