import networkx as nx
import graph1
import graph2
import graph3
import graph4
import graph5


def find_smallest_color(G,i):
    n = len(G.nodes())
    color = 0
    check = []
    adjlist = list(G.adj[i])
    
    for items in adjlist:
        check.append(G.nodes[items]['color'])
   
    wer = []
    for i in check:
        
        if type(i) is str:
            wer.append(i)
    check = [i for i in check if not i in wer or wer.remove(i)]   
    if len(check) == 0:
        color = 1
        return color
                     
    maxcolor = max(check)
    colorlist = []
    for items in range(1,maxcolor+1):
        colorlist.append(items)
    check = [i for i in colorlist if not i in check or check.remove(i)] 
    if len(check)== 0:
        color = maxcolor+1
    if len(check)!= 0:
        color = min(check)
    return color
        
                     
 
        
                     








def greedy(G):
    global kmax
    n = len(G.nodes())
    colorlist = []
    for items in range(1,n+1):
        G.nodes[items]['color'] = find_smallest_color(G,items)
        colorlist.append(find_smallest_color(G,items))
    kmax = max(colorlist)
    
    






    print()
    for i in G.nodes():
        print('vertex', i, ': color', G.node[i]['color'])
    print()
    print('The number of colors that Greedy computed is:', kmax)


print('Graph G1:')
G=graph1.Graph()
greedy(G)


print('Graph G2:')
G=graph2.Graph()
greedy(G)


print('Graph G3:')
G=graph3.Graph()
greedy(G)


print('Graph G4:')
G=graph4.Graph()
greedy(G)


print('Graph G5:')
G=graph5.Graph()
greedy(G)
