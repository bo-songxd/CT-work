def message(a):
    count = 4
    b = len(a)
    if b == 1:
        if a ==[1]:
            return [0,0,1,1]
        if a == [0]:
            return [0,0,1,0]
    # b is input bit number
    #count is the number of binary bit of length
    while b > 2**count or b == 2**count:
        count = count+1    
    k = 2**count-count-1
    while k< count+b:
        count = count+1
        k = 2**count - count-1
    
    #count = r in dec
    
    format1 = "0"+str(count)+"b"
    ra = format(b,format1)
    
    # ra is a part of result, but now it is a string , becuase bin function output string
    r = []
    for item in ra:
        item = int(item)
        r.append(item)
    final = []
    final = final + r + a
    
    while len(final)!= k:
        final.append(0)
    return final



import numpy as np
def hammingEncoder(m):
    b = len(m)
    if b == 1:
        if m == [0]:
            m = m+m+m
            return m
        if m == [1]:
            m = m+m+m
            return m
        return []
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
            break
    G = hammingGeneratorMatrix(count)
    G = np.array(G)
    m = np.array(m)
    C = m.dot(G)
    d = len(C)
    for items in range(d):
        if C[items] % 2 == 0:
            C[items] = 0
        if C[items] % 2 ==1:
            C[items] = 1
    C = np.array(C).tolist()
    return C

def hammingDecoder(m):
    b = len(m)
    if b == 3:
        zerolist = 0
        onelist = 0
        for item in m:
            if item == 0:
                zerolist = zerolist + 1
            if item == 1:
                onelist = onelist + 1
        if onelist > zerolist:
            return [1,1,1]
        if onelist < zerolist:
            return [0,0,0]
            

    if b < 7:
        return []
    count = 3
    while b > 7 or b == 7:
        
        k = 2**count -1
        if b == k:
            break
        if b < k:
            return []
        if b > k:
            count = count+1
    Hnumber = 2**count - 1
    H = np.array([]).reshape(0,count)
    for items in range(1,Hnumber+1):
        la = decimalToVector(items,count)
        H =np.vstack([H,la])
    
    
    m = np.array(m)
    A = m.dot(H)
    
    add = 0
    lala = len(A)
    for items in range(lala):
        if A[items]%2 == 0:
            A[items] = 0
        if A[items]%2 ==1:
            A[items] = 1
        add = add + A[items]
    
    if add == 0:
        m = np.array(m).tolist()
        return m
    else:
        alength = len(A)
        copylength = alength
        check = 0
        result = 0
        for items in range(alength):
            result = result + A[check]*(2**(copylength-1))
            copylength = copylength - 1
            check = check+1
    result = int(result)
    
    m[result-1] = m[result-1]+1
    if m[result-1]%2 == 0:
        m[result-1] = 0
    if m[result-1]%2 == 1:
        m[result-1] =1
    m = np.array(m).tolist()       
    return m
    
        
def messageFromCodeword(c):
    b = len(c)
    if b == 3:
        if c[0]==c[1] and c[1] == c[2]:
            d = []
            d.append(c[0])
            return d
        else:
            return []
    count = 3
    if b < 3 or 3<b<7:
        return []
    while b > 7 or b == 7:
        
        k = 2**count -1
        if b == k:
            break
        if b < k:
            return []
        if b > k:
            count = count+1
    unwant = []
    for items in range (0,count):
        unwant.append(2**items-1)
    want = []
    for items in range (0,k):
        if items not in unwant:
            want.append(items)
    result = []
    for items in want:
        result.append(c[items])
    Hnumber = 2**count - 1
    H = np.array([]).reshape(0,count)
    for items in range(1,Hnumber+1):
        la = decimalToVector(items,count)
        H =np.vstack([H,la])
    c = np.array(c)
    A = c.dot(H)
    add = 0
    lala = len(A)
    for items in range(lala):
        if A[items]%2 == 0:
            A[items] = 0
        if A[items]%2 ==1:
            A[items] = 1
        add = add + A[items]
    if add == 0:
        result = np.array(result).tolist()
        return result
    else:
        return[]
import math
def dataFromMessage(m):
    b = len(m)
    if b == 1:
        return m
    count = 3
    if 1<b<4:
        return []
    if b == 4:
        pass
    while b > 4:
        k = 2**count-count-1
        if b > k:
            count = count+1
        if b == k:
            break
        if b < k:
            return []
    numberlist = []
    for items in range(count):
        numberlist.append(m[items])
    lala = ''.join(str(e) for e in numberlist)
    lala2 = 0
    for items in lala:
        lala2 = lala2*2 + int(items)
    k = 2**count - count - 1
    if lala2+count > k:
        return []
    else:
        result = []
        for items in range(lala2):
            result.append(m[items+count])
    
    return result
        
    
def repetitionEncoder(m,n):
    b = len(m)
    if b != 1:
        return[]
    else:
        result=[]
        result = n*m
        return result
    
def repetitionDecoder(v):
    b = len(v)
    zerolist=0
    onelist=0
    for items in v:
        if items == 0:
            zerolist = zerolist + 1
        if items == 1:
            onelist = onelist + 1
    if zerolist == onelist:
        return []
    if zerolist> onelist:
        result = []
        result.append(0)
        return result
    if onelist > zerolist:
        result = []
        result.append(1)
        return result
        


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




    
        
    
    
    
    
