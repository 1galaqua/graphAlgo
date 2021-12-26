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
    # def dijikstra(self, src:int, dest:int):
    #     test=self.get_graph()
    #     mylist_ver=[]
    #     ans=[]
    #     # src=0
    #     # dest=9
    #     print(src,"-->",dest)
    #     for id,node in test.get_all_v().items():
    #         test.NodesMap[id].tag=0
    #         test.NodesMap[id].weight=100000000
    #         test.NodesMap[id].dist=0
              
    #     test.NodesMap[src].weight=0
    #     test.NodesMap[src].tag=1

    #     mylist_ver.append(test.NodesMap[src].id)
    
    #     test.NodesMap[src].prev=test.NodesMap[src]
    #     while(len(mylist_ver)):
       
    #         nodeTemp=mylist_ver.pop(0)
        
    #             for id,weight in test.NodesMap[nodeTemp].me_to_other.items():
            
    #                 tempWeight=test.NodesMap[nodeTemp].weight+weight
    #                 if (tempWeight<test.NodesMap[id].weight):
    #                     test.NodesMap[id].weight=tempWeight
    #                     test.NodesMap[id].prev=test.NodesMap[nodeTemp].id
    #         if(test.NodesMap[id].tag!=1):    
    #             mylist_ver.insert(len(mylist_ver),id)
                
    #         test.NodesMap[nodeTemp].tag=1
    
    #     boolean=True
    #     ans.append(dest)
    #     tempONlist=dest
    
    #     while(boolean):
            
    #         ans.append(test.NodesMap[tempONlist].prev)
    #         # print(ans)
    #         tempONlist=test.NodesMap[tempONlist].prev
    #         if(tempONlist==src):
            
    #             boolean=False

        
    
    #     final_ans=[]
    #     print(test.NodesMap[dest].weight)
    #     for id in ans:
    #         final_ans.insert(0,id)
        
    #     return (final_ans)
   
   