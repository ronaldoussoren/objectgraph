"""
A basic graph datastructure
"""
from typing import (
    Dict,
    Generic,
    Hashable,
    Iterator,
    Optional,
    Set,
    Tuple,
    TypeVar,
    Union,
)

from typing_extensions import Protocol


class GraphNode(Protocol):
    @property
    def identifier(self) -> str:
        ...  # pragma: nocover


# The graph is generic for the types of nodes and edges,
# mostly to make it easier to type-check code using the graph.
NODE_TYPE = TypeVar("NODE_TYPE", bound=GraphNode)
EDGE_TYPE = TypeVar("EDGE_TYPE", bound=Hashable)


class ObjectGraph(Generic[NODE_TYPE, EDGE_TYPE]):
    """
    A basic graph datastructure where the nodes can be arbitrary objects
    with an attribute named "identifier". Edges between nodes can have
    associated data.

    There can be multiple edges between nodes, but all edges with the
    same attributes are collapsed into one edge.

    For `Mypy <https://mypy.readthedocs.io/en/latest/index.html>`_ users
    this is a generic class with two type parameters:

    * The node type

      An arbitrary that that has an string-valued attribute named "identifier"

    * The edge type

      An arbirary type that is hashable.
    """

    def __init__(self):
        """
        Create a new empty graph
        """
        self._roots: Set[str] = set()
        self._nodes: Dict[str, NODE_TYPE] = {}
        self._edges: Dict[Tuple[str, str], Set[EDGE_TYPE]] = {}

    def __repr__(self):
        return f"<{type(self).__name__} with {len(self._roots)} roots, {len(self._nodes)} nodes and {len(self._edges)} edges>"  # noqa:E501, B950

    def roots(self) -> Iterator[NODE_TYPE]:
        """
        Yield the roots of the graph in an arbirary order.
        """
        return (self._nodes[identifier] for identifier in self._roots)

    def nodes(self) -> Iterator[NODE_TYPE]:
        """
        Yield all nodes in the graph in an arbirary order.
        """
        return iter(self._nodes.values())

    def edges(self) -> Iterator[Tuple[NODE_TYPE, NODE_TYPE, Set[EDGE_TYPE]]]:
        """
        Yield the source and destination of all edges in the graph with a
        set of all unique edge attributes for edges between the two nodes.
        """
        for from_id, to_id in self._edges:
            yield self._nodes[from_id], self._nodes[to_id], self._edges[
                (from_id, to_id)
            ]

    def add_root(self, node: Union[str, NODE_TYPE]) -> None:
        """
        Add a root to the graph

        Args:
          node: A node or name of a node.

        Raises:
          KeyError: if the node is not part of the graph
        """
        value = self.find_node(node)
        if value is None:
            raise KeyError("Adding non-existing {node!r} as root")

        self._roots.add(value.identifier)

    def add_node(self, node: NODE_TYPE) -> None:
        """
        Add a root to the graph

        Args:
          node: A node
        """
        if node.identifier in self._nodes:
            raise ValueError(f"Already have node with name {node.identifier!r}")

        self._nodes[node.identifier] = node

    def add_edge(
        self,
        source: Union[str, NODE_TYPE],
        destination: Union[str, NODE_TYPE],
        edge_attributes: EDGE_TYPE,
    ) -> None:
        """
        Add a directed edge between *source* and *destination* with edge
        attributes. Edges between the *source* and *destination* with the
        same edge attributes are merged into a single edge.

        Args:
          source: A node or node identifier
          destination: A node or node identifier
          edge_attributes: Attributes for the edge, must be hashable

        Raises:
          KeyError: If the source or destination are not nodes in the graph
        """
        from_node = self.find_node(source)
        to_node = self.find_node(destination)
        if from_node is None:
            raise KeyError(f"Source {source!r} not found")
        if to_node is None:
            raise KeyError(f"Destination {destination!r} not found")

        key = (from_node.identifier, to_node.identifier)
        if key in self._edges:
            self._edges[key].add(edge_attributes)

        else:
            self._edges[key] = {edge_attributes}

    def remove_root(self, node: Union[str, NODE_TYPE]) -> None:
        """
        Removes one of the graph roots, without removing
        the node from the graph.

        Args:
          node: A node or node identifier

        Raises:
          KeyError: if the node is not a root of the graph
        """
        if isinstance(node, str):
            self._roots.remove(node)

        else:
            self._roots.remove(node.identifier)

    def remove_node(self, node: Union[str, NODE_TYPE]) -> None:
        """
        Removes a node and related information from the graph.

        Args:
          node: The node or node identifier to remove

        Raises:
           KeyError: If the node is not part of the graph
        """
        node_id: str

        if isinstance(node, str):
            node_id = node

        else:
            node_id = node.identifier

        if node_id not in self._nodes:
            raise KeyError(node_id)

        if node_id in self._roots:
            self._roots.remove(node_id)

        to_remove = []
        for source, destination in self._edges:
            if source == node_id or destination == node_id:
                to_remove.append((source, destination))

        for item in to_remove:
            del self._edges[item]

        del self._nodes[node_id]

    def remove_edge(
        self,
        source: Union[str, NODE_TYPE],
        destination: Union[str, NODE_TYPE],
        edge_attributes: EDGE_TYPE,
    ) -> None:
        """
        Remove an edge from the graph

        Args:
          source: a node or node identifier
          destination: a node or node identifier
          edge_attributes: attributes of the edge that should be removed

        Raises:
          KeyError: If the source of destination are not found
          KeyError: If there is no edge between source and destination
                    with the specified attributes
        """
        from_node = self.find_node(source)
        to_node = self.find_node(destination)
        if from_node is None:
            raise KeyError("Source {source!r} not found")
        if to_node is None:
            raise KeyError("Destination {destination!r} not found")

        key = (from_node.identifier, to_node.identifier)

        try:
            self._edges[key].remove(edge_attributes)

        except KeyError:
            raise KeyError(
                f"There is no edge between {from_node.identifier} and {to_node.identifier} with attributes {edge_attributes!r}"  # noqa:E501, B950
            ) from None

    def remove_all_edges(
        self, source: Union[str, NODE_TYPE], destination: Union[str, NODE_TYPE]
    ):
        """
        Remove all edges between *source* and *destination*.

        Args:
          source: a node or node identifier
          destination: a node or node identifier

        Raises:
          KeyError: If the source of destination are not found
        """
        from_node = self.find_node(source)
        to_node = self.find_node(destination)
        if from_node is None:
            raise KeyError("Source {source!r} not found")
        if to_node is None:
            raise KeyError("Destination {destination!r} not found")

        key = (from_node.identifier, to_node.identifier)

        try:
            del self._edges[key]

        except KeyError:
            raise KeyError(
                f"There is no edge between {from_node.identifier} and {to_node.identifier}"  # noqa:E501, B950
            ) from None

    def find_node(self, node: Union[str, NODE_TYPE]) -> Optional[NODE_TYPE]:
        """
        Find a node in the graph. If the argument is a node object
        this looks for a graph member with the same *identifier*.

        Args:
          node: A node or node identifier

        Returns:
          The node found, or :data:`None` when the node is not present
        """
        if isinstance(node, str):
            return self._nodes.get(node)

        else:
            return self._nodes.get(node.identifier)

    def __contains__(self, node: Union[str, NODE_TYPE]):
        """
        Check if a node is a member of the graph

        Args:
          node: The node or node identifier to look for

        Returns:
          True if the node is part of the graph, False otherwise
        """
        return self.find_node(node) is not None

    def edge_data(
        self, source: Union[str, NODE_TYPE], destination: Union[str, NODE_TYPE]
    ) -> Set[EDGE_TYPE]:
        """
        Return the all edge attributes for edges between *source* and *destination*.

        Args:
          source: A node or node identifier
          destination: A node or node identifier

        Returns:
          A set of edge attributes for all edges between *source* and *destination*

        Raises:
          KeyError: If *source* or *destination* aren't member of the graph
          KeyError: If there is no edge between *source* and *destination*
        """
        from_node = self.find_node(source)
        to_node = self.find_node(destination)
        if from_node is None:
            raise KeyError("Source {source!r} not found")
        if to_node is None:
            raise KeyError("Destination {destination!r} not found")

        try:
            return self._edges[(from_node.identifier, to_node.identifier)]
        except KeyError:
            raise KeyError(
                f"There is no edge between {from_node.identifier} and {to_node.identifier}"  # noqa:E501, B950
            ) from None

    def outgoing(
        self, source: Union[str, NODE_TYPE]
    ) -> Iterator[Tuple[Set[EDGE_TYPE], NODE_TYPE]]:
        """
        Yield (edge, node) for all outgoing edges

        Args:
          source: A node or node identifier
        """
        node = self.find_node(source)
        if node is None:
            return

        for from_node, to_node in self._edges:
            if from_node == node.identifier:
                yield self._edges[(from_node, to_node)], self._nodes[to_node]

    def incoming(
        self, destination: Union[str, NODE_TYPE]
    ) -> Iterator[Tuple[Set[EDGE_TYPE], NODE_TYPE]]:
        """
        Yield (edge, node) for all incoming edges

        Args:
          destination: A node or node identifier
        """
        node = self.find_node(destination)
        if node is None:
            return

        for from_node, to_node in self._edges:
            if to_node == node.identifier:
                yield self._edges[(from_node, to_node)], self._nodes[from_node]

    def iter_graph(
        self, *, node: Union[str, NODE_TYPE] = None, _visited: Optional[set] = None
    ) -> Iterator[NODE_TYPE]:
        """
        Yield all nodes in the graph reachable from *node*
        or any of the graph roots.

        Args:
          node: The node or node identifier used to start iterating. Defaults
                to using the graph roots.
        """
        if _visited is None:
            _visited = set()

        if node is None:
            for node in self._roots:
                yield from self.iter_graph(node=node, _visited=_visited)

        else:
            start_node = self.find_node(node)
            if start_node is None:
                raise KeyError(f"Start node {node!r} not found")

            if start_node.identifier in _visited:
                return

            _visited.add(start_node.identifier)
            yield start_node

            for _, node in self.outgoing(start_node):
                yield from self.iter_graph(node=node, _visited=_visited)
