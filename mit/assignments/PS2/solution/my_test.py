import unittest
from ps2 import load_map
from graph import Node

class GraphTest(unittest.TestCase):
    def test_graph(self):
        self.assertEqual(True, True)

    def test_load_map(self):
        g = load_map('test_load_map.txt')
        self.assertEqual(g.has_node(Node("1")), True)
        self.assertEqual(g.has_node(Node("2")), True)
        self.assertEqual(g.has_node(Node("3")), True)
        self.assertEqual(g.has_node(Node("4")), True)
        self.assertEqual(g.has_node(Node("5")), False)
        print(g.get_edges_for_node(Node("3"))[0])


if __name__ == '__main__':
    unittest.main()
