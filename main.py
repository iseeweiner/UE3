import maze



# Creation d'un objet maze de 10/10
test = maze.Maze(10, 10)

# Generation du labyrinthe
#test.generate_maze()

# Generation d'un labyrinthe random
#test.generate_random()

# Generation d'un labyrinthe biaisé horizontalement
test.generate_horizontal(0.1)

# Generation d'un labyrinthe biaisé verticalement
#test.generate_vertical(0.5)

# Resolution
#test.resolution()
test.prim_resolver()

# Affichage du graphe
test.print_graph()