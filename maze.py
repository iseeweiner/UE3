from matplotlib.pyplot import plot
import graph 
import render
import coveringtree
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
        render.draw_square_maze(self.graph, self.solution, False) # on donne le graph et la liste des solutions à afficher

    def generate_maze(self):
        parent = coveringtree.prim(self.graph)
        newgraph = self.generate_graph(self.width, self.height)
        # A revoir
        newgraph.adjacency = {}
        for node in parent:
            if parent[node] != []:
                newgraph.add_arc((node, parent[node][0]))
                newgraph.add_arc((parent[node][0], node))         
        #newgraph.adjacency = parent
        self.graph = newgraph

    def generate_random(self):
        grid = graph.Graph()
        # On genere le graphe
        for i in range (self.height):
            for j in range (self.width):
                # On genere la liste des voisons
                neighbours = [(j, i + 1), (j + 1, i), (j, i - 1), (j - 1, i)]
                # Pour chaque voisin
                for neighbour in neighbours:
                    # Si il est dans la grille
                    x, y = neighbour
                    if self.width -1 >= x >= 0 and self.height - 1 >= y >= 0:
                        node = (j, i)
                        weight = random.randint(0, 1)
                        grid.add_weighted_arc((node,neighbour), weight)
                        grid.add_weighted_arc((neighbour,node), weight)
        self.graph = grid

    def prim_resolver(self):
        parent = coveringtree.prim(self.graph)
        print("Parent :" + str(parent))
        position = (0, 0)
        while parent[position] != []:
            self.solution.append(position)
            position = parent[position][0]
    
    def generate_horizontal(self, biais):
        newgraph = self.generate_graph(self.width, self.height)
        # On applique le biais aux poids
        for arc in newgraph.weights:
            # On ajout le biais aux arretes horizontales
            j, i = arc[0]
            x, y = arc[1]
            if i == y:
                newgraph.weights[arc] += biais
                print("Horizontal Arc: %s / Weight: %s" % (str(arc), str(newgraph.weights[arc])))
        parent = coveringtree.prim(newgraph)
        newgraph.adjacency= {}
        for node in parent:
            if parent[node] != []:
                newgraph.add_arc((node, parent[node][0]))
                newgraph.add_arc((parent[node][0], node))  
        self.graph = newgraph

    def generate_vertical(self, biais):
        newgraph = self.generate_graph(self.width, self.height)
        # On applique le biais aux poids
        for arc in newgraph.weights:
            # On ajout le biais aux arretes horizontales
            j, i = arc[0]
            x, y = arc[1]
            if j == x:
                newgraph.weights[arc] += biais
                print("Veritcal Arc: %s / Weight: %s" % (str(arc), str(newgraph.weights[arc])))
        parent = coveringtree.prim(newgraph)
        print("Parent: %s" % parent)
        print("Weights: %s" % str(newgraph.weights))
        newgraph.adjacency= {}
        for node in parent:
            if parent[node] != []:
                newgraph.add_arc((node, parent[node][0]))
                newgraph.add_arc((parent[node][0], node))  
        self.graph = newgraph
        

#Tache 6 : generation d’un labyrinthe biais ́e (3 points)
#G ́en ́erer un labyrinthe se fait tr`es facilement ; en v ́erit ́e, il suffit de proc ́eder `a une exploration al ́eatoire en
#profondeur du graphe support. Notre m ́ethode plus compliqu ́ee a cependant un avantage : nous allons pouvoir
#facilement modifier notre g ́en ́eration pour transformer le rendu de nos labyrinthes.

#Pour accomplir cette tˆache, rajouter deux fonctions `a la classe Maze. L’une g ́en`ere une grille, et prend en
#param`etre suppl ́ementaire une valeur entre 0 et 1, qui repr ́esente le biais qui sera rajout ́e au poids des arˆetes
#verticales. La seconde fonction fait de mˆeme, mais rajoute ce biais au poids des arˆetes horizontale.
#Par l’action de ce biais, les arˆetes verticales (resp. horizontales) seront privil ́egi ́ees par l’algorithme de Prim.
#Ainsi, un biais de 0 ne fera aucune diff ́erence, mais un biais vertical de 0.5 rendra les transition verticales bien
#plus ch`eres par rapport au arˆetes horizontales, et donc choisies moins souvent. Un biais de 1 rendra toutes les
#transitions de la direction choisie n ́ecessairement plus ch`eres que les transitions de l’autre direction ; ainsi, un
#biais horizontal de 1 nous donnera un labyrinthe avec un nombre minimal de transitions horizontales.
#Un exemple d’affichage est pr ́esent ́e en figure 2