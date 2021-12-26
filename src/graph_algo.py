#from _typeshed import Self
import sys
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
    # def save_to_json(self, file_name: str) -> bool:
    #     pass


    # def shortest_path(self, id1: int, id2: int) -> (float, list):
    #     pass
    
    # def TSP(self, node_lst: List[int]) -> (List[int], float):
    #     pass

    # def centerPoint(self) -> (int, float):
    #     pass

    # def plot_graph(self) -> None:
    #     pass

    # function Dijkstra(Graph, source):

    # create vertex set Q

    # for each vertex v in Graph:             // Initialization
    #     dist[v] ← INFINITY                  // Unknown distance from source to v
    #     prev[v] ← UNDEFINED                 // Previous node in optimal path from source
    #     add v to Q                          // All nodes initially in Q (unvisited nodes)

    # dist[source] ← 0                        // Distance from source to source
    
    # while Q is not empty:
    #     u ← vertex in Q with min dist[u]    // Node with the least distance will be selected first
    #     remove u from Q 
        
    #     for each neighbor v of u:           // where v is still in Q.
    #         alt ← dist[u] + length(u, v)
    #         if alt < dist[v]:               // A shorter path to v has been found
    #             dist[v] ← alt 
    #             prev[v] ← u 

    # return dist[], prev[]
    def dijikstra(self, src:int, dest:int)->list:
        list_ver=[]
        ans=[]
        # Self.load_from_json("A0.json")
        test = self.get_graph()
        
        for id,node in test.get_all_v().items():
            node.tag=0
            node.weight=sys.float_info.max
            node.dist=0
                
        self.diGraph.NodesMap[src].weight=0
        list_ver.append(id)
        while(len(list_ver)):
            nodeTemp=list_ver.pop
            for id,weight in self.diGraph.NodesMap[nodeTemp].me_to_other.items():
                self.diGraph.NodesMap[nodeTemp].tag=1
                tempWeight=self.diGraph.NodesMap[nodeTemp].weight+weight
                if (tempWeight<self.diGraph.NodesMap[id].weight):
                    self.diGraph.NodesMap[id].weight=tempWeight
                    self.diGraph.NodesMap[id].prev=nodeTemp
                    if(self.diGraph.NodesMap[id]!=1):    
                     list_ver.append(id)

        boolean=True
        ans.append(self.diGraph.NodesMap[dest].prev)
        tempONlist=self.diGraph.NodesMap[dest].prev
        while(boolean):
            
            ans.append(self.diGraph.NodesMap[tempONlist].prev)
            tempONlist=self.diGraph.NodesMap[tempONlist].prev
            if(tempONlist==src):
                boolean=False

        return ans
   
   