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

Historic
........

Objectgraph is a complete rewrite of the ObjectGraph class in
`altgraph <https://pypi.org/project/altgraph/>`_,
using lessons learned in that project but with a complete new
Python 3 code base and full test coverage.


|pypi-version| |test-badge| |lint-badge| |docs-badge|

.. |pypi-version| image:: https://img.shields.io/pypi/v/objectgraph.svg
   :target: https://pypi.org/project/objectgraph

.. |test-badge| image:: https://github.com/ronaldoussoren/modulegraph2/actions/workflows/test.yml/badge.svg
   :target: https://github.com/ronaldoussoren/objectgraph/actions/workflows/test.yml

.. |lint-badge| image:: https://github.com/ronaldoussoren/modulegraph2/actions/workflows/lint.yml/badge.svg
   :target: https://github.com/ronaldoussoren/objectgraph/actions/workflows/lint.yml

.. |docs-badge| image:: https://img.shields.io/readthedocs/objectgraph/latest.svg
   :target: https://objectgraph.pypa.io
