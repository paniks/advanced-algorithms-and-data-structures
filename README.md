# Advanced algorithms and data structures
Subject realized as course during studies.

The aim of those project classes is to present students theory of algorithms with 
particular emphasis on problems that do not fit in the basic course in this subject.

## Prepare environment

Scrpits wrote on Linux Ubuntu 16.04LTS with Python3.5.2.

Update system
```bash
sudo apt-get update
sudo apt-get upgrade
```

Prepare Python 3.5 env
```bash
sudo apt-get install python3.5
sudo pip3 install virtualenv

(it's my favorite way to manage python's virtualenvs, it's not obligatory or something)
mkdir ~/venvs
cd ~/venvs/

virtualenv aads -p $(which python3)
```

Clone repo with https

```bash
cd directory
git clone https://github.com/paniks/advanced-algorithms-and-data-structures.git
```

Activate virtualenv and install requirements
```bash
(in project dir)

source path/to/venv/bin/activate
pip install -r requiments.txt
```


## Lab 1. Dijkstra's algorithm
#### Task Description
1. Implement Disjkstra algorithm (being used in the Open Shortest Path First routing protocol) using any graph library, e.g., JUNG for JAVA or NetworkX for Python.

2. Test it using this input file containg the weighted graph (see the example below) data given as a sequence of records of the form (source vertex index;destination vertex index;edge weight). Find  distance between vertices 1 and 20 and all vertices on the path (incl. endpoints, i.e., nodes 1 and 20)

#### Algorithm description
Is an algorithm for finding the shortest paths between nodes in a graph, which may represent, for example, road networks
 
Algorithm via [Wikipedia](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm#Algorithm) in steps : 
1. Mark all nodes unvisited. Create a set of all the unvisited nodes called the unvisited set.
2. Assign to every node a tentative distance value: set it to zero for our initial node and to infinity for all other nodes. Set the initial node as current.
3. For the current node, consider all of its unvisited neighbors and calculate their tentative distances through the current node. Compare the newly calculated tentative distance to the current assigned value and assign the smaller one. For example, if the current node A is marked with a distance of 6, and the edge connecting it with a neighbor B has length 2, then the distance to B through A will be 6 + 2 = 8. If B was previously marked with a distance greater than 8 then change it to 8. Otherwise, keep the current value.
4. When we are done considering all of the unvisited neighbors of the current node, mark the current node as visited and remove it from the unvisited set. A visited node will never be checked again.
5. If the destination node has been marked visited (when planning a route between two specific nodes) or if the smallest tentative distance among the nodes in the unvisited set is infinity (when planning a complete traversal; occurs when there is no connection between the initial node and remaining unvisited nodes), then stop. The algorithm has finished.
6. Otherwise, select the unvisited node that is marked with the smallest tentative distance, set it as the new "current node", and go back to step 3.

#### Usage
1. Prepare file with graph structure like file graf.txt and use function read_graph_structure_scheme(file.txt) or prepare graph scheme in other format which is able to handle by networkX's add_weighted_edges_from method. [Check how.](https://networkx.github.io/documentation/networkx-1.10/reference/generated/networkx.DiGraph.add_weighted_edges_from.html?highlight=add_weighted_edges_from#networkx.DiGraph.add_weighted_edges_from)
2. Import Dijkstra module.
```python 
from dijkstra_o import Dijkstra
```
3. Create object.
```python
o = Dijkstra()
```
4. Call 'initialization' methods.
```python
o.create_directed_graph()
o.add_weighted_edges(structure_scheme)
```
5. Call shortest path method.
```python 
o.shortest_path(start_point, end_point)
```
## Lab 2/3. Ford-Fulkurson Algorithm
#### Task Description

1. Implement Ford-Fulkerson Algorithm. 
2. Calculate maximum flow between vertices 10 and 60. 
3. Find a target vertex for which the maximum flow from the source s=10 is reached. 

#### Algorithm description 
It is used to model a network flow (e.g., traffic flow, liquid flow, electric current flow etc.).

Pseudocode via [Wikipedia](https://en.wikipedia.org/wiki/Ford%E2%80%93Fulkerson_algorithm):

    Inputs Given a Network G = ( V , E ) {\displaystyle G=(V,E)} G=(V,E) with flow capacity c, a source node s, and a sink node t
    Output Compute a flow f from s to t of maximum value

        f ( u , v ) ← 0 {\displaystyle f(u,v)\leftarrow 0} f(u,v)\leftarrow 0 for all edges ( u , v ) {\displaystyle (u,v)} (u,v)
        While there is a path p from s to t in G f {\displaystyle G_{f}} G_{f}, such that c f ( u , v ) > 0 {\displaystyle c_{f}(u,v)>0} c_{f}(u,v)>0 for all edges ( u , v ) ∈ p {\displaystyle (u,v)\in p} (u,v)\in p:
            Find c f ( p ) = min { c f ( u , v ) : ( u , v ) ∈ p } {\displaystyle c_{f}(p)=\min\{c_{f}(u,v):(u,v)\in p\}} c_{f}(p)=\min\{c_{f}(u,v):(u,v)\in p\}
            For each edge ( u , v ) ∈ p {\displaystyle (u,v)\in p} (u,v)\in p
                f ( u , v ) ← f ( u , v ) + c f ( p ) {\displaystyle f(u,v)\leftarrow f(u,v)+c_{f}(p)} f(u,v)\leftarrow f(u,v)+c_{f}(p) (Send flow along the path)
                f ( v , u ) ← f ( v , u ) − c f ( p ) {\displaystyle f(v,u)\leftarrow f(v,u)-c_{f}(p)} f(v,u)\leftarrow f(v,u)-c_{f}(p) (The flow might be "returned" later)

#### Usage
1. Prepare file with graph structure like file graf.txt and use function read_graph_structure_scheme(file.txt)
2. Import Ford-Fulkerson module and read_graph_structure_scheme from tools.
```python 
from ford_fulkerson import FordFulkerson
from tools import read_graph_structure_scheme
```
3. Read file and prepare scheme.
```python
structure_scheme = read_graph_structure_scheme('graf.txt', '\t')
structure_scheme = np.asarray(structure_scheme)
```
4. Call objects and 'initialization' methods.
```python
o = FordFulkerson()
o.create_graph(structure_scheme)
```
5. Call max_flow method.
```python 
o.max_flow(source, target)
```

## Lab 4. 
[Concurrent matrix multiplication](computer_graphics_algorithm/README.md)