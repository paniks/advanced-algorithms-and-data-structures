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