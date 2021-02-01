import sys
input = sys.stdin.readline

from collections import Counter
from itertools import groupby

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
    nums=invr()

    nums = [k for k,g in groupby(nums)]

    ca = Counter(nums)

    start, end = nums[0], nums[-1]

    ca[start] -= 1
    ca[end] -= 1

    print min(ca.values()) + 1



        