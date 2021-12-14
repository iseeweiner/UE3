import maze

# Tache 3 - Test / Pour tester votre travail, créer un main.py qui

# Création d'un objet maze de 10/10
test = maze.Maze(10, 10)

# Décommenter la methode a tester (generate_maze, generate_random, generate_horizontal, generate_vertical)

# Génération du labyrinthe
#test.generate_maze()

# Génération d'un labyrinthe aléatoire
test.generate_random()

# Génération d'un labyrinthe biaisé horizontalement
#test.generate_horizontal(0.0000001)

# Génération d'un labyrinthe biaisé verticalement
#test.generate_vertical(0.5)

# Résolution
test.prim_resolver()

# Affichage du graphe
test.print_graph()