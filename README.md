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


## Dijkstra's algorithm

#### Description
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
