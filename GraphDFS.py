#!usr/bin/env python3

from collections import defaultdict


class GraphDFS:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):  # function to add an edge to graph
        self.graph[u].append(v)

    def DFSUtil(self, v, visited):
        visited[v] = True
        print(v, end = " ")
        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited)

    def DFS(self, v):
        visited = [False] * (len(self.graph))
        self.DFSUtil(v, visited)


