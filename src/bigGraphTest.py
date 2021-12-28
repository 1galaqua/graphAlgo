import unittest
from di_graph import DiGraph 
from graph_algo import GraphAlgo

class DiGraphTest(unittest.TestCase):
    def test_shortestPath(self):
        graph = GraphAlgo()
        test = graph.load_from_json("data/100000.json")
        graph.save_to_json("data/copy1.json")
        

if __name__ == '__main__':
    unittest.main()