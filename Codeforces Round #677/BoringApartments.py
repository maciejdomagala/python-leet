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

    s = str(n)

    a = (int(s[0]) - 1)*10
    
    b = (len(s)*(len(s)-1))//2 + len(s)

    print a+b

