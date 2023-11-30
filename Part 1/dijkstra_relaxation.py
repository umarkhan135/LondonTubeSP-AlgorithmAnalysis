from final_project_part1 import *
from min_heap import *



def dijkstra_approx(G, source, k):
    pred = {} #Predecessor dictionary. Isn't returned, but here for your understanding
    dist = {} #Distance dictionary
    relax = {}
    Q = min_heap.MinHeap([])
    nodes = list(G.adj.keys())
    
    for node in nodes:
        relax[node] = 0

    #Initialize priority queue/heap and distances
    for node in nodes:
        Q.insert(min_heap.Element(node, float("inf")))
        dist[node] = float("inf")
    Q.decrease_key(source, 0)

    #Meat of the algorithm
    while not Q.is_empty():
        current_element = Q.extract_min()
        current_node = current_element.value
        dist[current_node] = current_element.key
        for neighbour in G.adj[current_node]:
            if relax[neighbour] < k and dist[current_node] + G.w(current_node, neighbour) < dist[neighbour]:
                Q.decrease_key(neighbour, dist[current_node] + G.w(current_node, neighbour))
                dist[neighbour] = dist[current_node] + G.w(current_node, neighbour)
                pred[neighbour] = current_node
                relax[neighbour] += 1;
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

#print(dijkstra_approx(g, 0, 1))
