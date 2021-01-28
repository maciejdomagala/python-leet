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

    a,b,k = invr()
    boys = invr()
    girls = invr()

    cb = Counter(boys)
    cg = Counter(girls)

    ans = 0
    for boy, girl in zip(boys, girls):
        ans += k -( cb[boy] + cg[girl] - 1)
    print ans//2