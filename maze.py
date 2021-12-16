from matplotlib.pyplot import plot
import graph 
import render
import coveringtree
import random

class Maze:

    # Tache 1 - 2 / Constructeur qui prend en paramètre une largeur et une hauteur et initialise l'attribut graphe
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.graph = self.generate_graph(width, height)
        self.solution = []

    # Tache 1 - 1 / Méthode qui prend en paramètre une largeur et une hauteur et génère et retourne un graphe non orienté
    def generate_graph(self, width, height):
        list_nodes = []
        newgraph = graph.Graph()
        # On génère toutes les coordonnées en fonction de la taille du graphe
        for j in range (width):
            for i in range (height):
                # On ajoute la coordonnée à la liste des coordonées
                list_nodes.append((j, i))    
        # On parcourt toutes les coordonnées du graphe
        for node in list_nodes:
            j, i = node
            # On génère la liste des voisins pour la coordonnée en cours
            neighbours = [(j, i + 1), (j + 1, i), (j, i - 1), (j - 1, i)]
            # Pour chaque voisin
            for neighbour in neighbours:
                x, y = neighbour
                # Si il est dans la grille
                if self.width -1 >= x >= 0 and self.height - 1 >= y >= 0:
                    node = (j, i)
                    # On ajoute l'arc de ces deux coordonnées au graphe
                    newgraph.add_arc((node,neighbour))
                    newgraph.add_arc((neighbour,node))
        # On retourne le graphe généré
        return newgraph

    # Tache 1 - 3 / Affiche le graphe à l'écran grâce au module render
    def print_graph(self):
        # On donne le graphe et la liste des solutions à afficher
        render.draw_square_maze(self.graph, self.solution, False)

    # Tache 3 / Génération d'un labyrinthe
    def generate_maze(self):
        # Tache 3 - 1 / Faire appel à prim avec pour paramètre le graphe support du labyrinthe
        parent = coveringtree.prim(self.graph)
        # Tache 3 - 2 / Utiliser le dict généré à l'étape précédente pour créer un nouveau graphe
        newgraph = self.generate_graph(self.width, self.height)
        # On réinitialise les adjacences pour pouvoir les remplacer avec celles données par prim (parent)
        newgraph.adjacency = {}
        # On parcourt la liste des parents
        for node in parent:
            # Si le parent n'est pas vide
            if parent[node] != []:
                # On ajoute l'arc entre ces deux coordonnées
                newgraph.add_arc((node, parent[node][0]))
                # Ainsi que son inverse
                newgraph.add_arc((parent[node][0], node))         
        # Tache 3 - 3 / Remplacer l'attribut contenant le graphe du labyrinthe par le graphe construit a l'étape précédente
        self.graph = newgraph

    # Tache 4 / Génération d'un labyrinthe aléatoire
    def generate_random(self):
        grid = graph.Graph()
        # On génère chaque coordonnées
        for i in range (self.height):
            for j in range (self.width):
                # On génère la liste des voisins pour la coordonnée en cours
                neighbours = [(j, i + 1), (j + 1, i), (j, i - 1), (j - 1, i)]
                # Pour chaque voisin
                for neighbour in neighbours:
                    x, y = neighbour
                    # Si il est dans la grille
                    if self.width -1 >= x >= 0 and self.height - 1 >= y >= 0:
                        node = (j, i)
                        # On génère un poids aleatoire entre 1 et 0
                        weight = random.uniform(0, 1)
                        # On ajoute l'arc de ces deux coordonnées au graphe avec le poids aléatoire généré précedemment
                        grid.add_arc((node,neighbour), weight)
                        grid.add_arc((neighbour,node), weight)
        parent = coveringtree.prim(grid)
        grid.adjacency = {}
        for node in parent:
            # Si le parent n'est pas vide
            if parent[node] != []:
                # On ajoute l'arc entre ces deux coordonnées
                grid.add_arc((node, parent[node][0]))
                # Ainsi que son inverse
                grid.add_arc((parent[node][0], node))       
        # On enregistre le graphe généré dans l'attribut graph du constructeur
        self.graph = grid

    # Tache 5 / Résolution d'un labyrinthe
    def prim_resolver(self):
        # On fait appel à prim pour obtenir les parents
        parent = coveringtree.prim(self.graph)
        # On part de la position de départ (0,0)
        position = (0, 0)
        # Tant que l'élément "position" dans le dictionnaire des parents n'est pas vide
        while parent[position] != []:
            # On ajoute cette position à la solution
            self.solution.append(position)
            # On change l'élément "position" sur la nouvelle position
            position = parent[position][0]
    
    # Tache 6 - 1 / Génération d'un labyrinthe biaisé horizontalement
    def generate_horizontal(self, biais):
        # On genere une nouvelle grille
        newgraph = self.generate_graph(self.width, self.height)
        # On parcours les arcs
        for arc in newgraph.weights:
            # On ajoute le biais aux arêtes horizontales
            j, i = arc[0]
            x, y = arc[1]
            # Si l'arête est horizontale (coordonnées des ordonnées identiques pour les deux sommets)
            if j == x:
                # On rajoute le biais
                newgraph.weights[arc] += biais
        # On fait appel à prim pour obtenir les parents du nouveau graphe avec le biais ajouté
        parent = coveringtree.prim(newgraph)
        # On réinitialise les adjacences du graphe pour insérer les nouveaux arcs donnés par prim
        newgraph.adjacency= {}
        # On parcourt chaque coordonnée de parent
        for node in parent:
            # Si la coordonnée a au moins un parent
            if parent[node] != []:
                # On ajoute l'arc entre la coordonnée et son parent
                newgraph.add_arc((node, parent[node][0]))
                # Ainsi que l'inverse
                newgraph.add_arc((parent[node][0], node)) 
        # On enregistre le graphe généré dans l'attribut graph du constructeur
        self.graph = newgraph

    # Tache 6 - 1 / Génération d'un labyrinthe biaisé verticalement
    def generate_vertical(self, biais):
        # On parcours les arcs
        newgraph = self.generate_graph(self.width, self.height)
        # On applique le biais aux poids
        for arc in newgraph.weights:
            # On ajoute le biais aux arêtes verticales
            j, i = arc[0]
            x, y = arc[1]
            # Si l'arête est verticale (coordonnées des abscisses identiques pour les deux sommets)
            if y == i:
                # On rajoute le biais
                newgraph.weights[arc] += biais
        # On fait appel à prim pour obtenir les parents du nouveau graphe avec le biais ajouté
        parent = coveringtree.prim(newgraph)
        # On réinitialise les adjacences du graphe pour insérer les nouveaux arcs donnés par prim
        newgraph.adjacency= {}
        # On parcourt chaque coordonnée de parent
        for node in parent:
            # Si la coordonnée a au moins un parent
            if parent[node] != []:
                # On ajoute l'arc entre la coordonnée et son parent
                newgraph.add_arc((node, parent[node][0]))
                # ainsi que l'inverse
                newgraph.add_arc((parent[node][0], node)) 
        # On enregistre le graphe généré dans l'attribut graph du constructeur 
        self.graph = newgraph
    