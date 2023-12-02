from final_project_part1 import *
from dijkstra_relaxation import *
from bellmanford_relaxation import *
import matplotlib.pyplot as plt
import timeit 



'''
*************
Experiment 1
*************
'''


def experiment1_helper(G, source, k_value, numtrials):
    results = {}
    graph_size = G.number_of_nodes()
    dist_standard = dijkstra(G, source)
    total_distance_standard = total_dist(dist_standard)

    for value in k_value:
        relative_error = 0
        for i in range(numtrials):
            k = value
            dist_approx = dijkstra_approx(G, source, k)
            total_distance_approx = total_dist(dist_approx)

            # Correctly calculate accuracy
            relative_error += abs(total_distance_approx - total_distance_standard) / total_distance_standard
        results[value] = relative_error/numtrials
    
    return results

def experiment1(G_sizes, k_value, source, upper, numtrials):
    results = {value: [] for value in k_value}
    for size in G_sizes:
        G = create_random_complete_graph(size, upper)
        accuracies = experiment1_helper(G, source, k_value, numtrials)
        for value in k_value:
            results[value].append(accuracies[value])
            
    for value in k_value:
        plt.plot(G_sizes, results[value], label=f'k_value = {value}')
    plt.title('Accuracy vs Graph Size for Different k values')
    plt.xlabel('Graph Size')
    plt.ylabel('Accuracy')
    plt.legend()
    plt.grid(True)
    plt.show()
    

G_sizes1 = []
for i in range(100, 450, 50):
    G_sizes1.append(i)
k_value1 = [1, 2, 5, 10, 15]
source1 = 0
num_trials1 = 25
upper1 = 1000

#experiment1(G_sizes1, k_value1, source1, upper1, num_trials1)


'''
*************
Experiment 2
*************
'''

def create_sparse_graph(num_nodes, edge_probability, upper):
    G = DirectedWeightedGraph()
    
    for i in range(num_nodes):
        G.add_node(i)

    for i in range(num_nodes):
        for j in range(num_nodes):
            if i != j and random.random() < edge_probability:
                G.add_edge(i, j, random.randint(1, upper))

    return G

def experiment2_helper(G, source, k_value, numtrials):
    results = {}
    dist_standard = dijkstra(G, source)
    total_distance_standard = total_dist(dist_standard)

    for value in k_value:
        relative_error = 0
        for i in range(numtrials):
            k = value
            dist_approx = dijkstra_approx(G, source, k)
            total_distance_approx = total_dist(dist_approx)

            # Correctly calculate accuracy
            relative_error += abs(total_distance_approx - total_distance_standard) / total_distance_standard
        results[value] = relative_error/numtrials
    
    return results

def experiment2(G_size, k_value, source, upper, numtrials, probabilities):
    results = {value: [] for value in k_value}
    
    for prob in probabilities:
        G = create_sparse_graph(G_size, prob, upper)
        accuracies = experiment2_helper(G, source, k_value, numtrials)
        for value in k_value:
            results[value].append(accuracies[value])
            
    for value in k_value:
        plt.plot(probabilities, results[value], label=f'k_value = {value}')
    plt.title('Accuracy vs Graph Density for Different k values')
    plt.xlabel('Graph Density (Probability)')
    plt.ylabel('Accuracy')
    plt.legend()
    plt.grid(True)
    plt.show()
    

G_sizes2 = 200
k_value2 = [1, 2, 5, 10, 15]
source2 = 0
num_trials2 = 10
upper2 = 1000
probability = [0.1, 0.2, 0.3, 0.5, 0.75]

#experiment2(G_sizes2, k_value2, source2, num_trials2, upper2, probability)



'''
*************
Experiment 3
*************
'''


def experiment3_helper(G, source, k_value, numtrials):
    results = {}
    graph_size = G.number_of_nodes()
    dist_standard = dijkstra(G, source)
    total_distance_standard = total_dist(dist_standard)

    for value in k_value:
        relative_error = 0
        for i in range(numtrials):
            k = value
            dist_approx = dijkstra_approx(G, source, k)
            total_distance_approx = total_dist(dist_approx)

            # Correctly calculate accuracy
            relative_error += abs(total_distance_approx - total_distance_standard) / total_distance_standard
        results[value] = relative_error/numtrials
    
    return results

def experiment3(G_sizes, k_value, source, upper, numtrials, probability):
    results = {value: [] for value in k_value}
    for size in G_sizes:
        G = create_sparse_graph(size, probability, upper)
        accuracies = experiment3_helper(G, source, k_value, numtrials)
        for value in k_value:
            results[value].append(accuracies[value])
            
    for value in k_value:
        plt.plot(G_sizes, results[value], label=f'k_values = {value}')
    plt.title('Accuracy vs Sparce Graphs for Different k values')
    plt.xlabel('Graph Size')
    plt.ylabel('Accuracy')
    plt.legend()
    plt.grid(True)
    plt.show()
    

G_sizes3 = []
for i in range(100, 450, 50):
    G_sizes3.append(i)
k_value3 = [1, 2, 5, 10, 15]
source3 = 0
num_trials3 = 25
upper3 = 1000
probability3 = 0.1

#experiment3(G_sizes3, k_value3, source3, upper3, num_trials3, probability3)


