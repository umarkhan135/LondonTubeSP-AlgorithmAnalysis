from final_project_part1 import *
from min_heap import *


def bellman_ford_approx(G, source, k):
    pred = {} #Predecessor dictionary. Isn't returned, but here for your understanding
    dist = {} #Distance dictionary
    relax = {}
    nodes = list(G.adj.keys())
    
    for node in nodes:
        relax[node] = 0

    #Initialize distances
    for node in nodes:
        dist[node] = float("inf")
    dist[source] = 0

    #Meat of the algorithm
    for _ in range(G.number_of_nodes()):
        for node in nodes:
            for neighbour in G.adj[node]:
                if relax[neighbour] < k and dist[neighbour] > dist[node] + G.w(node, neighbour):
                    dist[neighbour] = dist[node] + G.w(node, neighbour)
                    pred[neighbour] = node
                    relax[neighbour] += 1
    return dist

'''
*************
Testing
*************
'''

g = DirectedWeightedGraph()
for i in range(9):
    g.add_node(i)
g.add_edge(0, 1, 2)
g.add_edge(0, 2, 1)
g.add_edge(1, 3, 3)
g.add_edge(1, 4, 5)
g.add_edge(1, 5, 1)
g.add_edge(2, 6, 7)
g.add_edge(5, 7, 2)
g.add_edge(6, 8, 3)
g.add_edge(5, 4, 1)


g1 = DirectedWeightedGraph()
for i in range(6):
    g1.add_node(i)
    
g1.add_edge(0, 1, 8)
g1.add_edge(0, 2, 10)
g1.add_edge(1, 3, 1)
g1.add_edge(2, 5, 2)
g1.add_edge(3, 2, -4)
g1.add_edge(3, 5, -1)
g1.add_edge(4, 2, 1)
g1.add_edge(5, 4, -2)

#print(bellman_ford_approx(g1, 0, 1))