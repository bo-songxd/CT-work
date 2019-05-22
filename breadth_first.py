import networkx as nx
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
        
    
    
    











G6=graph6.Graph()
a=12
b=40
print('Graph G6:')
print('The distance between vertices', a, 'and', b, 'is:', bfs(G6,a,b))
print()

G7=graph7.Graph()
a=5
b=36
print('Graph G7:')
print('The distance between vertices', a, 'and', b, 'is:', bfs(G7,a,b))
print()



G8=graph8.Graph()
a=15
b=35
print('Graph G8:')
print('The distance between vertices', a, 'and', b, 'is:', bfs(G8,a,b))
print()


G9=graph9.Graph()
a=1
b=19
print('Graph G9:')
print('The distance between vertices', a, 'and', b, 'is:', bfs(G9,a,b))
print()



G10=graph10.Graph()
a=6
b=30
print('Graph G10:')
print('The distance between vertices', a, 'and', b, 'is:', bfs(G10,a,b))
print()

