import maze

test = maze.Maze(30, 30)
#test.generate_maze()
test.generate_grid(30, 30)
#test.generate_graph(12, 12)
print("Poids: " + str(test.graph.weights))
print()
print("Aretes: " + str(test.graph.adjacency))
#print(test.graph.successors((0, 1)))
test.resolution()
print(test.solution)
test.print_graph()