
import time
import sys
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
def hierarchy_pos(G, root=None, width=1., vert_gap = 0.2, vert_loc = 0, xcenter = 0.5):
    if not nx.is_tree(G):
        raise TypeError('cannot use hierarchy_pos on a graph that is not a tree')

    if root is None:
        if isinstance(G, nx.DiGraph):
            root = next(iter(nx.topological_sort(G)))  #allows back compatibility with nx version 1.11
        else:
            root = random.choice(list(G.nodes))

    def _hierarchy_pos(G, root, width=1., vert_gap = 0.2, vert_loc = 0, xcenter = 0.5, pos = None, parent = None):
        '''
        see hierarchy_pos docstring for most arguments

        pos: a dict saying where all nodes go if they have been assigned
        parent: parent of this branch. - only affects it if non-directed

        '''

        if pos is None:
            pos = {root:(xcenter,vert_loc)}
        else:
            pos[root] = (xcenter, vert_loc)
        children = list(G.neighbors(root))
        if not isinstance(G, nx.DiGraph) and parent is not None:
            children.remove(parent)  
        if len(children)!=0:
            dx = width/len(children) 
            nextx = xcenter - width/2 - dx/2
            for child in children:
                nextx += dx
                pos = _hierarchy_pos(G,child, width = dx, vert_gap = vert_gap, 
                                    vert_loc = vert_loc-vert_gap, xcenter=nextx,
                                    pos=pos, parent = root)
        return pos


    return _hierarchy_pos(G, root, width, vert_gap, vert_loc, xcenter)

def getmatrix(a):
    result1 = []
    b = a.shape[0]
    slice_one = a[1:b,1:b]
    upperab = a[0,1:b]
    leftab = a[0:b,0]
    mini = int(a[1,2])
    x = 1
    y = 0
    for items in range(0,b-1):
        for item in range(0,b-1):
            slice_one[items,item] = int(slice_one[items,item])
            if slice_one[items,item] != 0 and slice_one[items,item] < mini:
                mini = slice_one[items,item]
                x = item
                y = items
    result1.append(upperab[x])
    result1.append(leftab[y+1])
    for items in range(0,b-1):
        if items == x or items == y:
            continue
        else:
            count = (slice_one[items,x]+slice_one[items,y])/2
            slice_one[items,x] = count
            slice_one[x,items] = count
    slice_one = np.delete(slice_one,[y],axis = 0)
    slice_one = np.delete(slice_one,[y],axis = 1)
    upperab[x] = upperab[y] + upperab[x]
    result1.append(upperab[x])
    leftab[x+1] = leftab[y+1] + leftab[x+1]
    upperab = np.delete(upperab,[y])
    leftab = np.delete(leftab,[y+1])
    result = np.vstack((upperab,slice_one))
    leftab = np.array([leftab])
    result = np.hstack((leftab.T,result))
    result1.append(result)
    return result1

def WPGMA(file1):
    start = time.time()
    a = np.loadtxt(file1,dtype = object)
    result = getmatrix(a)
    b = result[3]
    print(b)
    
    n = b.shape[0]
    G = nx.Graph()
    G.clear()
    G.add_node(result[0])
    G.add_node(result[1])
    G.add_node(result[2])
    G.add_edge(result[0],result[2])
    G.add_edge(result[1],result[2])
    while n > 3 or n == 3:
        result = getmatrix(b)
        
        b = result[3]
        print(b)
        check = G.nodes()
        if result[0] not in check:
            G.add_node(result[0])
        if result[1] not in check:
            G.add_node(result[1])
        G.add_node(result[2])
        G.add_edge(result[0],result[2])
        G.add_edge(result[1],result[2])   
        n = b.shape[0]
    
    
    
    checknode = list(G.nodes)
    checkcheck = ''
    checklength = 0
    for items in checknode:
        if len(items) > checklength:
            checklength = len(items)
            checkcheck = items
    
        
        
    
    pos = hierarchy_pos(G,checkcheck)    
    nx.draw(G, pos=pos, with_labels=True)
    stop = time.time()
    time_taken=stop-start
    print('Time taken: '+str(time_taken))
    
    plt.savefig('hierarchy.png')
                       
                
            
    
    
    



