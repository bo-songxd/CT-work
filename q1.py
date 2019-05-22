#!/usr/bin/python
import time
import sys
import numpy as np

# YOUR FUNCTIONS GO HERE -------------------------------------
# 1. Populate the scoring matrix and the backtracking matrix

# ------------------------------------------------------------
def smatrix(a,b):
    nsq1 = len(a)
    nsq2 = len(b)
    smatrix = np.zeros((nsq2+1,nsq1+1),dtype=int)
    up ={}
    dia = {}
    for items in range (1,nsq2+1):
        smatrix[items,0] = -2*items
    for items in range(1,nsq1+1):
        up[items] = -2*items
        dia[items] = -2*(items-1)
        smatrix[0,items] = -2*items
    bamatrix = np.zeros((nsq2+1,nsq1+1),dtype=object)
    for items in range (1,nsq2+1):
        bamatrix[items,0] = 'U'
    for items in range(1,nsq1+1):
        bamatrix[0,items] = 'L'
    
    for items in range(1,nsq2+1):
        dia[1] = -2*(items-1)
        pause= dia[1]
        lefter = -2*items
        for item in range(1,nsq1+1):
            c = 0
            aitem = a[item-1]
            bitem = b[items-1]
            if aitem == bitem:
                if aitem == 'A':
                    c = c +4
                if aitem == 'C':
                    c = c + 3
                if aitem == 'G':
                    c = c +2
                if aitem == 'T':
                    c = c +1
            else:
                c = -3
            
            diagonal = c+dia[item]
            dia[item] = pause
            
            upper = up[item]-2
            
            score = max(diagonal,upper,lefter)
            up[item] = score
            pause= score
            

            smatrix[items,item] = score
            bma = ''
            if diagonal == score:
                bma = bma + 'D'
            if upper == score:
                bma = bma + 'U'
            if lefter ==  score:
                bma = bma + 'L'
            bamatrix[items,item] = bma
            lefter = score -2
    bamatrix[0,0] = 'END'
    lal = []
    lal.append(smatrix)
    lal.append(bamatrix)
    return lal
# DO NOT EDIT ------------------------------------------------
# Given an alignment, which is two strings, display it

def displayAlignment(alignment):
    string1 = alignment[0]
    string2 = alignment[1]
    string3 = ''
    for i in range(min(len(string1),len(string2))):
        if string1[i]==string2[i]:
            string3=string3+"|"
        else:
            string3=string3+" "
    print('Alignment ')
    print('String1: '+string1)
    print('         '+string3)
    print('String2: '+string2+'\n\n')

# ------------------------------------------------------------


# DO NOT EDIT ------------------------------------------------
# This opens the files, loads the sequences and starts the timer
file1 = open(sys.argv[1], 'r')
seq1=file1.read()
file1.close()
file2 = open(sys.argv[2], 'r')
seq2=file2.read()
file2.close()
start = time.time()

#-------------------------------------------------------------


# YOUR CODE GOES HERE ----------------------------------------
# The sequences are contained in the variables seq1 and seq2 from the code above.
# Intialise the scoring matrix and backtracking matrix and call the function to populate them
# Use the backtracking matrix to find the optimal alignment 
# To work with the printing functions below the best alignment should be called best_alignment and its score should be called best_score.
resultlist = smatrix(seq1,seq2)
backtrackingmatrix = resultlist[1]

global count
count = False
n1 = len(seq1)
n2 = len(seq2)

def check(n1,n2,mat):
    lista = []
    lala = True
    while mat[n2,n1] != 'END':
        if len(mat[n2,n1]) > 1 and lala :
            part = mat[n2,n1][0]
            mat[n2,n1] = mat[n2,n1][1:len(mat[n2,n1])]
            global count
            count = True
            lala = False
        else:
            part = mat[n2,n1][0]
        if part =='U':
            result1 = part
            n2 = n2 - 1
            lista.append(result1)
            continue
        if part == 'L':
            result1 = part
            n1 = n1 - 1
            lista.append(result1)
            continue
        if part == 'D':
            result1 = part
            n1 = n1 - 1
            n2 = n2 - 1
            lista.append(result1)
            continue
       
    return lista
result = []

pa = check(n1,n2,backtrackingmatrix)
result.append(pa)

while count:
    count = False
    lala = True
    pi = check(n1,n2,backtrackingmatrix)
    result.append(pi)
"""
stop2 = time.time()
print('function check',stop2 - stop1)
"""
alliment = []
best_alignment = []
best_score =resultlist[0][n2,n1]
alliment1 = []
for items in result:
    lalal = []
    lalal1 = []
    ccc = 0
    ddd = 0
    for item in items:
        if item == 'D' or item == 'U':
            ccc = ccc-1
            lalal.append(seq2[ccc])
        if item == 'L':
            lalal.append('-')
        if item == 'D' or item == 'L':
            ddd = ddd-1
            lalal1.append(seq1[ddd])
        if item == 'U':
            lalal1.append('-')
    alliment.append(lalal)
    alliment1.append(lalal1)
"""
stop3 = time.time()
print('backtracking',stop3 - stop2)
"""
for items in alliment:
    items.reverse()
for items in alliment1:
    items.reverse()
    sf = 0
for item in range(0,len(alliment)):
    for items in range(0,len(alliment[item])):
        if alliment[item][items] == alliment1[item][items]:
            if alliment[item][items] == 'A':
                sf = sf +4
            if alliment[item][items] == 'C':
                sf = sf +3
            if alliment[item][items] == 'G':
                sf = sf +2
            if alliment[item][items] == 'T':
                sf = sf +1
        if alliment[item][items] != alliment1[item][items]:
            if alliment[item][items] == '-' or alliment1[item][items] == '-':
                sf = sf - 2
            else:
                sf = sf - 3
        
        if sf == best_score:
            
            result1 = ''.join(str(e) for e in alliment[item])
            result2 = ''.join(str(e) for e in alliment1[item])
            best_alignment.append(result1)
            best_alignment.append(result2)

#-------------------------------------------------------------


# DO NOT EDIT (unless you want to turn off displaying alignments for large sequences)------------------
# This calculates the time taken and will print out useful information 
stop = time.time()
time_taken=stop-start

# Print out the best
print('Time taken: '+str(time_taken))
print('Best (score '+str(best_score)+'):')
print(best_alignment)
displayAlignment(best_alignment)
#-------------------------------------------------------------

