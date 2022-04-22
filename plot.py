import matplotlib.pyplot as plt
from collections import defaultdict

def plot_from_file(graph_file_name, png_name=None):
    num_nodes_by_degrees = defaultdict(int)
    graph_file = open(graph_file_name, "r")
    n = int(graph_file.readline())
    
    for i in range(n):
        line = [int(x) for x in graph_file.readline().split()]
        for j in range(n):
            if i == j:
                num_nodes_by_degrees[j] += sum(line)
            num_nodes_by_degrees[j] += line[j]

    # for i in range(n):
        # print(f"{i} >> {num_nodes_by_degrees[i]}")
    graph_file.close()

    plt.title('Node degree distribution')
    plt.scatter(num_nodes_by_degrees.keys(), num_nodes_by_degrees.values())

    plt.xlabel('Degree')
    plt.xscale('log')

    plt.ylabel('# Nodes')
    plt.yscale('log')

    if png_name:
        plt.savefig(png_name)
    plt.show()

plot_from_file('graph.txt', 'plot.png')
