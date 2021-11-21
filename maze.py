from matplotlib.pyplot import plot
import graph 
import render
import coveringtree
import random

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
        #print(str(list_nodes))
        for item in list_nodes:
            self.graph.add_node(item)
        #return mygraph

    def print_graph(self):
        render.draw_square_maze(self.graph, [], False)
        #render.draw_tree(self.graph, False)

    def generate_maze(self):
        parent = coveringtree.prim(self.graph)
        newgraph = graph.Graph()
        newgraph.adjacency = parent
        self.graph = newgraph

    def generate_grid(self, width, height):
        grid = graph.Graph()
        list_nodes = []
        for i in range (height):
            for j in range (width):
                list_nodes.append((j, i))    
        # On defini des poids aleatoires
        for i in range (height):
            for j in range (width):
                #weight = random.uniform(0, 1)
                weight = random.randint(0, 1)
                if not (j, i) in grid.weights:
                    grid.set_arc_weight((j, i), weight)
                    grid.set_arc_weight((i, j), weight)
        # On defini les sommets
        for item in list_nodes:
            grid.add_node(item)
            j, i = item
            neighbours = [(j, i + 1), (j + 1, i), (j, i - 1), (j - 1, i)]
            neighbours_list = []
            for v in neighbours:
                j, i = v
                if j > 0 and j < width and i > 0 and i < height and grid.weights[v] == 0:
                    neighbours_list.append(v)
            grid.adjacency[item] = neighbours_list
        self.graph = grid

        