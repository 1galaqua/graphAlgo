from types import MappingProxyType
import pygame
from pygame.constants import DOUBLEBUF, HWSURFACE, RESIZABLE, VIDEORESIZE
from di_graph import DiGraph
from graph_algo import GraphAlgo
import os
import sys
from node_class import Nodes

from node_class import Nodes

#values of the window
WIDTH , HEIGHT = 900 , 500

# display the main window
WIN = pygame.display.set_mode((WIDTH,HEIGHT) , HWSURFACE | DOUBLEBUF | RESIZABLE)

#the coordinate corners of the window
# global MAXx ,MINx ,MAXy , MINy
MAXx = sys.float_info.min
MAXy = sys.float_info.min
MINy = sys.float_info.max
MINx = sys.float_info.max

#colors
WHITE = (255, 255, 255)
BLUE = (0 , 0 , 255)
GREY = (128,128,128)
BLACK = (0 , 0 , 0)

# title of the graph
pygame.display.set_caption("Graph Display")


#find the good ratio
def findRatio(graph:DiGraph):
    listNode = graph.get_all_v()
    node:Nodes
    global MINx , MINy , MAXx , MAXy

    for node in listNode.values():
        if node.pos[0] < MINx:
            # global MINx
            MINx = node.pos[0]
        if node.pos[0] > MAXx:
            # global MAXx
            MAXx = node.pos[0]
        if node.pos[1] < MINy:
            # global MINy
            MINy = node.pos[1]
        if node.pos[1] > MAXy:
            # global MAXy 
            MAXy = node.pos[1]
    


# window drawer
def draw_window():
    WIN.fill(WHITE)
    
    # print a graph 
    graph = GraphAlgo()
    graph.load_from_json("data/A3.json")
    node_map = GraphAlgo.get_graph(graph)
    findRatio(node_map)
    # print(MAXx,MAXy,MINx,MINy)
    repereX = (MAXx - MINx)
    repereY = (MAXy - MINy)
    # print(repereX,repereY)
    node:Nodes
    for id , node in node_map.get_all_v().items():
        point = pygame.draw.circle(WIN , BLACK ,  ( ( MAXx+0.001 -node.pos[0])*(WIDTH / (repereX*1.2)) , ( MAXy+0.001 -node.pos[1])*(HEIGHT/ (repereY*1.2) ) ) , 10 , 0)
        for id in node.me_to_other:
            curr:Nodes
            curr = node_map.get_all_v().get(id)
            line = pygame.draw.line(WIN , BLUE ,  ( ( MAXx+0.001 -node.pos[0])*(WIDTH / (repereX*1.2)) , ( MAXy+0.001 -node.pos[1])*(HEIGHT/ (repereY*1.2) ) ) , ( ( MAXx+0.001 -curr.pos[0])*(WIDTH / (repereX*1.2)) , ( MAXy+0.001 -curr.pos[1])*(HEIGHT/ (repereY*1.2) ) ) , 2 )
            arrow = pygame.draw.polygon(WIN , BLUE , ( ( MAXx+0.001 -curr.pos[0])*(WIDTH / (repereX*1.2)) , ( MAXy+0.001 -curr.pos[1])*(HEIGHT/ (repereY*1.2) ) ) , ( ( MAXx+0.001 -curr.pos[0]-0.0001)*(WIDTH / (repereX*1.2)) , ( MAXy+0.001 -curr.pos[1]-0.0001)*(HEIGHT/ (repereY*1.2) ) ) , ( ( MAXx+0.001 -curr.pos[0]-0.0001)*(WIDTH / (repereX*1.2)) , ( MAXy+0.001 -curr.pos[1]+0.0001)*(HEIGHT/ (repereY*1.2) ) ) , 0)

    pygame.display.update()

    


def main():
    run = True
    while run:

        for event in pygame.event.get():
            # allow to quit the GUI
            if event.type == pygame.QUIT:
                run = False
            # allow to resize the screen
            elif event.type == VIDEORESIZE:
                screen  = pygame.display.set_mode(event.dict['size'] , HWSURFACE | DOUBLEBUF | RESIZABLE)

        
        draw_window()
        
    pygame.quit()


if __name__ == "__main__":
    main()

