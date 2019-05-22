import networkx as nx
import graph1
import graph2
import graph3
import graph4
import graph5


def find_next_vertex(G):
    
    lista = []
    listb = []
    listc = []
    listd = []
    n = len(G.nodes())
    for items in range(1,n+1):
        if G.nodes[items]['visited'] == 'no':
            lista.append(items)
            if len(lista) == n:
                visited_counter = 1
                return 1
    for items in range(1,n+1):
        if G.nodes[items]['visited'] == 'yes':
            listb = list(G.adj[items])
            for item in listb:
                if G.nodes[item]['visited'] == 'no':
                    listd.append(item)
            listc = listc + listd
    
    return min(listc)
            
    
        
    
        
    
        
    










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
    n = len(G.nodes())
    global kmax 
    
    colorlist = []
    for items in range(1,n+1):
        G.nodes[find_next_vertex(G)]['color'] = find_smallest_color(G,find_next_vertex(G))
        colorlist.append(find_smallest_color(G,find_next_vertex(G)))
        G.nodes[find_next_vertex(G)]['visited'] = 'yes'
        
    kmax = max(colorlist)
        

        
    
        











    print()
    for i in G.nodes():
        print('vertex', i, ': color', G.node[i]['color'])
    print()
    print('The number of colors that Greedy computed is:', kmax)
    print()



print('Graph G1:')
G=graph1.Graph()
G.add_nodes_from(G.nodes(), visited = 'no')
greedy(G)



print('Graph G2:')
G=graph2.Graph()
G.add_nodes_from(G.nodes(), visited = 'no')
greedy(G)



print('Graph G3:')
G=graph3.Graph()
G.add_nodes_from(G.nodes(), visited = 'no')
greedy(G)



print('Graph G4:')
G=graph4.Graph()
G.add_nodes_from(G.nodes(), visited = 'no')
greedy(G)


print('Graph G5:')
G=graph5.Graph()
G.add_nodes_from(G.nodes(), visited = 'no')
greedy(G)

