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


    def shortest_path(self, src: int, dest: int) -> (float, list):
        return self.dijikstra(src,dest)
        
    
    # def TSP(self, node_lst: List[int]) -> (List[int], float):
    #     pass

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

    # def plot_graph(self) -> None:
    #     pass

    
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

                tempWeight=test.NodesMap[nodeTemp].weight+weight
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
   
   