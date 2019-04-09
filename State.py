#!usr/bin/env python3

# code provided by Miłosz Chodkowski,
# Poznan University Of Technology

from Graph import Graph

if __name__ == "__main__":
    g = Graph(6)
    g.generateMatrix()
    g.printMatrix()
    g.generateListOfEdges()
    g.printListOfEdges()
    g.generateListOfAdj()
    g.printListOfAdj()

