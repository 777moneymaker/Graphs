#!usr/bin/env python3

import random


class Graph:
    def __init__(self, nvert=None):
        self.nvert = nvert  # number of vertices
        self.matrix = None
        self.listOfEdges = []
        self.listOfAdj = [[] for i in range(self.nvert)]  # empty matrix
        self.visitedVert = [[] for i in range(self.nvert)]

    def generateMatrix(self):
        nvert = self.nvert
        matrix = [[random.randint(0, 1) for i in range(nvert)] for i in range(nvert)]
        for i in range(nvert):
            matrix[i][i] = 0
        self.matrix = matrix

    def printMatrix(self):
        matrix = self.matrix
        count = 0
        print("\nMatrix:")
        for cell in matrix:
            print(count, cell)
            count += 1

    def generateListOfEdges(self):
        nvert = self.nvert
        matrix = self.matrix
        listofedges = self.listOfEdges
        for i in range(nvert):
            for j in range(nvert):
                if matrix[i][j] == 1:
                    listofedges.append((i, j))
        self.listOfEdges = listofedges

    def printListOfEdges(self):
        listofedges = self.listOfEdges
        print("\nList of edges:")
        for edge in listofedges:
            print(edge, end=" ")

    def generateListOfAdj(self):
        nvert = self.nvert
        matrix = self.matrix
        listofadj = self.listOfAdj
        for i in range(nvert):
            for j in range(nvert):
                if matrix[i] == 0:
                    listofadj[i].append(None)
                if matrix[i][j] == 1:
                    listofadj[i].append(j)
        self.listOfAdj = listofadj

    def printListOfAdj(self):
        listofadj = self.listOfAdj
        print("\n\nList of Adj:")
        count = 0
        for adj in listofadj:
            print(count, adj)
            count += 1
