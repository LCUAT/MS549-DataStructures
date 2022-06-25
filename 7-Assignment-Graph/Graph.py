import matplotlib.pyplot as plt
import networkx as nx

edges = [['S','A'], ['S','G'], ['S','D'],['D', 'E'], ['A', 'D'], ['A', 'B'], ['B', 'C'], ['C','F'], ['C','t'], ['G','D'],['G','H'], ['H','E'], ['H','I'], ['I','F'], ['I','t'], ['E','F']]
G = nx.Graph()
G.add_edges_from(edges)
pos = nx.spring_layout(G)
plt.figure()
nx.draw(
    G, pos, edge_color='black', width=1, linewidths=1,
    node_size=500, node_color='pink', alpha=0.9,
    labels={node: node for node in G.nodes()}
)
nx.draw_networkx_edge_labels(
    G, pos,
    edge_labels=
    {
        ('S', 'A'): 1, 
        ('S','G'):6,
        ('S','D'):4,
        ('A','D'):3,
        ('A', 'B'):2,
        ('B','C'):2,
        ('C','F'):1,
        ('C','t'):4,
        ('G','D'):2,
        ('G','H'):6,
        ('H','E'):2,
        ('H','I'):6,
        ('I', 'F'):1,
        ('I', 't'):4,
        ('D','E'):3,
        ('E','F'):3

    },
    font_color='red'
)
plt.axis('off')
plt.show()