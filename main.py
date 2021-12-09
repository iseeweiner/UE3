import maze

test = maze.Maze(5, 5)
test.graph = test.generate_graph(5, 5)
print("Test.graph : " + str(test.graph.adjacency))
#test.generate_grid(5, 5)
test.generate_maze()
#test.resolution()
#print(test.solution)
test.print_graph()