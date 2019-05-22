#function HammingG
#input: a number r
#output: G, the generator matrix of the (2^r-1,2^r-r-1) Hamming code
def hammingGeneratorMatrix(r):
    n = 2**r-1
    
    #construct permutation pi
    pi = []
    for i in range(r):
        pi.append(2**(r-i-1))
    for j in range(1,r):
        for k in range(2**j+1,2**(j+1)):
            pi.append(k)

    #construct rho = pi^(-1)
    rho = []
    for i in range(n):
        rho.append(pi.index(i+1))

    #construct H'
    H = []
    for i in range(r,n):
        H.append(decimalToVector(pi[i],r))

    #construct G'
    GG = [list(i) for i in zip(*H)]
    for i in range(n-r):
        GG.append(decimalToVector(2**(n-r-i-1),n-r))

    #apply rho to get Gtranpose
    G = []
    for i in range(n):
        G.append(GG[rho[i]])

    #transpose    
    G = [list(i) for i in zip(*G)]

    return G


#function decimalToVector
#input: numbers n and r (0 <= n<2**r)
#output: a string v of r bits representing n
def decimalToVector(n,r): 
    v = []
    for s in range(r):
        v.insert(0,n%2)
        n //= 2
    return v

import numpy as np
def hammingEncoder(m):
    b = len(m)
    if b == 1:
        re = m+m+m
        return re
    if b>1 and b<4:
        return []
    if b == 4:
        count = 3
        k = 4
    if b > 4:
        count = 4
        k = 2**count-count-1
        while b > k:
            count = count+1
            k = 2**count-count-1
        while b< k:
            return []
        while b == k:
            continue
    G = hammingGeneratorMatrix(count)
    G = np.array(G)
    m = np.array(m)
    C = m.dot(G)
    return C

