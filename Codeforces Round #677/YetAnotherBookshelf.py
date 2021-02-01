import sys
input = sys.stdin.readline

from collections import Counter

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

    arr = invr()
    s = ''.join([str(a) for a in arr])
    s = s.strip('0')

    print s.count('0')

