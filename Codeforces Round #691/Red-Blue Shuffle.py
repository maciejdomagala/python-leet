import sys
from collections import Counter
input = sys.stdin.readline

############ ---- Input Functions ---- ############
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))
def insr2():
    s = input()
    return(s.split(" "))

for _ in range(inp()):
    n = inp()
    a =  insr()
    b = insr()

    ca,cb = 0,0

    for i,j in zip(a,b):
        if int(i) > int(j):
            ca += 1
        elif int(i) < int(j):
            cb += 1

    if ca > cb:
        print 'RED'
    elif ca < cb:
        print 'BLUE'
    else:
        print 'EQUAL'