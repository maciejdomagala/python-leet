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
    n=inp()
    s = input()
    
    for i in range(5):
        if (s[:i] + s[-5+i:]).strip() == '2020':
            print 'YES'
            break
    else:
        print 'NO' 

    
