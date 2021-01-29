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
    nums = invr()
    ans = [0]*len(nums)

    l=0
    r=-1
    for i in range(len(nums)):
        if i % 2 == 0:
            ans[i] = nums[l]
            l += 1
        else:
            ans[i] = nums[r]
            r -= 1

    print(' '.join([str(a) for a in ans]))
    
