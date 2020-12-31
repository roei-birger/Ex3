# Graphs 

***Authors:** Roei Birger & Yaara Barak*

#### Directional weighted graph
In this project we used the infrastructure of a directed weighted graph.<br />
Building the graph's data structurs and algorithms.<br /> 

## Data Structures:

**Node:**<br />
*The node implemented in NodeData object:*<br />
This object represents the set of operations applicable on a  node (vertex) in a (directional) weighted graph.<br />
Each node has a unique id number and location in the graph. <br />
The nodes , the edge into add from the node implemented in a data structure - dictionary.<br />


**Edge:**<br />
The edge represents the set of operations applicable on a directional edge with source and destination nodes in a (directional) weighted graph , the edge not implement by object .<br />
Each edge has a source, destenation nodes and weight.<br />
The edge weight represents the cost of arrival from the source vertex to the destination vertex.<br />
*There is no option to have a negative edge weight and an edge from a vertex to itself.*


**Graph:**<br />
*The GraphInterface interface is implemented in DiGraph:*<br />
 This object represents a directional weighted graph.<br />

 The nodes and edges are implemented in a data structure - dictionary.<br />
 There are functions that are used for: <br />
 Adding / removing nodes and edges<br />
 Obtaining dictionary of nodes and edges(into and from the node)<br />
 Obtaining the amount of nodes/edges that are in the diagram <br />
 Obtaining the amount of actions done on the graph (saved as MC).<br />
  
 **Map:**<br />
  This object represents a support object for the "shortestPath" method,
  at the "shortestPathDist" method the graph is tested to find the shortest
  path between vertexses. Each vertex that is found in this way is preserved
  by this object in order to know which vertex was "his parent"
  on the way and what is the weight of the edge between them.
 
 
 ## Algorithms:
 
 *The GraphAlgoInterface interface is implemented in GraphAlgo:*<br />
 The GraphAlgo object contains a graph to design the algorithms on.
 
 This object represents the Graph Theory algorithms including:
 1. **init** <br />
 2. **get_graph**- Return the DiGraph at the GraphAlgo.init.<br />
 3. **save_to_json**- Saves the graph to a file in JSON format.<br />
 4. **load_from_json**- Loads the graph from a given file in JSON format.<br />
 5. **shortest_path_dist**- Calculates the shortest path distance between 2 given nodes. <br />
 6. **shortest_path** - Finds the shortest path (what path we should choose on which edge) between 2 given nodes in the graph. <br />

להוסיף פה את הקונקטים החדשים///

 7. ???**isConnected** -Checks whither the graph is strongly connected.<br />
 /////////////////////
 
 <br /> 
 
//////add diagram of the python class<br /> 
//////add explane about Dijkstra's algorithm<br /> 
//////add pic about directed weighted graph<br /> 

## **Clone repository**

```
$ git clone https://github.com/roei-birger/Ex3.git
```



