
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
    s = insr()
    s = [int(a) for a in s]
    c = 0

    d = defaultdict(int)

    pre = [0]*(n)
    ans = 0

    d[0] = 1

    for i in range(n):
        pre[i] = pre[i-1]+s[i]
        ans += d[pre[i]-i-1]
        d[pre[i]-i-1] += 1


    # print pre
    # ca = Counter(pre)
    print ans

    # print ca

    # for i in ca.keys():
    #     x = ca[i]
    #     ans += (x*(x-1))//2

    # print ans



# for _ in range(inp()):

#     n = inp()
#     s = insr()
#     s = [int(a) for a in s]
#     c = 0
#     dp = [[0] for i in range(n)]

#     dp[0] = [(1, s[0])]
#     if s[0] == 1:
#         c += 1
#     # print dp
#     for i in range(1, n):
#         dp[i][0] = (1, s[i])
#         if s[i] == 1:
#             c += 1
#         for j in range(1, i+1):
#             dp[i].append((j+1, dp[i-1][j-1][1] + s[i]))

#             if j+1 == (dp[i-1][j-1][1] + s[i]):
#                 c += 1

#             # print dp

#     print c

"""
1
6
120102
"""