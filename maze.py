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
        self.solution = []

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
        render.draw_square_maze(self.graph, self.solution, False) # on donne le graph et la liste des solutions à afficher

    def generate_maze(self):
        parent = coveringtree.prim(self.graph)
        newgraph = graph.Graph()
        newgraph.adjacency = parent
        self.graph = newgraph

    def generate_grid_old(self, width, height):
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
        for position in list_nodes:
            grid.add_node(position)
            j, i = position
            neighbours = [(j, i + 1), (j + 1, i), (j, i - 1), (j - 1, i)]
            neighbours_list = []
            for v in neighbours:
                j, i = v
                if j >= 0 and j < width and i >= 0 and i < height and grid.weights[v] == 0: # si on ne sort pas du cadre et que le voisin 'v' a un poids de 0
                    neighbours_list.append(v) # ajoute le voisin 'v' dans la liste des voisins
            grid.adjacency[position] = neighbours_list
        self.graph = grid



    def generate_grid(self, width, height):
        grid = graph.Graph()
        list_nodes = []
        for i in range (height):
            for j in range (width):
                list_nodes.append((j, i))    
        # On defini des poids aleatoires
        for i in range (height):
            for j in range (width):
                # On parcour les voisins
                
                #weight = random.uniform(0, 1)
                weight = random.randint(0, 1)
                if not (j, i) in grid.weights:
                    grid.set_arc_weight((j, i), weight)
                    grid.set_arc_weight((i, j), weight)
        # On defini les sommets
        for position in list_nodes:
            grid.add_node(position)
            j, i = position
            neighbours = [(j, i + 1), (j + 1, i), (j, i - 1), (j - 1, i)]
            neighbours_list = []
            for v in neighbours:
                j, i = v
                if j >= 0 and j < width and i >= 0 and i < height and grid.weights[v] == 0: # si on ne sort pas du cadre et que le voisin 'v' a un poids de 0
                    neighbours_list.append(v) # ajoute le voisin 'v' dans la liste des voisins
            grid.adjacency[position] = neighbours_list
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
                    # filtre la position precedante
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
                position = (j, i + 1) # on deplace 'position' sur la position choisie
                self.solution.append(position) # on rajoute la nouvelle position dans la liste des solutions
            else:
                previous = position
                position = possible_positions[0] # on deplace 'position' sur la position choisie
                self.solution.append(position) # on rajoute la nouvelle position dans la liste des solutions   
            # si aucun choix disponible et aucune solution choisie --> break
            if self.solution[-1] == position: # si on n'a pas bougé, on break
                break
    