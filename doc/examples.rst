Examples for using objectgraph
------------------------------

A basic node class
..................

.. sourcecode:: python

   import dataclasses

   @dataclasses.dataclass(frozen=True)
   class Node:
      identifier: str


Creating a basic graph
......................

.. sourcecode:: python

   from objectgraph import ObjectGraph

   graph = ObjectGraph()

   # Create some nodes to add to the graph
   node1 = Node("node1")
   node2 = Node("node2")
   node3 = Node("node3")
   node4 = Node("node4")

   # Add the nodes to the graph
   graph.add_node(node1)
   graph.add_node(node2)
   graph.add_node(node3)
   graph.add_node(node4)

   # And select one of them as a graph root
   graph.add_root(node1)

   # Add some edges
   graph.add_edge(node1, node2, None)
   graph.add_edge(node1, node3, None)
   graph.add_edge(node2, node4, None)
   graph.add_edge(node3, node4, None)

   # We now have a basic diamond-shaped graph, with node1 and node4 at the
   # top and bottom, and node2 and node3 in between

Inspecting the graph
....................

.. sourcecode:: python

   # Look for a node:
   n = graph.find_node("node1")
   assert n is node1

   # Print roots:
   print(list(graph.roots()))

   # Print all nodes:
   print(list(graph.nodes()))

   # Print all nodes reachable from a root:
   print(list(graph.iter_graph()))

   # Print all nodes reachable from a node2:
   print(list(graph.iter_graph(node=node2)))

   # Print information on all outgoing edges:
   for edge_data, destination in graph.outgoing(node2):
       print(edge_data, destination)

   # Print information on all incoming edges:
   for edge_data, source in graph.incoming(node2):
       print(edge_data, source)

   # Retrieve edge attributes:
   attributes = graph.edge_data(node1, node2)

Mutating the graph
..................

.. sourcecode:: python

   # Remove a node:
   graph.remove_node(node4)

   # Remove an edge:
   graph.remove_edge(node1, node2, None)
   graph.remove_all_edges(node1, node2)

   # Remove a graph root:
   graph.remove_root(node1)

   # The node is still part of the graph:
   assert node1 in graph
