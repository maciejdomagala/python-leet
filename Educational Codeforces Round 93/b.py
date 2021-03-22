
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
    s = insr()

    seg = []
    c = 0

    for  a in s:
        if a == '1':
            c += 1
        else:
            seg.append(c)
            c = 0

    seg.append(c)

    seg.sort(reverse=True)
    score = 0

    # print seg

    for i in range(len(seg)):
        if i % 2 == 0:
            score += seg[i]

    print score

