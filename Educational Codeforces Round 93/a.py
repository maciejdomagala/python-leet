
from __future__ import division
import sys
input = sys.stdin.readline
import math
from math import sqrt, floor, ceil
from collections import Counter, defaultdict
from copy import deepcopy as dc
# from statistics import median, mean


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

# a = raw_input()

for _ in range(inp()):
    n = inp()
    arr = invr()

    if arr[0] + arr[1] <= arr[-1]:
        print ' '.join(str(a) for a in [1, 2, n])
    else:
        print -1