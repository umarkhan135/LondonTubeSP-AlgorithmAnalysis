import min_heap
from final_project_part1 import *


def a_star(G, s, d, h):
    pred = {}
    dist = {}
    Q = min_heap.MinHeap([])
    nodes = list(G.adj.keys())
    
    for node in nodes:
        Q.insert(min_heap.Element(node, float("inf")))
        dist[node] = float("inf")
        pred[node] = None  # Initialize predecessors
    Q.decrease_key(s, h(s))
    dist[s] = 0
    
    while not Q.is_empty():
        current_element = Q.extract_min()
        current_node = current_element.value
        dist[current_node] = current_element.key

        if current_node == d:
            break

        for neighbour in G.adj[current_node]:
            if dist[current_node] + G.w(current_node, neighbour) < dist[neighbour]:
                dist[neighbour] = dist[current_node] + G.w(current_node, neighbour)
                pred[neighbour] = current_node
                fn = dist[current_node] + G.w(current_node, neighbour) + h(neighbour)
                Q.decrease_key(neighbour, fn)

        
    
    
    path = []
    if pred[d] is not None or d == s:  # Check if d is reachable
        while d is not None:
            path.insert(0, d)
            d = pred[d]

    return pred, path



