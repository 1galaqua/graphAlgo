from GraphAlgoInterface import GraphAlgoInterface
from GraphInterface import GraphInterface
from di_graph import DiGraph
from node_class import Nodes
import json


class GraphAlgo(GraphAlgoInterface):
    
    # constructor
    def __init__(self) -> None:
        GraphAlgoInterface.__init__(self)
        self.diGraph:DiGraph
            
    # return the graph from graphAlgo
    def get_graph(self) -> GraphInterface:
        return self.diGraph
    
    #  read json file to graph
    def load_from_json(self, file_name: str) -> bool:
        self.diGraph= DiGraph()
        f = open(file_name)
        datas = json.load(f)
        for node in datas['Nodes']:
            #split and cast location values
            values = node['pos'].split(",")
            pos = (float(values[0]) , float(values[1]) , float(values[2]))
            
            self.diGraph.add_node(node['id'],pos)
        for edge in datas['Edges']:
            self.diGraph.add_edge(edge['src'],edge['dest'],edge['w'])
        return True
       
    # save the graph to a json file  
    def save_to_json(self, file_name: str) -> bool:
        pass
            
    
    
if __name__ == '__main__':
    pass
    # graph = GraphAlgo()
    # test = graph.load_from_json("./A0.json")
    # print(test)