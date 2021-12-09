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

    def print_graph(self):
        render.draw_square_maze(self.graph, self.solution, False) # on donne le graph et la liste des solutions à afficher

    def generate_maze(self):
        parent = coveringtree.prim(self.graph)
        print("parent: " + str(parent))
        newgraph = self.generate_graph(self.width, self.height)
        # A revoir
        for node in parent:
            if parent[node] != []:
                print("Node: %s  /  Parents(node): %s" % (str(node), str(parent[node])))
                newgraph.remove_arc((node, parent[node][0]))
                newgraph.remove_arc((parent[node][0], node))         
        #newgraph.adjacency = parent
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
                neighbours = [(j, i + 1), (j + 1, i), (j, i - 1), (j - 1, i)]
                for neighbour in neighbours:
                    if neighbour in list_nodes:
                        node = (j, i)
                        weight = random.randint(0, 1)
                        grid.add_arc((node,neighbour), weight)
                        grid.add_arc((neighbour,node), weight)
                        ## on defini un poids pour la paire de sommets, si il n'existe pas deja
                        #if not (node,neighbour) in grid.weights:
                        #    grid.set_arc_weight((node,neighbour), weight)
                        ## on defni le meme poids pour la paire inverse, si il n'existe pas deja
                        #if not (neighbour,node) in grid.weights:
                        #    grid.set_arc_weight((neighbour,node), weight)
#        # On defini les sommets
#        for position in list_nodes:
#            # On ajoute la position a la liste des sommets
#            grid.add_node(position)
#            j, i = position
#            # On genere la liste des voisins
#            neighbours = [(j, i + 1), (j + 1, i), (j, i - 1), (j - 1, i)]
#            # On initialise une liste vide de voisin accessible 
#            accessible_neighbours = []
#            for v in neighbours:
#                x, y = v
#                if x >= 0 and x < width and y >= 0 and y < height and grid.weights[(position, v)] == 0: # si on ne sort pas du cadre et que le voisin 'v' a un poids de 0
#                    accessible_neighbours.append(v) # ajoute le voisin 'v' dans la liste des voisins
#            grid.adjacency[position] = accessible_neighbours
        self.graph = grid


    def resolution(self):
        position = (0, 0)
        previous = ()
        self.solution.append(position)
        while position != (self.width - 1, self.height - 1):
            # parcourir le poids des voisins de "position"
            possible_positions = []
            j, i = position
            for arc in self.graph.successors(position):
                # filter les positions en diagonale
                if arc in [(j + 1, i), (j, i + 1), (j - 1, i), (j, i - 1)]:
                    # filtre la position precedente
                    if arc != previous:
                        possible_positions.append(arc)
            # choix de la nouvelle position
            if len(possible_positions) == 0:
                break
            elif (j, i + 1) in possible_positions:
                previous = position
                position = (j, i + 1) # on deplace 'position' sur la position choisie
                self.solution.append(position) # on rajoute la nouvelle position dans la liste des solutions       
            elif (j + 1, i) in possible_positions:
                previous = position
                position = (j + 1, i) # on deplace 'position' sur la position choisie
                self.solution.append(position) # on rajoute la nouvelle position dans la liste des solutions
            else:
                previous = position
                position = possible_positions[0] # on deplace 'position' sur la position choisie
                self.solution.append(position) # on rajoute la nouvelle position dans la liste des solutions   
            # si aucun choix disponible et aucune solution choisie --> break
    
    def generate_horizontal(self, width, height, biais):
        grid = graph.Graph()
        list_nodes = []
        for i in range (height):
            for j in range (width):
                list_nodes.append((j, i))    
        # On defini des poids aleatoires
        for i in range (height):
            for j in range (width):
                neighbours = [(j, i + 1), (j + 1, i), (j, i - 1), (j - 1, i)]
                for neighbour in neighbours:
                    if neighbour in list_nodes:
                        node = (j, i)
                        weight = random.randint(0, 1)
                        # on defini un poids pour la paire de sommets, si il n'existe pas deja
                        if not (node,neighbour) in grid.weights:
                            grid.set_arc_weight((node,neighbour), weight)
                        # on defni le meme poids pour la paire inverse, si il n'existe pas deja
                        if not (neighbour,node) in grid.weights:
                            grid.set_arc_weight((neighbour,node), weight)
        # On defini les sommets
        for position in list_nodes:
            # On ajoute la position a la liste des sommets
            grid.add_node(position)
            j, i = position
            # On genere la liste des voisins
            neighbours = [(j, i + 1), (j + 1, i), (j, i - 1), (j - 1, i)]
            # On initialise une liste vide de voisin accessible 
            accessible_neighbours = []
            for v in neighbours:
                x, y = v
                if x >= 0 and x < width and y >= 0 and y < height and grid.weights[(position, v)] == 0: # si on ne sort pas du cadre et que le voisin 'v' a un poids de 0
                    accessible_neighbours.append(v) # ajoute le voisin 'v' dans la liste des voisins
            grid.adjacency[position] = accessible_neighbours
        self.graph = grid


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