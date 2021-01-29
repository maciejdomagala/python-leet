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
    x = inp()
    ans = []
    if x > 45:
        print -1
        continue
    for i in range(9, 0, -1):
        if x <= i:
            ans.append(x)
            break
        x -= i
        ans.append(i)

    print ''.join([str(a) for a in ans[::-1]])


    
