"""
Module can find a path using nodes in an ACII map.

author: Jaanus
"""
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def draw_maze(labyrinth):
    """Plot background as a maze."""
    plt.figure(num=None, figsize=(20, 20))
    for x in range(len(labyrinth)):
        for y in range(len(labyrinth[x])):
            someX, someY = x, y
            current_axis = plt.gca()
            current_axis.add_patch(Rectangle((someX - .5, someY - .5), 1, 1, facecolor="white", zorder=0))
            if labyrinth[x][y] != ' ':
                current_axis.add_patch(Rectangle((someX - .5, someY - .5), 1, 1, facecolor="grey", zorder=0))


def draw_nodes_and_edges(G, pos, relabel):
    """Save graph with filename graph in a png format."""
    nx.draw(G, pos)
    pos = nx.get_node_attributes(G, 'pos')
    labels = nx.get_edge_attributes(G, 'weight')
    printable_labels = {}
    for neig in labels:
        printable_labels[(neig[0], neig[1])] = labels[neig]
    nx.draw_networkx_edges(G, pos, edgelist=None, width=1.0, edge_color='black', style='solid', alpha=1.0, edge_cmap=None, edge_vmin=None, edge_vmax=None, ax=None, arrows=False, label=None)
    nx.draw_networkx_edge_labels(G, pos, printable_labels)
    nx.draw_networkx_labels(G, pos, relabel)
    # nx.draw_networkx_labels(G, pos)
    plt.savefig('graph.png', dpi=300)


def exceptions(G, x, y):
    """Make a list of exeptions for use in remove_tunnels function."""
    curve_is_not_tunnel = False  # if false loops in mazes have errors
    end_is_bottom_left = True  # will the most bottom and left space be exception
    start_is_up_right = True
    labels = nx.get_edge_attributes(G, 'weight')
    nodes = nx.get_node_attributes(G, 'pos')
    memory = []
    for node in nodes:
        num_edge = []
        for edge in labels:
            if node in edge:
                num_edge.append((edge, labels[edge]))
        if len(num_edge) != 2:
            memory.append(node)
        if nodes[node] == (x, y) and end_is_bottom_left:
            memory.append(node)
        if nodes[node] == (0, 0) and start_is_up_right:
            memory.append(node)
        if len(num_edge) == 2 and node in G.nodes() and node not in memory and curve_is_not_tunnel:
            neighbors = G.neighbors(node)
            if (nodes[node][0] == nodes[neighbors[0]][0] and nodes[node][1] == nodes[neighbors[1]][1]) \
               or (nodes[node][1] == nodes[neighbors[0]][1] and nodes[node][0] == nodes[neighbors[1]][0])\
               or (nodes[node][0] == nodes[neighbors[0]][1] and nodes[node][1] == nodes[neighbors[1]][0])\
               or (nodes[node][1] == nodes[neighbors[0]][0] and nodes[node][0] == nodes[neighbors[1]][1]):
                memory.append(node)
    return memory


def remove_tunnels(G, relabel, exception=[]):
    """Remove nodes with 2 connections."""
    labels = nx.get_edge_attributes(G, 'weight')
    nodes = nx.get_node_attributes(G, 'pos')
    for node in nodes:
        num_edge = []
        for edge in labels:
            if node in edge:
                num_edge.append((edge, labels[edge]))
        if len(num_edge) == 2 and node in G.nodes() and node not in exception:
            if num_edge[0][0][0] == node:
                new1 = num_edge[0][0][1]
            else:
                new1 = num_edge[0][0][0]
            if num_edge[1][0][0] == node:
                new2 = num_edge[1][0][1]
            else:
                new2 = num_edge[1][0][0]
            G.add_edge(new1, new2, weight=num_edge[0][1] + num_edge[1][1])
            G.remove_node(node)
            del relabel[node]
            remove_tunnels(G, relabel, exception)
    return relabel


def create_graph(labyrinth):
    """Create a graph of paths in labyrinth with weights."""
#    draw_maze(labyrinth)
    G = nx.MultiGraph()
    node = 0
    alf = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    relabel = {}
    for x in range(len(labyrinth)):
        for y in range(len(labyrinth[x])):
            if labyrinth[x][y] == ' ':
                node += 1
                relabel[node] = alf[x] + str(y)
                G.add_node(node, pos=(x, y))
    pos = nx.get_node_attributes(G, 'pos')
    for index in pos:
        for i in range(index, len(pos) + 1):
            if pos[index][0] == pos[i][0] and abs(pos[index][1] - pos[i][1]) == 1:
                G.add_edge(index, i, weight=1)
            elif pos[index][1] == pos[i][1] and abs(pos[index][0] - pos[i][0]) == 1:
                G.add_edge(index, i, weight=1)
    exception = exceptions(G, len(labyrinth) - 1, len(labyrinth[0]) - 1)  # changes how remove tunnle works
    relabel = remove_tunnels(G, relabel, exception)
    pos = nx.get_node_attributes(G, 'pos')
#    draw_nodes_and_edges(G, pos, relabel)
    nx.relabel_nodes(G, relabel, copy=False)  # line decides if nodes are named as 1, 2, 3, ... or A0, A1, A2, ...
    return G


def find_shortest_path(graph):
    """Find the shortest path from a graph using networkX module."""
    if len(graph) == 0:
        return
    source = min(graph.nodes())
    end = max(graph.nodes())
    return nx.dijkstra_path(graph, source=source, target=end)


if __name__ == '__main__':
    graph = create_graph([[' ', ' ', ' ', 'X', 'X'],
                          [' ', 'X', ' ', ' ', ' '],
                          ['X', 'X', ' ', 'X', ' ']])
    print(find_shortest_path(graph))
#    graph = create_graph([['X', ' ', ' ', ' ', 'X'],
#                          [' ', ' ', 'X', ' ', ' '],
#                          ['X', 'X', ' ', ' ', ' ']])
#    print(find_shortest_path(graph))
#    print(list(find_shortest_path(create_graph([[' ', ' ', ' ', 'X', 'X'],
#                                                ['X', 'X', ' ', ' ', ' '],
#                                                ['X', 'X', ' ', 'X', 'X']]))))
#    graph = create_graph([[' ']])
#    print(find_shortest_path(graph))
#    graph = create_graph([['X']])
#    print(find_shortest_path(graph))
#    graph = create_graph([' '])
#    print(find_shortest_path(graph))
#    graph = create_graph(['X'])
#    print(find_shortest_path(graph))
#    graph = create_graph(' ')
#    print(find_shortest_path(graph))
#    graph = create_graph('X')
#    print(find_shortest_path(graph))
#    graph = create_graph([[' ', ' ']])
#    print(find_shortest_path(graph))
#    graph = create_graph([' ', ' '])
#    print(find_shortest_path(graph))
#    graph = create_graph('n')
#    print(find_shortest_path(graph))
