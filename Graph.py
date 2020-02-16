#!usr/bin/env python3

__author__ = 'Milosz Chodkowski PUT'

from random import randint


class Graph:
    def __init__(self, nvert = 3):
        self.nvert = nvert  # number of vertices
        self.adj_list = {
            node: list({randint(0, self.nvert - 1) for i in range(randint(1, self.nvert - 1))}) for node in range(self.nvert)
        }
        self.visited = [False] * self.nvert
        self.path = []

    def dfs(self, vertex = 0):
        self.visited[vertex] = True
        self.path.append(vertex)
        for neighbour in self.adj_list[vertex]:
            if self.visited[neighbour] == False:
                self.dfs(neighbour)
