from final_project_part1 import *
from dijkstra_relaxation import *
from bellmanford_relaxation import *
import matplotlib.pyplot as plt
import timeit 
import numpy as np

'''
*************
Testing
*************
'''

g = DirectedWeightedGraph()
for i in range(9):
    g.add_node(i)
g.add_edge(0, 1, 2)
g.add_edge(0, 2, -1)
g.add_edge(1, 3, 3)
g.add_edge(1, 4, 5)
g.add_edge(1, 5, 1)
g.add_edge(2, 6, -7)
g.add_edge(5, 7, 2)
g.add_edge(6, 8, 3)
g.add_edge(5, 4, -1)

#print(mystery(g))

'''
*************
Experiment
*************
'''

def experiment(graph_sizes, upper, num_trials):
    times = []
    for sizes in graph_sizes:
        count = 0
        for _ in range(num_trials):
            G = create_random_complete_graph(sizes, upper)
            start_time = timeit.default_timer()
            mystery(G)
            end_time = timeit.default_timer()
            execution_time = end_time - start_time
            count += execution_time
        times.append(count/num_trials)

    log_x1 = np.log(graph_sizes[0])
    log_y1 = np.log(times[0])
    log_x2 = np.log(graph_sizes[-1])
    log_y2 = np.log(times[-1])

    # Calculating the slope
    slope = (log_y2 - log_y1) / (log_x2 - log_x1)
    print(slope)
    
    times2 = times.copy()
    
    #plt.loglog(graph_sizes, times2, label='log-log')
    plt.plot(graph_sizes, times, label='normal-plot')
    plt.xlabel('Graph sizes')
    plt.ylabel('Time')
    plt.title('Graph size VS time for mystery algorithm')
    plt.grid(True)
    plt.legend()
    plt.show()
    
graph_sizes = []
for i in range(10, 200, 10):
    graph_sizes.append(i)

upper = 1000
num_trials = 10

#experiment(graph_sizes, upper, num_trials)

'''
****************
Small Graph with Negative Edges Test
****************
'''

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

#print(mystery(g1))