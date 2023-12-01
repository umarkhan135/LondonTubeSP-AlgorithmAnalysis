from final_project_part1 import *
from dijkstra_relaxation import *
from bellmanford_relaxation import *
import matplotlib.pyplot as plt
import timeit 


'''
*************
Experiment 1
*************



def experiment_helper(G, k_value, source, num_trials):
    count = 0
    for _ in range(num_trials):
        start_time = timeit.default_timer()
        dijkstra_approx(G, source, k_value)
        end_time = timeit.default_timer()
        execution_time = end_time - start_time
        count += execution_time
    return count/num_trials


def experiment1(G_sizes, k_ratios, source, num_trials, upper):
    results = {ratio: [] for ratio in k_ratios}
    
    for size in G_sizes:
        g = create_random_complete_graph(size, upper)
        for ratio in k_ratios:
            k_value = ratio
            avg_time = experiment_helper(g, k_value, source, num_trials)
            results[ratio].append(avg_time)
    
    for ratio in k_ratios:
        plt.plot(G_sizes, results[ratio], label=f'k_value = {ratio}')
    
    plt.xlabel('Graph sizes')
    plt.ylabel('Time')
    plt.title('Graph size VS time for certain k values')
    plt.grid(True)
    plt.legend()
    plt.show()
    
G_sizes = []
for i in range(100, 525, 25):
    G_sizes.append(i)
k_ratios = [1, 5, 10, 25]
source = 0
num_trials = 10
upper = 1000

#experiment1(G_sizes, k_ratios, source, num_trials, upper)
'''

'''
*************
Experiment 2
*************
'''


def experiment1_helper(G, source, k_ratios, numtrials):
    results = {}
    graph_size = G.number_of_nodes()
    dist_standard = dijkstra(G, source)
    total_distance_standard = total_dist(dist_standard)

    for ratio in k_ratios:
        relative_error = 0
        for i in range(numtrials):
            k = ratio
            dist_approx = dijkstra_approx(G, source, k)
            total_distance_approx = total_dist(dist_approx)

            # Correctly calculate accuracy
            relative_error += abs(total_distance_approx - total_distance_standard) / total_distance_standard
        results[ratio] = relative_error/numtrials
    
    return results

def experiment1(G_sizes, k_ratios, source, upper, numtrials):
    results = {ratio: [] for ratio in k_ratios}
    for size in G_sizes:
        G = create_random_complete_graph(size, upper)
        accuracies = experiment1_helper(G, source, k_ratios, numtrials)
        for ratio in k_ratios:
            results[ratio].append(accuracies[ratio])
            
    for ratio in k_ratios:
        plt.plot(G_sizes, results[ratio], label=f'k_value = {ratio}')
    plt.title('Accuracy vs Graph Size for Different k Ratios')
    plt.xlabel('Graph Size')
    plt.ylabel('Accuracy')
    plt.legend()
    plt.grid(True)
    plt.show()
    

G_sizes2 = []
for i in range(100, 450, 50):
    G_sizes2.append(i)
k_ratios2 = [1, 2, 5, 10, 15]
source2 = 0
num_trials2 = 25
upper2 = 1000

#experiment1(G_sizes2, k_ratios2, source2, upper2, num_trials2)


'''
*************
Experiment 3
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

def experiment2_helper(G, source, k_ratios, numtrials):
    results = {}
    dist_standard = dijkstra(G, source)
    total_distance_standard = total_dist(dist_standard)

    for ratio in k_ratios:
        relative_error = 0
        for i in range(numtrials):
            k = ratio
            dist_approx = dijkstra_approx(G, source, k)
            total_distance_approx = total_dist(dist_approx)

            # Correctly calculate accuracy
            relative_error += abs(total_distance_approx - total_distance_standard) / total_distance_standard
        results[ratio] = relative_error/numtrials
    
    return results

def experiment2(G_size, k_ratios, source, upper, numtrials, probabilities):
    results = {ratio: [] for ratio in k_ratios}
    
    for prob in probabilities:
        G = create_sparse_graph(G_size, prob, upper)
        accuracies = experiment2_helper(G, source, k_ratios, numtrials)
        for ratio in k_ratios:
            results[ratio].append(accuracies[ratio])
            
    for ratio in k_ratios:
        plt.plot(probabilities, results[ratio], label=f'k_ratio = {ratio}')
    plt.title('Accuracy vs Graph Density for Different k Ratios')
    plt.xlabel('Graph Density (Probability)')
    plt.ylabel('Accuracy')
    plt.legend()
    plt.grid(True)
    plt.show()
    

G_sizes3 = 200
k_ratios3 = [1, 2, 5, 10, 15]
source3 = 0
num_trials3 = 10
upper3 = 1000
probability = [0.1, 0.2, 0.3, 0.5, 0.75]

#experiment2(G_sizes3, k_ratios3, source3, num_trials3, upper3, probability)



'''
*************
Experiment 4
*************
'''


def experiment3_helper(G, source, k_ratios, numtrials):
    results = {}
    graph_size = G.number_of_nodes()
    dist_standard = dijkstra(G, source)
    total_distance_standard = total_dist(dist_standard)

    for ratio in k_ratios:
        relative_error = 0
        for i in range(numtrials):
            k = ratio
            dist_approx = dijkstra_approx(G, source, k)
            total_distance_approx = total_dist(dist_approx)

            # Correctly calculate accuracy
            relative_error += abs(total_distance_approx - total_distance_standard) / total_distance_standard
        results[ratio] = relative_error/numtrials
    
    return results

def experiment3(G_sizes, k_ratios, source, upper, numtrials, probability):
    results = {ratio: [] for ratio in k_ratios}
    for size in G_sizes:
        G = create_sparse_graph(size, probability, upper)
        accuracies = experiment3_helper(G, source, k_ratios, numtrials)
        for ratio in k_ratios:
            results[ratio].append(accuracies[ratio])
            
    for ratio in k_ratios:
        plt.plot(G_sizes, results[ratio], label=f'k_values = {ratio}')
    plt.title('Accuracy vs Sparce Graphs for Different k Ratios')
    plt.xlabel('Graph Size')
    plt.ylabel('Accuracy')
    plt.legend()
    plt.grid(True)
    plt.show()
    

G_sizes4 = []
for i in range(100, 450, 50):
    G_sizes4.append(i)
k_ratios4 = [1, 2, 5, 10, 15]
source4 = 0
num_trials4 = 25
upper4 = 1000
probability2 = 0.1

experiment3(G_sizes4, k_ratios4, source4, upper4, num_trials4, probability2)


