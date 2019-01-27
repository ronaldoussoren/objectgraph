import unittest

import objectgraph

PUBLIC_SYMBOLS = {"ObjectGraph", "NODE_TYPE", "EDGE_TYPE"}

PYTHON_SYMBOLS = {
    "__loader__",
    "__doc__",
    "__file__",
    "__builtins__",
    "__spec__",
    "__all__",
    "__name__",
    "__path__",
    "__package__",
    "__cached__",
    "__version__",
}


def submodules(module):
    for nm in dir(module):
        if nm.startswith("_") and isinstance(getattr(module, nm), type(module)):
            yield nm


class TestAPI(unittest.TestCase):
    def test_package_symbols(self):
        self.assertEqual(PUBLIC_SYMBOLS, set(objectgraph.__all__))
        self.assertEqual(
            PUBLIC_SYMBOLS,
            set(objectgraph.__dict__.keys())
            - PYTHON_SYMBOLS
            - set(submodules(objectgraph)),
        )

    def test_all(self):
        for nm in objectgraph.__all__:
            getattr(objectgraph, nm)
