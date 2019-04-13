#!usr/bin/env python3

import random


class Graph:
    def __init__(self, nvert = 3):
        self.nvert = nvert  # number of vertices
        self.matrix = None
        self.listOfEdges = []
        self.listOfAdj = [[] for i in range(self.nvert)]  # empty matrix

    def generateMatrix(self):
        self.matrix = [[random.randint(0, 1) for i in range(self.nvert)] for i in range(self.nvert)]
        for i in range(self.nvert):
            self.matrix[i][i] = 0

    def printMatrix(self):
        print("\nMatrix:")
        for c, cell in enumerate(self.matrix, 1):
            print(c, cell)

    def generateListOfEdges(self):
        for i in range(self.nvert):
            for j in range(self.nvert):
                if self.matrix[i][j] == 1:
                    self.listOfEdges.append((i, j))

    def printListOfEdges(self):
        print("\nList of edges:")
        for edge in self.listOfEdges:
            print(edge, end=" ")

    def generateListOfAdj(self):
        for i in range(self.nvert):
            for j in range(self.nvert):
                if self.matrix[i] == 0:
                    self.listOfAdj[i].append(None)
                if self.matrix[i][j] == 1:
                    self.listOfAdj[i].append(j)

    def printListOfAdj(self):
        print("\n\nList of Adj:")
        for c, adj in enumerate(self.listOfAdj, 1):
            print(c, adj)
