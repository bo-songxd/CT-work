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
    
    
        
    
