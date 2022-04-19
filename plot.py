import matplotlib.pyplot as plt
from collections import defaultdict
# from bakly import Graph

def plot(graph, file_name=None):
    num_nodes_by_degrees = defaultdict(int)
    for degree in graph.deg_V.values():
        num_nodes_by_degrees[degree] += 1

    plt.title('Node degree distribution')
    plt.scatter(num_nodes_by_degrees.keys(), num_nodes_by_degrees.values())

    plt.xlabel('Degree')
    plt.xscale('log')

    plt.ylabel('# Nodes')
    plt.yscale('log')

    if file_name:
        plt.savefig(file_name)
    plt.show()

# g = Graph()
# g.generate(1, 1000, 5)
# plot(g, 'fn.png')
