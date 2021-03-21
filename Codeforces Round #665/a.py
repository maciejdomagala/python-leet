
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
    n, k = invr()

    if k >= n:
        print k-n
    else:
        if (k+n)%2 == 0:
            print 0
        else:
            print 1