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

    ans = [a+1 for a in range(n)]
    ans = ans[::-1]
    if n % 2 == 1 and n > 1:
        ans[n//2], ans[n//2 + 1] =  ans[n//2 + 1], ans[n//2]

    print ' '.join([str(a) for a in ans])


