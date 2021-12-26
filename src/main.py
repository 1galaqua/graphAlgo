import sys
from GraphAlgoInterface import GraphAlgoInterface
from di_graph import DiGraph
from graph_algo import GraphAlgo
from node_class import Nodes




def check():
    """
    Graph: |V|=4 , |E|=5
    {0: 0: |edges out| 1 |edges in| 1, 1: 1: |edges out| 3 |edges in| 1, 2: 2: |edges out| 1 |edges in| 1, 3: 3: |edges out| 0 |edges in| 2}
    {0: 1}
    {0: 1.1, 2: 1.3, 3: 10}
    (3.4, [0, 1, 2, 3])
    (2.8, [0, 1, 3])
    (inf, [])
    2.062180280059253 [1, 10, 7]
    17.693921758901507 [47, 46, 44, 43, 42, 41, 40, 39, 15, 16, 17, 18, 19]
    11.51061380461898 [20, 21, 32, 31, 30, 29, 14, 13, 3, 2]
    inf []
    (7, 6.806805834715163)
    ([1,3,4,2],3.5)
    """
    check0()
    check1()
    check2()


def check0():
    """
    This function tests the naming (main methods of the DiGraph class, as defined in GraphInterface.
    :return:
    """
    g = DiGraph()  # creates an empty directed graph
    for n in range(4):
        g.add_node(n)
    g.add_edge(0, 1, 1)
    g.add_edge(1, 0, 1.1)
    g.add_edge(1, 2, 1.3)
    g.add_edge(2, 3, 1.1)
    g.add_edge(1, 3, 1.9)
    g.remove_edge(1, 3)
    g.add_edge(1, 3, 10)
    print(g)  # prints the __repr__ (func output)
    print(g.get_all_v())  # prints a dict with all the graph's vertices.
    print(g.all_in_edges_of_node(1))
    print(g.all_out_edges_of_node(1))
    g_algo = GraphAlgo(g)
    print(g_algo.shortest_path(0, 3))
    g_algo.plot_graph()


def check1():
    """
       This function tests the naming (main methods of the GraphAlgo class, as defined in GraphAlgoInterface.
    :return:
    """
    g_algo = GraphAlgo()  # init an empty graph - for the GraphAlgo
    file = "../data/T0.json"
    g_algo.load_from_json(file)  # init a GraphAlgo from a json file
    print(g_algo.shortest_path(0, 3))
    print(g_algo.shortest_path(3, 1))
    print(g_algo.centerPoint())
    g_algo.save_to_json(file + '_saved')
    g_algo.plot_graph()


def check2():
    """ This function tests the naming, basic testing over A5 json file.
      :return:
      """
    g_algo = GraphAlgo()
    file = '../data/A5.json'
    g_algo.load_from_json(file)
    g_algo.get_graph().remove_edge(13, 14)
    g_algo.save_to_json(file + "_edited")
    dist, path = g_algo.shortest_path(1, 7)
    print(dist, path)
    dist, path = g_algo.shortest_path(47, 19)
    print(dist, path)
    dist, path = g_algo.shortest_path(20, 2)
    print(dist, path)
    dist, path = g_algo.shortest_path(2, 20)
    print(dist, path)
    print(g_algo.TSP([1, 2, 3]))
    g_algo.plot_graph()


def check3():
    """ This function tests the naming, basic testing over A5 json file.
      :return:
      """
    g = DiGraph()  # creates an empty directed graph
    for n in range(5):
        g.add_node(n)
    g.add_edge(0, 1, 1)
    g.add_edge(0, 4, 5)
    g.add_edge(1, 0, 1.1)
    g.add_edge(1, 2, 1.3)
    g.add_edge(1, 3, 1.9)
    g.add_edge(2, 3, 1.1)
    g.add_edge(3, 4, 2.1)
    g.add_edge(4, 2, .5)
    g_algo = GraphAlgo(g)
    print(g_algo.centerPoint())
    print(g_algo.TSP([1, 2, 4]))
    g_algo.plot_graph()


   


if __name__ == '__main__':
    # check()
    graph = GraphAlgo()
    graph.load_from_json("A0.json")
    test = GraphAlgo.get_graph(graph)
    node:Nodes
    # for id,node in test.get_all_v().items():
    #     # print(node,"<---")
    #     # print(test.all_in_edges_of_node(node))
    #     # print("-------------------")
    #     # print(node , "--->")
    #     # print(test.all_out_edges_of_node(node))
    #     print(node.tag)
    #     print(node.pos,"-----", node.weight)
    # mylist=[]
    # print("--------empty--------")
    # if  len(mylist):
    #     print("not empty_list")
    # else:
    #     print(" empty")
    # print("-------2-not empty--------")
    # mylist2=["gal","tamar"]
    # if len(mylist2):
    #     print("full_list")
    # else:
    #     print(" empty")
    
    # print(test.NodesMap[2].pos)
    # print("")
    tamarlist=["batata",5,"matzika"]
    (tamarlist.append("hi"))
    print(tamarlist.pop(1))
    print(tamarlist.pop(1))
    # print(graph.dijikstra(2,5))
    print("")
    print(test.NodesMap[2].me_to_other)
    mylist_ver=[]
    ans=[]
    src=2
    dest=5
    i=0
    for id,node in test.get_all_v().items():
        test.NodesMap[id].tag=0
        test.NodesMap[id].weight=10000000
        test.NodesMap[id].dist=0
        i=i+1
        print(test.NodesMap[id].weight ,"--",i)        
    test.NodesMap[src].weight=0
    test.NodesMap[src].tag=1
    print("src weight:",test.NodesMap[src].weight)
    print("src tag:",test.NodesMap[src].tag)
    mylist_ver.append(test.NodesMap[src].id)
    test.NodesMap[src].prev=test.NodesMap[src]
    while(len(mylist_ver)):
        print(mylist_ver)
        nodeTemp=mylist_ver.pop(0)
        print(nodeTemp)
        for id,weight in test.NodesMap[nodeTemp].me_to_other.items():
            test.NodesMap[nodeTemp].tag=1
            tempWeight=test.NodesMap[nodeTemp].weight+weight
            if (tempWeight<test.NodesMap[id].weight):
                test.NodesMap[id].weight=tempWeight
                test.NodesMap[id].prev=test.NodesMap[nodeTemp].id
            if(test.NodesMap[id].tag!=1):    
                mylist_ver.insert(len(mylist_ver),id)

    boolean=True
    ans.append(test.NodesMap[dest].prev)
    tempONlist=test.NodesMap[dest].prev
    print(ans)
    while(boolean):
            
        ans.append(test.NodesMap[tempONlist].prev)
       # print(ans)
        tempONlist=test.NodesMap[tempONlist].prev
        if(tempONlist==src):
            boolean=False

        
    for id,weight in test.NodesMap[2].me_to_other.items():
        print(weight)

    print(ans,test.NodesMap[dest].weight)
    


