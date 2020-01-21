Introduction
------------

Objectgraph is a library that provides a class representing
basic graphs with nodes and edges between nodes.

Nodes can be arbitrary objects with an "identifier" attribute
(which should be hashable). Edges can have arbitrary attributes.

The model for edges is slighly non-standard: There can be multiple
edges between nodes, but all edges with the same attributes are
collapsed into one edge.

There is `documentation at readthedocs <https://objectgraph.readthedocs.io>`_

CI Status
.........

.. image:: https://github.com/ronaldoussoren/objectgraph/workflows/Lint/badge.svg
.. image:: https://github.com/ronaldoussoren/objectgraph/workflows/Lint/badge.svg

Historic
........

Objectgraph is a complete rewrite of the ObjectGraph class in
`altgraph <https://pypi.org/project/altgraph/>`_,
using lessons learned in that project but with a complete new
Python 3 code base and full test coverage.
