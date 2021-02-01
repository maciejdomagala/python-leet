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

    m = max(arr)

    if len(set(arr)) == 1:
        print -1
        continue

    ans = -1

    for i, a in enumerate(arr):
        if a == m:
            if i == 0:
                if arr[1] < a:
                    ans = i+1
                    continue
            elif i == len(arr)-1:
                if arr[i-1] < a:
                    ans = i+1
                    continue
            else:
                if arr[i-1] < a or arr[i+1] < a:
                    ans = i+1
                    continue

    print ans
