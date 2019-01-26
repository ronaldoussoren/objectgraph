"""
A basic graph library

This package provides a class *ObjectGraph* that
represents a basic graph where nodes are arbitrary
objects with a string-values attribute named "identifier".

Edges between nodes have arbrary (hashable) attributes,
where edges with the same source, destination and attributes
are collapsed into one edge.
"""
__all__ = ("ObjectGraph",)
__version__ = "1.0a0"
from ._objectgraph import ObjectGraph
