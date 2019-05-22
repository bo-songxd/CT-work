import networkx as nx
import random as rd
import graph6
import graph7
import graph8
import graph9
import graph10

def bfs(G,a,b):
    G.add_nodes_from(G.nodes(), label = -1) # initialization of all labels
    G.node[a]['label'] = 0
    ba = []
    count = 0
    for items in list(G.nodes()):
        if G.node[items]['label'] == -1:
            ba.append(items)
    while len(ba) != 0:
        c = []
        for items in list(G.nodes()):
            if G.nodes[items]['label'] == count:
                d = list(G.adj[items])
                e = []
                for items in d:
                    if G.nodes[items]['label'] == -1:
                        e.append(items)
                c = c + e
        ba = list(set(ba) - set(c))
        count = count + 1
        for items in c:
            G.node[items]['label'] = count
    return G.node[b]['label']

def bfs1(G,a):
    n= len(G.nodes())
    G.add_nodes_from(G.nodes(), label = -1) # initialization of all labels
    G.node[a]['label'] = 0
    ba = []
    count = 0
    for items in list(G.nodes()):
        if G.node[items]['label'] == -1:
            ba.append(items)
    while len(ba) != 0:
        c = []
        for items in list(G.nodes()):
            if G.nodes[items]['label'] == count:
                d = list(G.adj[items])
                e = []
                for items in d:
                    if G.nodes[items]['label'] == -1:
                        e.append(items)
                c = c + e
        ba = list(set(ba) - set(c))
        count = count + 1
        for items in c:
            G.node[items]['label'] = count
    result = []
    for items in range(1,n+1):
        result.append(G.node[items]['label'])
    result2 = max(result)
    result1 = []
    for items in range(1,n+1):
        if G.node[items]['label'] == result2:
            result1.append(items)
    return result1
def max_distance(G):
    n = len(G.nodes())
    a = rd.randint(1,n)
    G.add_nodes_from(G.nodes(), label = -1 , visited = 'no')
    c = bfs1(G,a)
    result = []
    for items in c:
        G.add_nodes_from(G.nodes(), label = -1 , visited = 'no')
        d = bfs1(G,items)
        result.append(bfs(G,items,d[0]))
    return max(result)























print()
G6=graph6.Graph()
print('The diameter of G6 (i.e. the maximum distance between two vertices) is:', max_distance(G6))
print()



G7=graph7.Graph()
print('The diameter of G7 (i.e. the maximum distance between two vertices) is:', max_distance(G7))
print()



G8=graph8.Graph()
print('The diameter of G8 (i.e. the maximum distance between two vertices) is:', max_distance(G8))
print()


G9=graph9.Graph()
print('The diameter of G9 (i.e. the maximum distance between two vertices) is:', max_distance(G9))
print()


G10=graph10.Graph()
print('The diameter of G10 (i.e. the maximum distance between two vertices) is:', max_distance(G10))
print()

