from typing import Dict
from GraphInterface import GraphInterface
from node_class import Nodes
import __future__


class DiGraph(GraphInterface):
    
    # constructor
    def __init__(self) -> None:
        GraphInterface.__init__(self)
        self.NodesMap:Dict[int,Nodes] = {}
        self.nbrNodes = 0
        self.nbrEdges = 0
        self.mc = 0
           
    # return number of vertices in the graph
    def v_size(self) -> int:
        return self.nbrNodes
    
    
    # return the numbers of edges in the graph
    def e_size(self) -> int:
        return self.nbrEdges
    
    
    # return a dictionnary of all the nodes in the graph
    def get_all_v(self) -> dict:
        return self.NodesMap
    
    
    # return à dictionnary of all the edges to the node
    def all_in_edges_of_node(self, id1: int) -> dict:
        node = self.NodesMap[id1]
        return node.other_to_me
        
    
    # return a dictionnary of all the edges from the node
    def all_out_edges_of_node(self, id1: int) -> dict:
        node = self.NodesMap[id1]
        return node.me_to_other
    
    # return the number of modification made on the graph  
    def get_mc(self) -> int:
        return self.mc
    
    # add edge to the graph
    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if id1 in self.NodesMap and id2 in self.NodesMap:
            edge = (id1 , id2 , weight)
            node1 = self.NodesMap[id1]
            node2 = self.NodesMap[id2]
            node2.other_to_me[id1] = weight
            node1.me_to_other[id2] = weight
            self.nbrEdges+=1
            self.mc+=1
            return True
        else:
            return False
        
    # add node to the graph    
    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if node_id in self.NodesMap:
            return False
        else:
            node = Nodes(node_id, pos)
            self.NodesMap[node_id] = node
            self.nbrNodes+=1
            self.mc+=1
            return True
        
    # remove node from the graph    
    # def remove_node(self, node_id: int) -> bool:
    #     if node_id in self.NodesMap:
    #         for key in self.NodesMap:
    #             node = self.NodesMap[key]
    #             if node_id in node.other_to_me:
    #                 node.other_to_me.pop(node_id)
    #                 self.nbrEdges-=1
    #             if node_id in node.me_to_other:
    #                 node.me_to_other.pop(node_id)
    #                 self.nbrEdges-=1
    #         self.NodesMap.pop(node_id)
    #         self.nbrNodes-=1
    #         self.mc+=1
    #         return True
    #     else:
    #         return False
    
    def remove_node(self , node_id: int ) ->bool:
        if node_id in self.NodesMap:
            node = self.NodesMap[node_id]
            for key in node.other_to_me:
                curr = self.NodesMap[key]
                curr.me_to_other.pop(node_id)
                self.nbrEdges-=1
            for key in node.me_to_other:
                curr = self.NodesMap[key]
                curr.other_to_me.pop(node_id)
                self.nbrEdges-=1
            self.NodesMap.pop(node_id)
            self.nbrNodes-=1
            self.mc+=1
            return True
        else:
            return False
                
                
    
    #remove edge from the graph
    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        node1 = self.NodesMap[node_id1]
        if node_id2 in node1.me_to_other:
            node1.me_to_other.pop(node_id2)
            self.nbrEdges-=1
            self.mc+=1
            return True
        else:
            return False
            
    

if __name__ == '__main__':
    g = DiGraph()
    pos1 = (1,2,0)
    pos2 = (1,1,0)
    pos3 = (2,1,0)
    pos4 = (2,2,0)
    
    # node1 = Nodes(1, pos1)
    # node2 = Nodes(2, pos2)
    # node3 = Nodes(3, pos3)
    
    g.add_node(1,pos1)
    g.add_node(2,pos2)
    g.add_node(3,pos3)
    g.add_node(4,pos4)
    
    g.add_edge(1, 2, 1)
    g.add_edge(2, 1, 1)
    g.add_edge(2, 3, 1)
    g.add_edge(3, 1, 1)
    g.add_edge(4, 2, 1)
    g.add_edge(3, 4, 1)
    g.add_edge(3, 2 ,2)
    
    print(g.nbrEdges,g.nbrNodes)
    g.remove_node(2)
    
    print(g.nbrEdges,g.nbrNodes)
    print(g.NodesMap[3].me_to_other)
    print(g.NodesMap[4].other_to_me)
    print(g.NodesMap[4].me_to_other)