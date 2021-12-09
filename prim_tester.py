from matplotlib.pyplot import plot
import graph 
import render
import coveringtree
import random
    
    
    
def generate_graph(width, height):
    list_nodes = []
    newgraph = graph.Graph()
    for i in range (height):
        for j in range (width):
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

mygraph = generate_graph(5, 5)
parent = coveringtree.prim(mygraph)

print("MyGraph adjacency: " + str(mygraph.adjacency))
print("MyGraph weights: " + str(mygraph.weights))
print("Parent: " + str(parent))