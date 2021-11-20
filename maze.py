from matplotlib.pyplot import plot
import graph 
import render
import coveringtree

class Maze:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.graph = graph.Graph()

    def generate_graph(self, width, height):
        list_nodes = []
        for i in range (height):
            for j in range (width):
                list_nodes.append((j, i))
            
        print(str(list_nodes))
        for item in list_nodes:
            self.graph.add_node(item)
        #return mygraph

    def print_graph(self):
        render.draw_square_maze(self.graph, [], True)

    def generate_maze(self):
        parent = coveringtree.prim(self.graph, self.graph.adjacency)
        newgraph = graph.Graph()
        self.graph = parent
        #newgraph.adjacency = parent
