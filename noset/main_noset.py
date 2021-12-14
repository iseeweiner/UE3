import maze_noset as maze

# On a retiré les méthodes set dans la classe coveringtree qui semblent désordonner les dictionnaires/listes et perturber la résolution de prim

# On a remarqué lors de la génération d'un graphe de 10/10 que le dictionnaire des parents renvoyé par prim était désordonné et notamment, que le dernier élément de celui-ci
# a la même coordonnée que celle considérée sur le graphe comme l'arrivée du labyrinthe pour prim
#
#Parent :{(4, 0): [(4, 1)], (4, 9): [(5, 9)], (3, 7): [(4, 7)], (5, 4): [(5, 5)], (4, 6): [(4, 7)], (5, 1): [(4, 1)], (8, 0): [(8, 1)], (9, 2): [(9, 3)], (8, 9): [(7, 9)], (9, 8): [(9, 7)], (0, 5): [(1, 5)], (2, 2): [(2, 3)], 
#(1, 0): [(1, 1)], (8, 6): [(8, 7)], (1, 9): [(1, 8)], (2, 8): [(2, 7)], (7, 4): [(7, 5)], (6, 2): [(7, 2)], (7, 1): [(7, 2)], (6, 8): [(7, 8)], (4, 2): [(4, 3)], (3, 0): [(3, 1)], (3, 9): [(3, 8)], (5, 6): [(5, 7)], (4, 8): [(5, 8)], (3, 6): [(3, 5)], (5, 3): [(4, 3)], (8, 2): [(8, 3)], (9, 1): [(8, 1)], (0, 7): [(1, 7)], (2, 4): [(2, 5)], (1, 2): [(1, 3)], (0, 4): [(0, 3)], (2, 1): [(1, 1)], (8, 8): [(7, 8)], (1, 8): [(1, 7)], (6, 4): [(6, 5)], 
#(7, 3): [(8, 3)], (3, 2): [(3, 3)], (4, 1): [(3, 1)], (3, 8): [(4, 8)], (5, 5): [(6, 5)], (8, 4): [(9, 4)], (9, 3): [(9, 4)], (8, 1): [(8, 2)], (0, 0): [(0, 1)], (0, 9): [(0, 8)], (1, 4): [(1, 5)], (0, 6): [(1, 6)], (2, 3): [(3, 3)], (6, 6): [(7, 6)], (7, 5): [(7, 6)], (6, 3): [(7, 3)], (3, 4): [(4, 4)], (4, 3): [(4, 4)], (3, 1): [(3, 2)], (5, 7): [(5, 8)], (9, 5): [(9, 6)], (8, 3): [(9, 3)], (0, 2): [(0, 3)], (1, 6): [(2, 6)], (0, 8): [(1, 8)], 
#(2, 5): [(3, 5)], (1, 3): [(2, 3)], (7, 7): [(7, 8)], (6, 5): [(7, 5)], (4, 5): [(5, 5)], (3, 3): [(4, 3)], (5, 0): [(6, 0)], (5, 9): [(6, 9)], (9, 7): [(8, 7)], (8, 5): [(9, 5)], (9, 4): [(9, 5)], (0, 1): [(0, 2)], (2, 7): [(2, 6)], (1, 5): [(2, 5)], (6, 1): [(7, 1)], (7, 0): [(7, 1)], (7, 9): [(7, 8)], (6, 7): [(7, 7)], (7, 6): [(7, 7)], (4, 7): [(5, 7)], (3, 5): [(4, 5)], (5, 2): [(5, 3)], (4, 4): [(4, 5)], (9, 0): [(9, 1)], (5, 8): [(5, 9)], 
#(8, 7): [(7, 7)], (9, 9): [(9, 8)], (1, 1): [(0, 1)], (0, 3): [(1, 3)], (9, 6): [(9, 7)], (2, 0): [(2, 1)], (2, 9): [(3, 9)], (1, 7): [(2, 7)], (2, 6): [(2, 5)], (7, 2): [(7, 3)], (6, 0): [(7, 0)], (6, 9): [(7, 9)], (7, 8): []}
#
# On a donc fait le test, de supprimer l'appel aux méthodes set() dans la classe graph.py et conserver les résultats des methodes sous forme de liste/dictionnaire.
# Ce qui a pour but de conserver l'ordre des clés/valeurs des listes/dictionnaires et on constate que dans ce cas, la problématique de fin de labyrinthe fixe (position (7,8))
# pour un labyrinthe de taille 10/10 ou plus est maintenant corrigé

# Création d'un objet maze de 10/10
test = maze.Maze(20, 20)

# Génération du labyrinthe
#test.generate_maze()

# Génération d'un labyrinthe random
test.generate_random()

# Génération d'un labyrinthe biaisé horizontalement
#test.generate_horizontal(0.1)

# Génération d'un labyrinthe biaisé verticalement
#test.generate_vertical(0.5)

# Résolution
#test.resolution()
test.prim_resolver()

# Affichage du graphe
test.print_graph()