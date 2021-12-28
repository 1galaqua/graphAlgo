#from _typeshed import Self
import sys
from typing import Dict, List, Tuple
from GraphAlgoInterface import GraphAlgoInterface
from GraphInterface import GraphInterface
from di_graph import DiGraph
from node_class import Nodes
import json
import gui_graph


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
        try:
            f = open(file_name)
            datas = json.load(f)
            for node in datas['Nodes']:
                #split and cast location values
                try:
                    values = node['pos'].split(",")
                    pos = (float(values[0]) , float(values[1]) , float(values[2]))
                except:
                    pos = (None,None,None)
                self.diGraph.add_node(node['id'],pos)
            for edge in datas['Edges']:
                self.diGraph.add_edge(edge['src'],edge['dest'],edge['w'])

            f.close()
            return True
        except:
            return False
       
    # save the graph to a json file  
    def save_to_json(self, file_name: str) -> bool:
        
        if self.get_graph().e_size == 0 or self.get_graph().v_size == 0:
            return False
        else :
            
            # initialize temp List for nodes and edges 
            node_list:List[Nodes] = []
            edges_list:List[Tuple] = []
            dic_graph = {}
            
            # run over the nodes in the graph 
            for id in self.get_graph().get_all_v():
                node_dict = {}
                
                # convert pos from float tuple to string
                curr_pos = self.get_graph().get_all_v()[id][1]
                phrase = str(curr_pos[0])
                phrase+=','
                phrase+=str(curr_pos[1])
                phrase+=','
                phrase+=str(curr_pos[2])
                
                # add the node with his personnal element into the list 
                node_dict["id"] = id
                node_dict["pos"] = phrase
                node_list.append(node_dict)
                
                # run over the edges from the node to those it points to
                for edges in self.get_graph().all_out_edges_of_node(id):
                    edge_dic = {}
                    
                    # add the values to the edges list 
                    edge_dic["src"] = id
                    edge_dic["w"] = self.get_graph().all_out_edges_of_node(id)[edges]
                    edge_dic["dest"] = edges
                    edges_list.append(edge_dic)
                    
            # add the lists to the main dic that represent the entire graph
            dic_graph["Edges"] = edges_list
            dic_graph["Nodes"] = node_list
            
            # write the data into the target file
            try: 
                with open (file_name , 'w') as f:
                    json.dump(dic_graph,f)
                    return True
            except:
                return False
  
    def shortest_path(self, src: int, dest: int) -> (float, list):
        return self.dijikstra(src,dest)

    def centerPoint(self) -> (int, float):

        centerPoint=0
        weight=10000000
        tempList=[]
        tempOption=[]
        tempans=[-1,-1]
        for src,node1 in self.diGraph.get_all_v().items():
            nodeOne=0
            
            for dest,node in self.diGraph.get_all_v().items():
                
                if(src!=dest):
                    temp2=self.dijikstra(src,dest)
                    nodeOne=(src,dest,temp2[1]) 
                    tempList.append(nodeOne)
                   
            max=-1
            centerOption=(0,0,0)
            for checknode in tempList:
                
                if(checknode[2]>max):
                    max=checknode[2]
                    centerOption=checknode
            tempOption.append(centerOption) 
            
            tempList.clear()
        finalans=[]
        min=10000000
        for option in tempOption:
            if(option[2]<min):
                min=option[2]
                finalans=option
            
        tempans=[finalans[0],finalans[2]]     
        
        return(tempans)

     def dijikstra(self, src:int, dest:int):
        test=self.diGraph
        mylist_ver=[]
        ans=[]
       
        
        for id,node in test.get_all_v().items():
            test.NodesMap[id].tag=0
            test.NodesMap[id].weight=100000000
            test.NodesMap[id].dist=0
              
        test.NodesMap[src].weight=0
        test.NodesMap[src].tag=1

        mylist_ver.append(test.NodesMap[src].id)
    
        test.NodesMap[src].prev=test.NodesMap[src]
        while(len(mylist_ver)):
        
            nodeTemp=mylist_ver.pop(0)

            for id,weight in test.NodesMap[nodeTemp].me_to_other.items():

                tempWeight=test.NodesMap[nodeTemp].weight+weight[1]
                if (tempWeight<test.NodesMap[id].weight):
                    test.NodesMap[id].weight=tempWeight
                    test.NodesMap[id].prev=test.NodesMap[nodeTemp].id
                if(test.NodesMap[id].tag!=1):    
                    mylist_ver.insert(len(mylist_ver),id)

            test.NodesMap[nodeTemp].tag=1

        boolean=True
        ans.append(dest)
        tempONlist=dest

        while(boolean):

            ans.append(test.NodesMap[tempONlist].prev)
           
            tempONlist=test.NodesMap[tempONlist].prev
            if(tempONlist==src):

                boolean=False


        ans.reverse()
        

        return(ans,test.NodesMap[dest].weight)

    def plot_graph(self) -> None:
        gui_graph.main(self.get_graph())


if __name__ == '__main__':
    
    graph = GraphAlgo()
    test = graph.load_from_json("data/T0.json")
    graph.plot_graph()