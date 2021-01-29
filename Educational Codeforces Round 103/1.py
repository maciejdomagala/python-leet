import sys
from collections import Counter
from copy import copy
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
    n, k = invr()

    w = copy(k)
    while k < n:
        k += w

    c = 0
    while k - c*n > 0:
        c += 1

    print c 
