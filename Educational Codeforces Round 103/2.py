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
    n, k = invr()
    prices = invr()

    for i in range(len(prices)-1):
        curr = prices[i+1]/sum(prices[:i+1])
        if curr > k:
            



