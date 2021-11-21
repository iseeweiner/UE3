import maze

test = maze.Maze(10, 10)
#test.generate_maze()
test.generate_grid(5, 6)
#test.generate_graph(12, 12)
print(str(test.graph.weights))
print(str(test.graph.adjacency))
print(test.graph.successors((0, 1)))
test.print_graph()