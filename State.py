#!usr/bin/env python3

# code provided by Miłosz Chodkowski,
# Poznan University Of Technology

from Graph import Graph
from GraphDFS import GraphDFS

if __name__ == "__main__":
    print("\n FIRST GRAPH: \n")
    g = Graph(6)
    g.generateMatrix()
    g.printMatrix()
    g.generateListOfEdges()
    g.printListOfEdges()
    g.generateListOfAdj()
    g.printListOfAdj()

    print("\n SECOND GRAPH: \n")
    gDFS = GraphDFS()
    for i in range(6):
        for j in range(6):
            gDFS.addEdge(i, j)
    print("DFS 0: ")
    print(gDFS.DFS(0))
    print("DFS 1: ")
    print(gDFS.DFS(1))
    print("DFS 2: ")
    print(gDFS.DFS(2))
    print("DFS 3: ")
    print(gDFS.DFS(3))
    print("DFS 4: ")
    print(gDFS.DFS(4))
    print("DFS 5: ")
    print(gDFS.DFS(5))
