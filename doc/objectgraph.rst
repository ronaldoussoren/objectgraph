objectgraph - Reference documentation
=====================================

.. automodule:: objectgraph

Graph
.....

.. autoclass:: objectgraph.ObjectGraph

Creating and updating a graph
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. automethod:: objectgraph.ObjectGraph.__init__

.. automethod:: objectgraph.ObjectGraph.add_node

.. automethod:: objectgraph.ObjectGraph.add_root

.. automethod:: objectgraph.ObjectGraph.add_edge

.. automethod:: objectgraph.ObjectGraph.remove_edge

.. automethod:: objectgraph.ObjectGraph.remove_all_edges

.. automethod:: objectgraph.ObjectGraph.remove_root

.. automethod:: objectgraph.ObjectGraph.remove_node

Reporting on a graph
~~~~~~~~~~~~~~~~~~~~

.. automethod:: objectgraph.ObjectGraph.find_node

.. automethod:: objectgraph.ObjectGraph.__contains__

.. automethod:: objectgraph.ObjectGraph.edge_data

.. automethod:: objectgraph.ObjectGraph.roots

.. automethod:: objectgraph.ObjectGraph.nodes

.. automethod:: objectgraph.ObjectGraph.iter_graph

.. automethod:: objectgraph.ObjectGraph.edges

.. automethod:: objectgraph.ObjectGraph.incoming

.. automethod:: objectgraph.ObjectGraph.outgoing

Mypy support
~~~~~~~~~~~~

.. data:: objectgraph.NODE_TYPE

   This a type variable representing
   the interface for nodes: Nodes should have an
   string-valued attribute named "identifier".

.. data:: objectgraph.EDGE_TYPE

   This type is a type variable representing
   the interface for edges: Edges should be
   hashable.
