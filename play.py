#!usr/bin/env python3

__author__ = 'Milosz Chodkowski PUT'

from graph import Graph


if __name__ == "__main__":
    G = Graph(10)
    print(G.adj_list)
    G.dfs()
    print(G.path)