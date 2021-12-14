from matplotlib.pyplot import plot
import graph_noset as graph 
import render
import coveringtree_noset as coveringtree
import random

class Maze:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.graph = self.generate_graph(width, height)
        self.solution = []

    def generate_graph(self, width, height):
        list_nodes = []
        newgraph = graph.Graph()
        for j in range (width):
            for i in range (height):
                list_nodes.append((j, i))    
        for node in list_nodes:
            newgraph.add_node(node)
            j, i = node

            if j - 1 >= 0:
                newgraph.add_arc((node, (j - 1, i)))
                newgraph.add_arc(((j - 1, i), node))
            if i - 1 >= 0:
                newgraph.add_arc((node, (j, i - 1)))
                newgraph.add_arc(((j, i - 1), node))
        return newgraph

    def print_graph(self):
        render.draw_square_maze(self.graph, self.solution, False)

    def generate_maze(self):
        parent = coveringtree.prim(self.graph)
        newgraph = self.generate_graph(self.width, self.height)
        newgraph.adjacency = {}
        for node in parent:
            if parent[node] != []:
                newgraph.add_arc((node, parent[node][0]))
                newgraph.add_arc((parent[node][0], node))         
        self.graph = newgraph

    def generate_random(self):
        grid = graph.Graph()
        for i in range (self.height):
            for j in range (self.width):
                neighbours = [(j, i + 1), (j + 1, i), (j, i - 1), (j - 1, i)]
                for neighbour in neighbours:
                    x, y = neighbour
                    if self.width -1 >= x >= 0 and self.height - 1 >= y >= 0:
                        node = (j, i)
                        weight = random.randint(0, 1)
                        grid.add_weighted_arc((node,neighbour), weight)
                        grid.add_weighted_arc((neighbour,node), weight)
        self.graph = grid

    def prim_resolver(self):
        parent = coveringtree.prim(self.graph)
        position = (0, 0)
        while parent[position] != []:
            self.solution.append(position)
            position = parent[position][0]
        self.solution.append(position)
    
    def generate_horizontal(self, biais):
        newgraph = self.generate_graph(self.width, self.height)
        for arc in newgraph.weights:
            j, i = arc[0]
            x, y = arc[1]
            if i == y:
                newgraph.weights[arc] += biais
        parent = coveringtree.prim(newgraph)
        newgraph.adjacency= {}
        for node in parent:
            if parent[node] != []:
                newgraph.add_arc((node, parent[node][0]))
                newgraph.add_arc((parent[node][0], node))  
        self.graph = newgraph

    def generate_vertical(self, biais):
        newgraph = self.generate_graph(self.width, self.height)
        for arc in newgraph.weights:
            j, i = arc[0]
            x, y = arc[1]
            if j == x:
                newgraph.weights[arc] += biais
        parent = coveringtree.prim(newgraph)
        newgraph.adjacency= {}
        for node in parent:
            if parent[node] != []:
                newgraph.add_arc((node, parent[node][0]))
                newgraph.add_arc((parent[node][0], node))  
        self.graph = newgraph